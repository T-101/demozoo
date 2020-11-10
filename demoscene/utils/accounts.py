from __future__ import absolute_import, unicode_literals

# list from https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=<demozoo server IP>&port=443
TOR_ENDPOINT_IPS = set([
    '103.10.197.50',
    '103.234.220.197',
    '103.236.201.110',
    '103.250.73.6',
    '103.27.124.82',
    '103.29.70.23',
    '103.3.61.114',
    '103.35.74.75',
    '103.35.74.77',
    '103.56.207.84',
    '103.73.64.73',
    '103.8.79.229',
    '104.132.1.96',
    '104.200.20.46',
    '104.218.63.73',
    '104.218.63.74',
    '104.218.63.75',
    '104.218.63.76',
    '104.223.123.98',
    '104.236.141.156',
    '104.237.203.98',
    '104.244.74.78',
    '106.187.37.101',
    '107.181.174.84',
    '107.191.56.192',
    '108.56.199.13',
    '108.85.99.10',
    '109.10.44.69',
    '109.126.9.228',
    '109.133.37.46',
    '109.169.33.163',
    '109.201.133.100',
    '109.62.156.57',
    '109.69.67.17',
    '110.174.43.136',
    '111.248.99.159',
    '115.70.208.19',
    '117.201.240.2',
    '117.247.87.18',
    '118.163.74.160',
    '120.29.217.46',
    '124.109.1.207',
    '125.212.241.182',
    '125.230.97.39',
    '126.227.148.185',
    '126.227.157.205',
    '126.227.167.62',
    '126.227.195.165',
    '126.227.213.99',
    '126.227.250.151',
    '126.74.215.3',
    '126.94.102.22',
    '126.99.239.26',
    '128.153.146.125',
    '128.199.47.160',
    '128.199.59.35',
    '128.52.128.105',
    '128.70.27.66',
    '130.204.161.3',
    '130.226.169.137',
    '130.25.61.252',
    '137.74.169.241',
    '138.197.207.243',
    '138.201.40.83',
    '139.162.10.72',
    '139.162.105.26',
    '139.162.144.133',
    '139.162.226.245',
    '139.162.28.23',
    '139.162.28.31',
    '139.59.250.10',
    '139.59.62.94',
    '14.202.230.49',
    '141.138.141.208',
    '141.170.2.53',
    '141.255.189.161',
    '142.4.211.161',
    '142.44.166.241',
    '144.217.161.119',
    '144.217.167.240',
    '144.217.60.211',
    '144.217.60.239',
    '144.217.94.195',
    '145.239.74.115',
    '145.239.74.47',
    '145.239.82.79',
    '146.0.74.13',
    '146.0.79.144',
    '146.0.79.243',
    '146.185.177.103',
    '147.92.96.163',
    '149.202.238.204',
    '149.202.58.41',
    '149.202.98.160',
    '149.202.98.161',
    '149.36.64.22',
    '149.56.135.190',
    '149.56.223.241',
    '151.80.38.67',
    '154.127.61.249',
    '155.133.82.112',
    '155.4.230.97',
    '158.255.5.206',
    '158.255.6.242',
    '158.69.215.7',
    '158.69.220.128',
    '162.213.0.243',
    '162.213.3.221',
    '162.220.246.230',
    '162.221.201.57',
    '162.243.136.6',
    '162.243.166.137',
    '162.243.75.204',
    '162.247.72.199',
    '162.247.72.200',
    '162.247.72.201',
    '162.247.72.202',
    '162.247.72.216',
    '162.247.72.217',
    '162.247.72.27',
    '162.247.72.7',
    '162.247.73.204',
    '162.247.73.206',
    '162.247.73.74',
    '163.172.101.137',
    '163.172.125.207',
    '163.172.133.181',
    '163.172.134.39',
    '163.172.136.101',
    '163.172.137.174',
    '163.172.137.222',
    '163.172.139.161',
    '163.172.140.123',
    '163.172.142.15',
    '163.172.151.250',
    '163.172.151.47',
    '163.172.153.12',
    '163.172.156.159',
    '163.172.160.182',
    '163.172.161.56',
    '163.172.162.106',
    '163.172.163.85',
    '163.172.169.38',
    '163.172.170.161',
    '163.172.179.129',
    '163.172.190.34',
    '163.172.212.115',
    '163.172.217.50',
    '163.172.223.200',
    '163.172.223.87',
    '163.172.67.180',
    '164.132.106.162',
    '164.132.51.91',
    '164.77.133.220',
    '165.255.108.30',
    '165.255.216.199',
    '165.90.188.168',
    '166.70.15.14',
    '166.70.207.2',
    '167.114.34.150',
    '170.250.140.52',
    '171.25.193.131',
    '171.25.193.132',
    '171.25.193.20',
    '171.25.193.235',
    '171.25.193.25',
    '171.25.193.77',
    '171.25.193.78',
    '172.111.177.204',
    '172.111.177.70',
    '173.14.173.227',
    '173.208.213.114',
    '173.254.216.66',
    '173.255.226.142',
    '173.255.229.8',
    '173.255.231.125',
    '176.10.104.240',
    '176.10.104.243',
    '176.10.107.180',
    '176.10.250.33',
    '176.10.99.200',
    '176.10.99.201',
    '176.10.99.202',
    '176.10.99.203',
    '176.10.99.204',
    '176.10.99.205',
    '176.10.99.206',
    '176.10.99.207',
    '176.10.99.208',
    '176.10.99.209',
    '176.123.30.230',
    '176.125.193.120',
    '176.125.195.245',
    '176.125.215.56',
    '176.126.252.11',
    '176.126.252.12',
    '176.194.108.45',
    '176.222.179.206',
    '176.31.180.157',
    '176.31.45.3',
    '176.36.117.185',
    '176.38.163.77',
    '176.58.100.98',
    '176.58.89.182',
    '177.205.16.251',
    '177.205.17.157',
    '177.205.30.99',
    '177.99.153.239',
    '178.140.99.168',
    '178.156.202.125',
    '178.17.170.13',
    '178.17.170.135',
    '178.17.170.156',
    '178.17.170.164',
    '178.17.170.194',
    '178.17.170.195',
    '178.17.170.196',
    '178.17.171.40',
    '178.17.171.43',
    '178.17.171.49',
    '178.17.174.10',
    '178.17.174.14',
    '178.17.174.32',
    '178.175.131.194',
    '178.175.138.99',
    '178.18.83.215',
    '178.20.55.16',
    '178.20.55.18',
    '178.202.169.177',
    '178.209.42.84',
    '178.238.237.44',
    '178.32.181.97',
    '178.32.181.99',
    '178.32.53.53',
    '178.32.53.94',
    '178.38.176.102',
    '178.6.82.37',
    '178.63.110.151',
    '178.63.97.34',
    '179.183.165.70',
    '179.4.119.18',
    '179.43.146.230',
    '18.248.1.85',
    '18.248.2.85',
    '184.105.220.24',
    '185.10.68.119',
    '185.10.68.132',
    '185.10.68.184',
    '185.10.68.191',
    '185.10.68.95',
    '185.100.84.108',
    '185.100.84.82',
    '185.100.85.101',
    '185.100.85.147',
    '185.100.85.190',
    '185.100.85.192',
    '185.100.85.61',
    '185.100.85.90',
    '185.100.86.100',
    '185.100.86.128',
    '185.100.86.141',
    '185.100.86.154',
    '185.100.86.167',
    '185.100.86.199',
    '185.100.86.217',
    '185.100.87.210',
    '185.100.87.82',
    '185.103.99.60',
    '185.104.120.2',
    '185.104.120.3',
    '185.104.120.4',
    '185.104.120.7',
    '185.107.81.233',
    '185.112.157.135',
    '185.113.128.234',
    '185.117.118.132',
    '185.117.118.234',
    '185.129.62.62',
    '185.130.104.198',
    '185.135.10.76',
    '185.140.53.251',
    '185.159.128.193',
    '185.159.131.99',
    '185.16.200.176',
    '185.165.168.186',
    '185.165.168.42',
    '185.165.168.77',
    '185.170.41.8',
    '185.170.42.18',
    '185.170.42.4',
    '185.175.208.179',
    '185.175.208.180',
    '185.189.14.230',
    '185.189.14.61',
    '185.29.8.132',
    '185.34.33.2',
    '185.38.14.171',
    '185.38.14.215',
    '185.48.33.144',
    '185.48.33.145',
    '185.48.34.75',
    '185.48.34.85',
    '185.50.191.250',
    '185.61.138.207',
    '185.61.149.193',
    '185.62.190.23',
    '185.65.205.10',
    '185.66.200.10',
    '185.70.10.238',
    '185.72.244.24',
    '185.73.44.54',
    '185.82.216.233',
    '185.87.185.45',
    '186.120.225.119',
    '186.206.211.251',
    '186.214.3.247',
    '186.214.6.194',
    '186.214.77.129',
    '186.214.79.119',
    '187.104.58.208',
    '188.116.11.181',
    '188.152.49.58',
    '188.209.52.9',
    '188.213.165.101',
    '188.214.129.85',
    '188.219.232.165',
    '188.65.144.2',
    '188.72.116.194',
    '188.72.116.196',
    '188.72.116.198',
    '189.84.21.44',
    '190.10.8.50',
    '190.104.217.195',
    '190.210.98.90',
    '190.216.2.136',
    '191.101.238.214',
    '191.250.248.63',
    '191.34.31.245',
    '191.96.249.110',
    '192.160.102.164',
    '192.160.102.165',
    '192.160.102.166',
    '192.160.102.168',
    '192.160.102.169',
    '192.160.102.170',
    '192.195.80.10',
    '192.34.80.176',
    '192.42.113.102',
    '192.42.116.16',
    '192.81.131.49',
    '192.87.28.28',
    '193.107.85.56',
    '193.107.85.62',
    '193.110.157.151',
    '193.15.16.4',
    '193.169.135.133',
    '193.169.135.154',
    '193.171.202.150',
    '193.201.225.45',
    '193.70.36.201',
    '193.70.39.41',
    '193.70.56.25',
    '193.70.89.19',
    '193.70.89.20',
    '193.70.95.180',
    '193.90.12.86',
    '193.90.12.87',
    '193.90.12.88',
    '193.90.12.89',
    '193.90.12.90',
    '194.218.3.79',
    '194.54.162.212',
    '195.123.212.118',
    '195.123.212.34',
    '195.219.163.68',
    '195.219.166.53',
    '195.228.45.176',
    '195.254.135.76',
    '196.54.55.14',
    '197.231.221.211',
    '198.167.223.38',
    '198.167.223.48',
    '198.167.223.50',
    '198.211.122.191',
    '198.233.204.165',
    '198.245.60.8',
    '198.46.138.18',
    '198.50.158.140',
    '198.50.159.155',
    '198.50.159.204',
    '198.50.200.129',
    '198.50.200.131',
    '198.50.200.134',
    '198.50.200.135',
    '198.50.200.147',
    '198.58.100.240',
    '198.58.107.53',
    '198.71.81.66',
    '198.73.50.71',
    '198.96.155.3',
    '199.127.226.150',
    '199.19.225.212',
    '199.249.223.40',
    '199.249.223.60',
    '199.249.223.61',
    '199.249.223.62',
    '199.249.223.63',
    '199.249.223.64',
    '199.249.223.66',
    '199.249.223.67',
    '199.249.223.68',
    '199.249.223.69',
    '199.249.223.71',
    '199.249.223.72',
    '199.249.223.73',
    '199.249.223.74',
    '199.249.223.75',
    '199.249.223.76',
    '199.249.223.77',
    '199.249.223.78',
    '199.249.223.79',
    '199.249.223.81',
    '199.68.196.124',
    '199.87.154.255',
    '2.38.165.72',
    '201.68.215.52',
    '204.11.50.131',
    '204.145.94.126',
    '204.17.56.42',
    '204.194.29.4',
    '204.8.156.142',
    '204.85.191.30',
    '204.85.191.31',
    '205.166.94.153',
    '205.168.84.133',
    '206.248.184.127',
    '208.67.1.79',
    '208.67.1.82',
    '208.67.1.83',
    '209.123.234.23',
    '209.133.66.214',
    '209.249.157.69',
    '209.249.180.198',
    '209.66.119.150',
    '210.10.166.159',
    '210.3.102.152',
    '210.50.9.88',
    '211.21.48.217',
    '212.159.91.21',
    '212.16.104.33',
    '212.19.17.213',
    '212.21.66.6',
    '212.47.227.114',
    '212.47.229.60',
    '212.47.243.140',
    '212.47.246.21',
    '212.81.199.159',
    '212.83.40.239',
    '212.92.219.15',
    '213.108.105.71',
    '213.108.105.92',
    '213.61.149.100',
    '213.95.21.54',
    '216.158.234.3',
    '216.218.134.12',
    '216.218.222.11',
    '216.218.222.12',
    '216.239.90.19',
    '217.115.10.131',
    '217.182.207.27',
    '217.182.74.253',
    '217.182.76.240',
    '217.182.78.177',
    '217.23.13.129',
    '222.110.3.1',
    '223.26.48.248',
    '23.92.27.23',
    '23.92.28.23',
    '24.207.212.154',
    '24.214.133.150',
    '31.185.104.19',
    '31.185.104.20',
    '31.185.104.21',
    '31.185.27.208',
    '31.40.42.31',
    '35.184.106.64',
    '36.229.29.171',
    '36.229.81.163',
    '37.139.8.104',
    '37.157.196.97',
    '37.187.117.138',
    '37.187.129.166',
    '37.187.53.94',
    '37.187.7.74',
    '37.187.96.78',
    '37.218.240.21',
    '37.218.240.50',
    '37.218.240.68',
    '37.218.240.80',
    '37.220.35.202',
    '37.220.36.240',
    '37.48.120.196',
    '37.59.112.7',
    '37.97.228.159',
    '37.99.72.122',
    '4.31.64.70',
    '41.100.129.156',
    '41.100.130.227',
    '41.100.133.103',
    '41.100.140.7',
    '41.100.60.224',
    '41.206.188.206',
    '45.33.23.23',
    '45.33.48.204',
    '45.35.72.85',
    '45.62.213.11',
    '45.62.232.20',
    '45.62.236.66',
    '45.62.239.42',
    '45.62.251.20',
    '45.62.254.224',
    '45.79.137.11',
    '45.79.144.222',
    '45.79.207.176',
    '45.79.73.22',
    '45.79.85.112',
    '46.101.127.145',
    '46.101.139.248',
    '46.101.150.49',
    '46.101.237.184',
    '46.127.20.181',
    '46.148.132.169',
    '46.148.138.76',
    '46.165.223.217',
    '46.165.230.5',
    '46.166.162.53',
    '46.17.97.112',
    '46.182.106.190',
    '46.182.18.111',
    '46.182.18.214',
    '46.182.18.29',
    '46.182.18.40',
    '46.182.18.46',
    '46.182.19.15',
    '46.182.19.219',
    '46.183.218.199',
    '46.183.221.231',
    '46.194.37.230',
    '46.194.48.196',
    '46.233.0.70',
    '46.235.227.70',
    '46.246.35.34',
    '46.246.35.49',
    '46.246.35.62',
    '46.246.35.63',
    '46.246.35.90',
    '46.246.37.165',
    '46.246.49.138',
    '46.246.49.158',
    '46.246.49.165',
    '46.246.49.173',
    '46.246.49.196',
    '46.246.63.103',
    '46.29.248.238',
    '46.34.203.227',
    '46.39.102.250',
    '46.45.137.71',
    '46.5.76.233',
    '46.72.112.10',
    '46.72.115.12',
    '46.72.66.175',
    '46.72.68.78',
    '46.72.94.207',
    '46.72.95.168',
    '5.187.21.45',
    '5.189.146.133',
    '5.189.188.111',
    '5.196.1.129',
    '5.196.121.161',
    '5.196.66.162',
    '5.199.130.188',
    '5.254.112.154',
    '5.254.79.66',
    '5.28.62.85',
    '5.3.167.55',
    '5.34.59.1',
    '5.39.217.14',
    '5.61.34.63',
    '5.79.68.161',
    '5.9.158.75',
    '5.9.195.140',
    '50.115.164.113',
    '50.247.195.124',
    '50.76.159.218',
    '51.15.10.158',
    '51.15.134.120',
    '51.15.141.220',
    '51.15.34.210',
    '51.15.34.214',
    '51.15.37.97',
    '51.15.39.2',
    '51.15.40.233',
    '51.15.43.205',
    '51.15.45.131',
    '51.15.52.230',
    '51.15.53.118',
    '51.15.53.83',
    '51.15.54.136',
    '51.15.56.11',
    '51.15.62.146',
    '51.15.63.148',
    '51.15.63.229',
    '51.15.63.98',
    '51.15.64.212',
    '51.15.70.13',
    '51.15.70.226',
    '51.15.70.228',
    '51.15.73.164',
    '51.15.76.81',
    '51.15.76.86',
    '51.15.79.107',
    '51.15.8.198',
    '51.254.23.203',
    '51.255.196.218',
    '51.255.202.66',
    '52.169.74.227',
    '59.127.163.155',
    '60.248.162.179',
    '61.228.238.211',
    '61.228.92.98',
    '61.228.93.169',
    '61.230.114.76',
    '61.230.162.223',
    '62.102.148.67',
    '62.12.115.107',
    '62.141.39.47',
    '62.176.4.10',
    '62.210.105.116',
    '62.210.115.87',
    '62.210.123.10',
    '62.210.129.246',
    '62.210.37.82',
    '62.210.83.149',
    '62.212.73.141',
    '62.75.168.144',
    '64.113.32.29',
    '64.124.32.84',
    '64.137.162.142',
    '64.137.244.19',
    '64.27.17.140',
    '65.181.113.61',
    '65.181.123.254',
    '65.19.167.130',
    '65.19.167.131',
    '65.19.167.132',
    '66.155.4.213',
    '66.180.193.219',
    '66.220.3.179',
    '66.70.217.179',
    '67.1.236.9',
    '67.205.146.164',
    '67.215.255.140',
    '67.248.218.132',
    '68.147.220.49',
    '69.162.107.5',
    '69.162.123.166',
    '69.162.139.9',
    '69.164.207.234',
    '70.164.255.174',
    '71.46.220.68',
    '72.12.207.14',
    '72.14.179.10',
    '72.52.75.27',
    '73.189.24.253',
    '74.50.54.69',
    '75.54.229.204',
    '75.82.218.249',
    '77.109.139.87',
    '77.247.181.163',
    '77.247.181.165',
    '77.250.227.12',
    '77.81.107.138',
    '77.81.247.72',
    '78.107.237.16',
    '78.109.23.1',
    '78.109.24.135',
    '78.129.137.28',
    '78.142.19.166',
    '78.142.19.42',
    '78.156.250.2',
    '78.24.221.230',
    '78.31.164.41',
    '78.41.115.145',
    '78.63.161.0',
    '78.70.167.74',
    '78.94.31.174',
    '79.124.59.202',
    '79.134.234.247',
    '79.134.255.200',
    '79.137.67.116',
    '79.137.79.167',
    '79.137.80.94',
    '79.237.147.38',
    '80.169.241.76',
    '80.241.60.207',
    '80.244.81.191',
    '80.248.208.131',
    '80.67.172.162',
    '80.73.242.142',
    '80.79.23.7',
    '80.82.67.166',
    '80.82.67.186',
    '80.85.84.23',
    '82.211.19.143',
    '82.221.101.67',
    '82.221.112.122',
    '82.221.128.217',
    '82.221.139.190',
    '82.221.139.25',
    '82.223.27.82',
    '82.247.198.227',
    '82.248.29.136',
    '82.248.40.229',
    '82.249.156.221',
    '82.249.173.65',
    '82.249.191.53',
    '82.249.196.128',
    '82.249.74.122',
    '82.250.115.18',
    '82.250.127.48',
    '82.250.45.198',
    '82.250.66.203',
    '83.220.174.128',
    '83.226.165.147',
    '83.92.47.99',
    '84.105.18.164',
    '84.128.241.21',
    '84.128.255.118',
    '84.19.176.100',
    '84.19.180.135',
    '84.19.181.25',
    '84.190.178.119',
    '84.190.178.227',
    '84.200.50.18',
    '84.200.82.163',
    '84.209.48.106',
    '84.217.13.138',
    '84.3.0.53',
    '84.48.199.78',
    '84.53.225.118',
    '85.119.83.78',
    '85.143.219.211',
    '85.143.95.50',
    '85.195.107.250',
    '85.229.199.23',
    '85.248.227.163',
    '85.248.227.164',
    '85.248.227.165',
    '85.25.103.69',
    '85.25.222.176',
    '85.29.170.24',
    '85.5.15.11',
    '85.90.244.23',
    '86.59.170.188',
    '86.7.140.31',
    '87.118.111.158',
    '87.118.115.176',
    '87.118.116.12',
    '87.118.116.90',
    '87.118.122.254',
    '87.118.122.30',
    '87.118.122.50',
    '87.118.122.51',
    '87.118.82.3',
    '87.118.92.43',
    '87.118.94.2',
    '87.120.254.130',
    '87.120.37.107',
    '87.180.224.50',
    '87.180.239.120',
    '87.248.32.130',
    '87.248.32.32',
    '87.248.32.92',
    '87.81.148.61',
    '88.156.182.196',
    '88.159.9.134',
    '88.198.125.96',
    '88.76.17.146',
    '88.77.132.201',
    '88.77.218.28',
    '88.83.40.246',
    '88.99.23.92',
    '89.144.12.15',
    '89.187.144.122',
    '89.187.150.12',
    '89.223.27.241',
    '89.234.157.254',
    '89.236.34.117',
    '89.248.166.157',
    '89.31.57.5',
    '89.31.96.168',
    '89.32.127.178',
    '89.34.237.101',
    '89.34.237.121',
    '89.38.208.57',
    '89.45.226.28',
    '89.94.1.179',
    '90.3.108.73',
    '90.3.110.242',
    '91.116.229.6',
    '91.134.232.48',
    '91.134.232.58',
    '91.138.21.159',
    '91.138.41.48',
    '91.146.121.3',
    '91.197.234.102',
    '91.219.236.218',
    '91.219.236.232',
    '91.219.237.229',
    '91.219.237.244',
    '91.221.57.129',
    '91.223.82.156',
    '91.233.106.121',
    '91.233.106.172',
    '91.247.109.51',
    '91.250.241.241',
    '91.59.68.25',
    '91.59.82.77',
    '91.92.109.11',
    '92.111.156.14',
    '92.222.103.232',
    '92.222.134.129',
    '92.222.180.87',
    '92.222.38.67',
    '92.222.6.12',
    '92.222.74.226',
    '92.63.173.28',
    '93.115.95.201',
    '93.115.95.202',
    '93.115.95.204',
    '93.115.95.205',
    '93.115.95.206',
    '93.115.95.207',
    '93.115.95.216',
    '93.170.77.90',
    '93.174.90.30',
    '93.174.93.133',
    '93.201.163.220',
    '93.201.185.127',
    '93.64.207.55',
    '93.65.218.42',
    '94.102.50.42',
    '94.140.120.139',
    '94.141.227.12',
    '94.142.242.84',
    '94.198.100.17',
    '94.23.172.135',
    '94.23.201.80',
    '94.23.239.44',
    '94.242.246.23',
    '94.242.246.24',
    '94.242.57.161',
    '94.242.59.163',
    '94.34.60.147',
    '94.34.76.205',
    '94.34.83.158',
    '95.128.43.164',
    '95.129.164.103',
    '95.130.10.69',
    '95.130.11.147',
    '95.130.11.170',
    '95.142.161.63',
    '95.165.133.22',
    '95.211.118.194',
    '95.211.230.94',
    '95.30.152.201',
    '95.46.131.236',
    '95.71.51.33',
    '95.79.126.237',
    '96.43.142.139',
    '96.64.149.101',
    '96.68.60.77',
    '97.74.237.196',
])

BANNED_IPS = TOR_ENDPOINT_IPS | set([
    '81.234.236.23', '81.230.148.230',  # .se
    '86.143.83.97'  # .uk
])


def is_ip_banned(request):
    return (request.META['REMOTE_ADDR'] in BANNED_IPS)
