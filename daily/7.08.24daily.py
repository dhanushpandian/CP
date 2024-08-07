class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"
        }

        def conv(n):
            ans=[]
            h=n//100
            if h:
                ans.append(d[h]+" Hundred")
            t=n%100
            if t >=20:
                tens=t//10
                units=t%10
                ans.append(d[tens*10])
                if units:
                    ans.append(d[units])
            elif t:
                ans.append(d[t])
            return " ".join(ans) 
        
        l=[""," Thousand"," Million"," Billion"]
        i=0
        ans=[]
        while num:
            digits=num % 1000
            s=conv(digits)
            if s:
                ans.append(s+l[i])
            num=num // 1000
            i+=1
        ans=ans[::-1]
        return " ".join(ans)