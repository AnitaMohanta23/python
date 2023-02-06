#REVERSE A NUMBER
# n=int(input())

# _sum=0

# while n>0:
#     rem=n%10
#     _sum=_sum*10 + rem
#     n=int(n/10)

# print(_sum)


#CHECK N IS PALINDROME
n=int(input())
temp=n
_sum=0

while n>0:
    rem=n%10
    _sum=_sum*10 + rem
    n=int(n/10)

if n ==_sum: #not palindrom
    print(f"{_sum} is palondrom")
else:
    print(f"{_sum} is not palindrom")

##for  palidron
n=int(input())
temp=n
_sum=0

while n>0:
    rem=n%10
    _sum=_sum*10 + rem
    n=int(n/10)

if temp ==_sum:  #is palindrom
    print(f"{_sum} is palondrom")
else:
    print(f"{_sum} is not palindrom")
