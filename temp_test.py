#!/usr/bin/env python

import re
emphasis_pattern=r'\*([^\*]+)\*'
print re.sub(emphasis_pattern,r'<em>\1</em>','hello,*python*')