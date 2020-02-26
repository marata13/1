x=input('insert a text file name:')
s = open(x, 'r').read()
s=list(s) 
if s[-1]!=" ":
    s+=" "
mesa=0 #an einai 0 den exei ksanabei an einai 1 exei ksanabei sth lexi
k=0 #an einai 0 shmainei oti to block einai keno enw an einai 1 den einai
for i in range(len(s)):
    if k==1 and s[i]==" ":
        metr=0 #blepei an yparxoun ola ta apagoreymena grammata sth lexi
        if "f" in lexi:
            metr+=1
            if "c" in lexi:
                metr+=1
                if "k" in lexi:
                    metr+=1
                    if "r" in lexi:
                        metr+=1
        if plh8os>len(lexi)/2:
            print("h lexi "+str(lexi)+" kakh")
        else:
            print("h lexi "+str(lexi)+" kalh")
    if s[i]==" ":
        k=0
        mesa=0
    else:
        k=1
        if mesa==0:
            lexi=s[i]
            mesa=1
            plh8os=0 #ypologizei to plh8os twn apagoreumenwn grammatwn
        else:
            lexi+=s[i]
        if s[i]=="f" or s[i]=="c" or s[i]=="k" or s[i]=="r":
                plh8os+=1
