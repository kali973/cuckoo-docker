# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# This signature was contributed by RedSocks - http://redsocks.nl
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class miningpool(Signature):
    name = "miningpool"
    description = "Connects to Mining Pool to Generate Virtual Currency"
    severity = 2
    categories = ["mining"]
    authors = ["RedSocks"]
    minimum = "2.0"

    ipaddrs = [
        "144.76.102.176",
        "5.9.38.45",
        "80.241.1.7",
        "50.45.128.27",
        "54.195.36.180",
        "54.225.68.97",
        "54.72.148.56",
        "206.71.179.116",
        "162.13.142.151",
        "198.245.63.145",
        "88.214.194.226",
        "217.115.11.163",
        "50.112.124.28",
        "198.144.121.73",
        "199.83.50.51",
        "69.197.61.58",
        "144.76.176.12",
        "162.211.64.165",
        "8.35.198.175",
        "31.186.87.46",
        "78.24.223.85",
        "88.198.25.9",
        "66.207.163.134",
        "66.207.163.137",
        "178.33.111.19",
        "192.81.220.10",
        "54.245.105.184",
        "198.245.52.25",
        "81.209.165.238",
        "94.23.15.100",
        "76.74.178.203",
        "37.59.24.15",
        "37.187.92.211",
        "66.211.159.2",
        "97.104.170.35",
        "54.83.41.150",
        "198.27.70.101",
        "69.80.120.35",
        "37.187.52.219",
        "128.65.210.241",
        "192.99.241.167",
        "54.221.194.44",
        "173.14.171.57",
        "83.125.22.197",
        "176.31.185.239",
        "198.50.144.242",
        "188.165.84.230",
        "78.46.22.103",
        "59.127.188.231",
        "80.69.77.111",
        "151.236.218.211",
        "107.170.24.54",
        "142.4.202.112",
        "192.241.197.116",
        "198.251.80.29",
        "162.212.255.218",
        "209.141.38.200",
        "142.4.216.82",
        "144.76.176.163",
        "78.24.218.150",
        "92.222.18.43",
        "146.185.137.249",
        "88.198.25.105",
        "91.121.174.223"
    ]

    def on_complete(self):
        for indicator in self.ipaddrs:
            if self.check_ip(pattern=indicator):
                self.mark_ioc("ipaddr", indicator)

        return self.has_marks()
