# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# This signature was contributed by RedSocks - http://redsocks.nl
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class IcePoint(Signature):
    name = "icepoint"
    description = "Creates known IcePoint RAT files, registry keys and/or mutexes"
    severity = 3
    categories = ["rat"]
    families = ["icepoint"]
    authors = ["RedSocks"]
    minimum = "2.0"

    files_re = [
        ".*IcePoint"
    ]

    def on_complete(self):
        for indicator in self.files_re:
            match = self.check_file(pattern=indicator, regex=True)
            if match:
                self.mark_ioc("file", match)

        return self.has_marks()
