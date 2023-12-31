# Copyright (C) Check Point Software Technologies LTD.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature


class AndroidAbortBroadcast(Signature):
    name = "application_aborted_broadcast_receiver"
    description = "Application Aborted Broadcast Receiver (Dynamic)"
    severity = 2
    categories = ["android"]
    authors = ["Check Point Software Technologies LTD"]
    minimum = "2.0"

    def on_complete(self):
        if "abortBroadcast" in self.get_droidmon("events", []):
            return True
