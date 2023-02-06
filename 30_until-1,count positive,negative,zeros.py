num=(input('Enter a Number(if u want to exit plz enter-)'))
np=0
nn=0
nz=0
while num!=-1:
    if num>0:
        np=np+1
    elif num<0:
        nn=nn+1
else:
   nz=nz+1

num=(input('Enter a Number(if u want to exit plz enter-)'))
print('Number of positives',np)
print('Number of negetives',nn)
print('Number of zeros',nz)


