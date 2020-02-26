from datetime import datetime
currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
wantDate=input("dwse hmeromhnia:")
wantDate=list(wantDate)
mera=wantDate[0]+wantDate[1]
mhnas=wantDate[3]+wantDate[4]
xronia=wantDate[6]+wantDate[7]+wantDate[8]+wantDate[9]
mera,mhnas,xronia=int(mera),int(mhnas),int(xronia)
#starting #mhnas pou 8a ksekinhsei pou 8a bei sto loop IF cuurentMonth>mhnas:
#ending #mhnas pou 8a teleiwsei to loop
def dayz(metr,xronia,new=0):
    if new<0:
        meres=-new
        return meres
    if metr<=6:
        if metr==2:
            if xronia%4==0:
                meres=abs(29-new)
            else:
                meres=abs(28-new)
        else:
            if metr%2==1:
                meres=abs(31-new)
            else:
                meres=abs(30-new)
    else:
        if metr==7 or metr==8:
            meres=abs(31-new)
        else:
            if metr%2==0:
                meres=abs(31-new)
            else:
                meres=abs(30-new)
    return meres
mhniatiko=dayz(mhnas,xronia)
print("o dwsmenos mhnas exei "+str(mhniatiko)+" meres")
diafora=abs(xronia-currentYear)
year=currentYear
if currentYear>xronia:
    year=xronia
    if currentMonth<mhnas:
        starting = mhnas
        ending = currentMonth
        ksekinhma =mera
        teleiwma=currentDay
    elif currentMonth>mhnas:
        starting=mhnas
        ending=currentMonth
        ksekinhma=mera
        teleiwma=currentDay
    else: #currentMonth==mhnas:
        starting = currentMonth
        ending = starting
        ksekinhma=mera
        teleiwma=currentDay
elif currentYear<xronia:
    if currentMonth<mhnas:
        starting = currentMonth
        ending = mhnas
        ksekinhma =currentDay
        teleiwma=mera
    elif currentMonth>mhnas:
        starting=currentMonth
        ending=mhnas
        ksekinhma=currentDay
        teleiwma=mera
    else: #currentMonth==mhnas:
        starting = currentMonth
        ending = mhnas
        ksekinhma= currentDay
        teleiwma= mera
else:
    if currentMonth<mhnas:
        starting=currentMonth
        ending=mhnas
        ksekinhma=currentDay
        teleiwma=mera
    elif currentMonth<mhnas:
        starting=mhnas
        ending=currentMonth
        ksekinhma=mera
        teleiwa=currentDay
    else:#currentMonth=mhnas:
        starting=currentMonth
        ending=starting
        if currentDay>mera:
            ksekinhma=mera
            teleiwma=currentDay
        else: #currentDay<=mera:
            ksekinhma=currentDay
            teleiwma=mera
k=[] #mhnes diaforas trexousas hmeromhnias me th dosmenh
from library import dayz
for i in range(diafora+1):
    if i==0 and i!=diafora:
        for j in range(starting,13):
            if j==starting:
                k+=[dayz(j,year,ksekinhma)]
            else:
                k+=[dayz(j,year)]
    if i>0 and i!=(diafora):
        for z in range(1,13):
            k+=[dayz(z,year)]
    elif i>=0 and i==(diafora):
        if currentYear==xronia:
            if currentMonth==mhnas:
                meres=teleiwma-ksekinhma
                k+=[meres]
            else:
                for x in range(starting,ending+1):
                    if x==starting:
                        k+=[dayz(x,year,ksekinhma)]
                    elif x==ending:
                        k+=[dayz(x,year,-teleiwma)]
                    else:
                        k+=[dayz(x,year)]
        else:
            if i==0:
                for x in range(starting,13):
                    k+=[dayz(x,year,ksekinhma)]
            else:
                for x in range(1,ending+1):
                    if x==ending:
                        k+=[dayz(x,year,-teleiwma)]
                    else:
                        k+=[dayz(x,year)]
    year+=1
lexi="mhnes"
if k==1:
    lexi="mhna"
telikaXronia=0
telikoiMhnes=0
telikesMeres=0
if diafora==0:
    if len(k)>=3:
        for i in range(1,len(k)-1):
            telikoiMhnes+=1
        telikesMeres=k[0]+k[-1]
    else:
        telikesMeres+=k[0]+k[-1]
    while telikesMeres>=30:
        telikesMeres-=30
        telikoiMhnes+=1
else:
    if len(k)>=3:
        for i in range(1,len(k)-1):
            telikoiMhnes+=1
            if telikoiMhnes==12:
                telikoiMhnes=0
                telikaXronia+=1
            telikesMeres = k[0] + k[-1]
        else:
            telikesMeres += k[0] + k[-1]
if len(k)==1:
    telikesMeres=k[0]
while telikesMeres>=30:
    telikesMeres-=30
    telikoiMhnes+=1
    if telikoiMhnes==12:
        telikoiMhnes=0
        telikaXronia+=1
if telikesMeres-1>=0:
    telikesMeres-=1
flag=False #h hmeromhnia den einai idia me th dosmenh
if currentYear==xronia:
    if currentMonth==mhnas:
        if currentDay==mera:
            flag=True #h hmeromhnia einai idia me th twrinh ara to teleftaio print de 8a ektelestei
            print("oi hmeromhnies apexoun "+str(telikaXronia) + " xronia," + str(telikoiMhnes) + " mhnes," + str(telikesMeres) + " meres," + str(abs(currentHour)) + " wres, " + str(abs(currentMinute)) + " lepta, " + str(abs(currentSecond)) + "deytera")
if flag==False:
    print("oi hmeromhnies apexoun "+str(telikaXronia) + " xronia," + str(telikoiMhnes) + " mhnes," + str(telikesMeres) + " meres," + str(abs(23 - currentHour)) + " wres, " + str(abs(60 - currentMinute)) + " lepta, " + str(abs(60 - currentSecond)) + " deytera")