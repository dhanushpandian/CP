class Solution:
    def reformatDate(self, date: str) -> str:
        s = date.split() 
        monthDict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        day = s[0][:-2] # Removes the last 2 elements of the day
        month = s[1] 
        year = s[2]
        if int(day) < 10: # Adds 0 to the front of day if day < 10
            day = '0' + day
        return ''.join(f'{year}-{monthDict[month]}-{day}') # Joins it all together. Month is used to draw out the corresponding number from the dict.

class Solution:
    def reformatDate(self, date: str) -> str:
        months={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        a=date.split(" ")
        ans=a[::-1]
        ans[1]=months[ans[1]]
        ans[2]=ans[2][-3::-1]
        ans[2]=ans[2][::-1]
        if len(ans[2]) < 2 :
            ans[2]="0"+ans[2]
        res=ans[0]
        for i in ans[1:]:
            res+="-"
            res+=i
        return res