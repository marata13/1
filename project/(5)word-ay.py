x=input('insert a text file name:')
kwstas = open(x, 'r').read()
kwstas=list(kwstas) #metatroph se list me skopo na prosepelasw kai na tropopoihsw to periexomeno
flag=False #elegxei an to teleftaio block tou keimenou teleiwnei me keno
if kwstas[-1]!=" ":
    kwstas+=" "
    flag=True  #to teleftaio block den einai keno gia auto to bazoume emeis etsi wste o algori8mos na katalabaianei
                #oti h lexi exei teleiwsei
k=0 #mas deixnei poses fores brhke synecomena grammata
for x in range(len(kwstas)):
    if kwstas[x]==" " and k>3:
        None
    elif kwstas[x]==" ":
        k=0
        continue;
    else:
        if k==0:
            prwto=x #to prwto gramma ths lexis
        teleftaio=x #to teleftaio gramma ths lexis
        k+=1
    if k>=3 and kwstas[x]==" ":
            kwstas[teleftaio]=kwstas[teleftaio]+kwstas[prwto]+"ay"
            kwstas[prwto]="boom" #sto prwto gramma ths lexis bazw th lexi boom etsi wste na bgalw o,ti "boom" sto telos
            k=0 #arxio8etoume me 0 to synolo twn synexomenwn grammatwn afou
                #exoume brei mia lexi
if flag==True:
    kwstas[-1]="boom"
kwstas=[x for x in kwstas if x != "boom"]
meta=kwstas[0]
for j in range(1,len(kwstas)):
    meta+=kwstas[j] #to meta einai metablhth pou xrhsimopoieitai etsi wste na pros8esei ola periexomena ths listas
                    #kai na ta ksanakanei string
kwstas=meta
print(kwstas)
