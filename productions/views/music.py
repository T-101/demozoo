from __future__ import absolute_import, unicode_literals

import datetime
import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from read_only_mode import writeable_site_required

from awards.models import Event
from comments.forms import CommentForm
from comments.models import Comment
from demoscene.models import Edit
from demoscene.shortcuts import get_page
from productions.carousel import Carousel
from productions.forms import CreateMusicForm, MusicIndexFilterForm, ProductionDownloadLinkFormSet, ProductionTagsForm
from productions.models import Byline, Production, ProductionType
from productions.views.generic import IndexView, ShowView, apply_order


class MusicIndexView(IndexView):
    supertype = 'music'
    template = 'music/index.html'
    filter_form_class = MusicIndexFilterForm


class MusicShowView(ShowView):
    supertype = 'music'

    def get_context_data(self):
        context = super().get_context_data()

        context['featured_in_productions'] = [
            appearance.production for appearance in
            self.production.appearances_as_soundtrack.prefetch_related(
                'production__author_nicks__releaser', 'production__author_affiliation_nicks__releaser'
            ).order_by('production__release_date_date')
        ]
        context['packed_in_productions'] = [
            pack_member.pack for pack_member in
            self.production.packed_in.prefetch_related(
                'pack__author_nicks__releaser', 'pack__author_affiliation_nicks__releaser'
            ).order_by('pack__release_date_date')
        ]

        return context


def history(request, production_id):
    production = get_object_or_404(Production, id=production_id)
    if production.supertype != 'music':
        return HttpResponseRedirect(production.get_history_url())
    return render(request, 'productions/history.html', {
        'production': production,
        'edits': Edit.for_model(production, request.user.is_staff),
    })


@writeable_site_required
@login_required
def create(request):
    if request.method == 'POST':
        production = Production(updated_at=datetime.datetime.now())
        form = CreateMusicForm(request.POST, instance=production)
        download_link_formset = ProductionDownloadLinkFormSet(request.POST, instance=production)
        if form.is_valid() and download_link_formset.is_valid():
            form.save()
            download_link_formset.save_ignoring_uniqueness()
            form.log_creation(request.user)
            return HttpResponseRedirect(production.get_absolute_url())
    else:
        form = CreateMusicForm(initial={
            'byline': Byline.from_releaser_id(request.GET.get('releaser_id'))
        })
        download_link_formset = ProductionDownloadLinkFormSet()
    return render(request, 'music/create.html', {
        'form': form,
        'download_link_formset': download_link_formset,
    })
