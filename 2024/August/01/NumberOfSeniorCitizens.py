#!/usr/bin/env python3

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for detail in details:
            age = int(detail[11:13])
            res += age>60
        return res
