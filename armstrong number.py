# n=int(input())
# temp=n
# temp_size=n
# length=0
# _sum=0

# while temp_size>0:
#     temp_size= int(temp_size/10)
#     length+=1
# print(length)

# while n>0:
#     rem=n%10
#     _sum+=(rem*rem*rem)
#     n=int(n/10)

# if temp ==_sum:  #is palindrom
#     print(f"{temp} is armstrong")
# else:
#     print(f"{_sum} is not armstrong")






n=int(input())
temp=n
temp_size=n
length=0
_sum=0
#IS TO FIND LENGTH OF N
while temp_size>0:
    temp_size= int(temp_size/10)
    length+=1
# print(length)

#TO FIND SUM
while n>0:
    rem=n%10
    _sum+=(rem**length)
    n=int(n/10)
#TO COMPARE
if temp ==_sum:  #is palindrom
    print(f"{temp} is armstrong")
else:
    print(f"{_sum} is not armstrong")