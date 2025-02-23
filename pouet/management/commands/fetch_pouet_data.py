import datetime
import gzip
import json
import time

import requests
from django.core.management.base import BaseCommand

from demoscene.models import Releaser
from pouet.matching import automatch_productions, get_pouetable_prod_types
from pouet.models import Group, Production


class Command(BaseCommand):
    help = "Import latest Pouet data dump from data.pouet.net"

    def handle(self, *args, **kwargs):
        verbose = kwargs['verbosity'] >= 1

        # Dumps are published every Wednesday morning, so find out when last Wednesday was
        today = datetime.date.today()
        days_since_wednesday = (today.weekday() - 2) % 7
        wednesday = today - datetime.timedelta(days=days_since_wednesday)
        datestamp = wednesday.strftime('%Y%m%d')
        monthstamp = wednesday.strftime('%Y%m')

        if verbose:
            print("importing groups...")
        groups_url = "https://data.pouet.net/dumps/%s/pouetdatadump-groups-%s.json.gz" % (monthstamp, datestamp)
        r = requests.get(groups_url, stream=True)
        groups_file = gzip.GzipFile(fileobj=r.raw)

        groups_imported = 0
        groups_created = 0

        group_db_ids = {}

        def handle_group(group_data):
            nonlocal groups_imported, groups_created
            if 'id' in group_data:
                group, created = Group.objects.update_or_create(pouet_id=group_data['id'], defaults={
                    'name': group_data['name'],
                    'demozoo_id': group_data['demozoo'],
                    'last_seen_at': datetime.datetime.now(),
                })
                group_db_ids[group_data['id']] = group.id
                groups_imported += 1
                if groups_imported % 1000 == 0 and verbose:  # pragma: no cover
                    print("%d groups imported" % groups_imported)

                if created:
                    groups_created += 1

        json.load(groups_file, object_hook=handle_group)
        groups_file.close()
        if verbose:
            print("done. %d groups imported, of which %d newly created" % (groups_imported, groups_created))

        if verbose:
            print("importing prods...")
        prods_url = "https://data.pouet.net/dumps/%s/pouetdatadump-prods-%s.json.gz" % (monthstamp, datestamp)
        r = requests.get(prods_url, stream=True)
        prods_file = gzip.GzipFile(fileobj=r.raw)

        prods_imported = 0
        prods_created = 0

        def handle_prod(prod_data):
            nonlocal prods_imported, prods_created, group_db_ids
            # prods JSON contains various nested objects, but only prod entries have a 'download' field
            if 'download' in prod_data:
                prod, created = Production.objects.update_or_create(pouet_id=prod_data['id'], defaults={
                    'name': prod_data['name'],
                    'last_seen_at': datetime.datetime.now(),
                })
                prod.groups.set([
                    group_db_ids[group['id']]
                    for group in prod_data['groups']
                ])

                prods_imported += 1
                if prods_imported % 1000 == 0 and verbose:  # pragma: no cover
                    print("%d prods imported" % prods_imported)

                if created:
                    prods_created += 1

            return prod_data

        json.load(prods_file, object_hook=handle_prod)
        prods_file.close()
        if verbose:
            print("done. %d prods imported, of which %d newly created" % (prods_imported, prods_created))

        # garbage-collect productions / groups that haven't been seen for 30 days (i.e. have been deleted from Pouet)
        last_month = datetime.datetime.now() - datetime.timedelta(days=30)
        Production.objects.filter(last_seen_at__lt=last_month).delete()
        Group.objects.filter(last_seen_at__lt=last_month).delete()

        if verbose:
            print("automatching prods...")
        pouetable_prod_types = get_pouetable_prod_types()
        for i, releaser in enumerate(Releaser.objects.filter(external_links__link_class='PouetGroup').only('id')):
            automatch_productions(releaser, pouetable_prod_types=pouetable_prod_types)
            if i % 10 == 0 and i != 0:  # pragma: no cover
                if verbose:
                    print("%d releasers automatched" % i)
                time.sleep(2)
