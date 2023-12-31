# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# This signature was contributed by RedSocks - http://redsocks.nl
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class BuzusMutexes(Signature):
    name = "rat_buzus_mutexes"
    description = "Creates known Buzus files, registry keys and/or mutexes"
    severity = 3
    categories = ["rat"]
    families = ["buzus"]
    authors = ["RedSocks"]
    minimum = "2.0"

    mutexes_re = [
        ".*SnowDownVip2009v2",
        ".*SnowDownVip2009v2-Down",
        ".*SnowDownVip2010",
        ".*SnowDownVip2010-Down",
        ".*ImXD",
        ".*IamBugXD",
        ".*Cerberus"
    ]

    regkeys_re = [
        ".*SOFTWARE.*Cerberus",
    ]

    def on_complete(self):
        for indicator in self.mutexes_re:
            match = self.check_mutex(pattern=indicator, regex=True)
            if match:
                self.mark_ioc("mutex", match)

        for indicator in self.regkeys_re:
            match = self.check_key(pattern=indicator, regex=True)
            if match:
                self.mark_ioc("regkey", match)

        return self.has_marks()
