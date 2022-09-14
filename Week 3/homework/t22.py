n=int(input()) #n代表参加了n天
TotalGold=TotalSilver=TotalBronze=0
for i in range(n):
    s=input().split() #s代表奖牌列表
    Gold,Silver,Bronze=int(s[0]),int(s[1]),int(s[2]) #Gold为金牌，Silver为银牌，Bronze为铜牌
    TotalGold+=Gold
    TotalSilver+=Silver
    TotalBronze+=Bronze
    Total=TotalGold+TotalSilver+TotalBronze
print(TotalGold,TotalSilver,TotalBronze,Total,end='')
