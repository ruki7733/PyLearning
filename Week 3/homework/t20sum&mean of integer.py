n=int(input())
total=0
for i in range(n): #y有n组数据
    total+=int(input())
mean=int(total)/n
print(total,'%.5f'%(mean),end='')