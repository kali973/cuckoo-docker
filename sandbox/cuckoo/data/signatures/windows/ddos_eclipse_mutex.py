# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# This signature was contributed by RedSocks - http://redsocks.nl
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class EclipseMutexes(Signature):
    name = "ddos_eclipse_mutexes"
    description = "Creates known Eclipse DDoS Bot mutexes"
    severity = 3
    categories = ["ddos"]
    families = ["eclipse"]
    authors = ["RedSocks"]
    minimum = "2.0"

    mutexes_re = [
        ".*eclipseddos",
    ]

    def on_complete(self):
        for indicator in self.mutexes_re:
            if self.check_mutex(pattern=indicator, regex=True):
                return True
