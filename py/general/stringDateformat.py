
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