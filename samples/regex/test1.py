#!/user/bin/env python3
# -*- coding: utf-8 -*-

# Author : Martin
# Date&Time : 2020-12-04 17:18
# Description :

import re

def is_valid_email(addr):
    r_email = re.compile(r'^[a-z0-9A-Z\_\.]+\@[a-z0-9A-Z]+\.com$')
    if r_email.match(addr):
        return True

assert is_valid_email('someone@gmail.com')
assert not is_valid_email('bill.gates@microsoft.kom')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')