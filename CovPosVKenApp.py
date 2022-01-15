import bs4
import requests
import time

def printData():
    print("COVID positivity rate, 7-day average: "+pos[0].text)
    print("Kenney Approval Rating: "+str(KenRat)+'%')
    print("Poll source: "+PolSour+", "+PolDat)
    print("#ableg #covid19AB")
    
#Get the latest COVID positiity Data
re=requests.get('https://www.alberta.ca/stats/covid-19-alberta-statistics.htm')
abCov = bs4.BeautifulSoup(re.text,'html.parser')
pos=abCov.select('#tile2 > span.info-tile-large-text')
#print(pos[0].text)
posnum=float(pos[0].text[:-1])
#
KenRat=29
PolSour="Maru"
PolDat="12/6/21"
locT=time.localtime()
Day=str(locT.tm_mon)+'/'+str(locT.tm_mday)+'/'+str(locT.tm_year)
#To do, have data printing in a function
print(Day)
if posnum > KenRat:
    print("Yes, Alberta's COVID positivity rate is higher than than Jason Kenney's approval rating.")
    printData()
else:
    print("No, Alberta's COVID positivity rate is NOT higher than than Jason Kenney's approval rating.")
    printData()

#Check if the data changed
with open('data.txt','r') as oldat:
    oDay=oldat.readline()
    oCov=oldat.readline()
    oKen=oldat.readline()
    oSor=oldat.readline()
    oPD=oldat.readline()

if oDay != Day or oCov != pos[0].text or oSor != PolSour or oPD != PolDat:
    print("\n Data has changed")

    with open('data.txt','w') as updat:
        updat.writelines([Day,'\n'+pos[0].text,'\n'+str(KenRat),'\n'+PolSour,'\n'+PolDat])
