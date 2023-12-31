# Copyright (C) 2016 Brad Spengler
# Copyright (C) 2017-2018 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class AntiSandboxRestart(Signature):
    name = "antisandbox_restart"
    description = "Attempts to shutdown or restart the system, generally used for bypassing sandboxing"
    severity = 3
    categories = ["anti-sandbox"]
    authors = ["Cuckoo Technologies", "Brad Spengler"]
    minimum = "2.0"

    filter_apinames = (
        "InitiateSystemShutdownExW", "InitiateSystemShutdownExA",
        "NtShutdownSystem", "NtSetSystemPowerState", "ExitWindowsEx",
        "InitiateShutdownW", "InitiateSystemShutdownW", "NtRaiseHardError",
    )

    def on_call(self, call, process):
        self.mark_call()

    def on_complete(self):
        return self.has_marks()
