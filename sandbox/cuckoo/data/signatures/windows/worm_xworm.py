# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# This signature was contributed by RedSocks - http://redsocks.nl
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class Xworm(Signature):
    name = "worm_xworm"
    description = "Creates known X-Worm Backdoor files, registry keys and/or mutexes"
    severity = 3
    categories = ["worm"]
    families = ["xworm"]
    authors = ["RedSocks"]
    minimum = "2.0"

    mutexes_re = [
        ".*X-worm"
    ]

    def on_complete(self):
        for indicator in self.mutexes_re:
            mutex = self.check_mutex(pattern=indicator, regex=True)
            if mutex:
                self.mark_ioc("mutex", mutex)

        return self.has_marks()
