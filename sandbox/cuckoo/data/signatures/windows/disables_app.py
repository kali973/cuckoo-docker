# Copyright (C) 2015 Kevin Ross, Updated 2016 For Cuckoo 2.0
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class DisablesAppLaunch(Signature):
    name = "disables_app_launch"
    description = "Modifies system policies to prevent the launching of specific applications or executables"
    severity = 3
    categories = ["stealth"]
    authors = ["Kevin Ross"]
    minimum = "2.0"
    ttp = ["T1112"]

    regkeys_re = [
        ".*\\\\SOFTWARE\\\\(Wow6432Node\\\\)?Microsoft\\\\Windows\\\\CurrentVersion\\\\Policies\\\\Explorer\\\\DisallowRun$",
    ]

    def on_complete(self):
        for indicator in self.regkeys_re:
            for regkey in self.check_key(pattern=indicator, regex=True, actions=["regkey_written"], all=True):
                self.mark_ioc("registry", regkey)

        return self.has_marks()
