# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# This signature was contributed by RedSocks - http://redsocks.nl
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class BegseabugTDMutexes(Signature):
    name = "begseabugtd_mutexes"
    description = "Creates known Begseabug Trojan Downloader mutexes"
    severity = 3
    categories = ["trojandl"]
    families = ["begseabug"]
    authors = ["RedSocks"]
    minimum = "2.0"

    mutexes_re = [
        ".*SeBebugPrivilege",
    ]

    def on_complete(self):
        for indicator in self.mutexes_re:
            mutex = self.check_mutex(pattern=indicator, regex=True)
            if mutex:
                self.mark_ioc("mutex", mutex)

        return self.has_marks()
