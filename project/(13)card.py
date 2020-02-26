karta=str(input('put your card number:'))
flag=False #to length ths pistwtikhs den einai 16
if len(karta)==16:
    flag=True #to length ths pistwtikhs einai 16
while flag==False:
    karta=str(input('your card number must be 16 digits long:'))
    if len(karta)==16:
        flag=True
karta=[int(x) for x in (karta)]
for i in range(14,-1,-2):
    karta[i]=karta[i]*2
    athroisma=(karta[i]//10)+(karta[i]%10)
    while athroisma>9:
        athroisma=(athroisma//10)+(athroisma%10)
    karta[i]=athroisma
sum=0
for x in karta:
    sum+=x
if sum%10==0:
    print('the card number is accurate')
else:
    print('the card number is incorrect')
            
            


