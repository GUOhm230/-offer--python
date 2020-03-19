# -*- coding: utf-8 -*-
#！usr/bin/env python
def getFirst(s):
    for i in range(len(s)):
        if i <= len(s)-2:
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    return s[i]
    if s[i] != s[j]:
        return 5

print(getFirst('qwerfaa'))