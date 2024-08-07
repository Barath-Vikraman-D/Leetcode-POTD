#! /usr/bin/env python3

class Solution:
    def numberToWords(self, num: int) -> str:
        result = ""
        if num == 0 : return "Zero"
        ones = ("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen")
        tens = ("","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety")
        groups = ["","Thousand","Million","Billion"]
        index = 0
        while(num>0):
            if(num%1000 != 0):
                grpres = ""
                part = num%1000
                if part>=100:
                    grpres += ones[part//100] + " Hundred "
                    part %= 100
                if part>=20:
                    grpres += tens[part//10] +" "
                    part %= 10
                if part>0:
                    grpres += ones[part] + " "
                result = grpres + groups[index] + " " + result
            num //=1000
            index += 1
        return result.strip()
