#!/user/bin/env python3
# -*- coding: utf-8 -*-

# Author : Martin
# Date&Time : 2020-12-04 17:38
# Description :

import re

def name_of_email(addr):

    r_name = re.compile(r'^<?(\w*\s*\w*)>?(\s*\w*)(@\w*\.\w*)$')
    return r_name.match(addr).group(1)

#    m = re.match(r'^<?(\w*\s*\w*)>?(\s*\w*)(@\w*\.\w*)$', addr)
#    return m.group(1)

#    m = re.match(r'^<?(\w+\s?\w+)?>?(\s?\w+)?\@(\w+\.\w+)$', addr)
#    return m.group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')