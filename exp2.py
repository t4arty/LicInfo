import json
import random
import re

#some useless function
def rdStr(howmany):
    x = int(howmany)
    chars = ["a","b","c","d","e","1"]
    getString = ""
    i = 1
    while i < x:
        getString += str(chars[random.randint(0,len(chars)-1)])
        i = i + 1
    return getString

class Licence:
    res = {}
    arraylic = []
    arrayusers = []

    def __init__(self):
        pass

    def addlicences(self, lic={}):
        #{"name":"autocad","expiry":"20-10-2019","total":10,"count":5,"users": users}
        #
        self.arraylic.append(lic)
        pass

    def addusersarray(self, userss={}):
        #{"username" : "user12","armname" : "armname52","starttime" : "Wed 6/5 17:18"}
        #
        self.arrayusers.append(userss)
        pass

    def results(self):
        #here make result dict
        self.res = { "licences" : self.arraylic, "count" : len(self.arraylic)}
        return json.dumps(self.res, indent=4)

aaa = Licence()

lmutil = ""
# getting data
# encoding='utf-8' take out becose macOS wont getiing it
with open('all.tmp', 'r', encoding='utf8') as ofile: #output for parsing
    openfile = ofile.readlines()
    ofile.close()

lmutil = openfile

# licenses
c = 0
licsPos = []
for lics in lmutil:
    reLic = re.findall(r'^Users.*\)', lics)
    if len(reLic) > 0:
        licsPos.append(c)
    c += 1
##
licsPos.append(len(lmutil))
##for licenses
licenseAll = []
lstdata = []
expiry = ""
users = list()
##

for i in range(len(licsPos) - 1):
    licName = str(lmutil[licsPos[i]]).split(" ")[2].replace(":", "")  # name lic
    licTotal = int(lmutil[licsPos[i]].split(" ")[6])  # total count lic for use
    licUsing = int(lmutil[licsPos[i]].split(" ")[12])  # using count lic
    #licexpiry = re.findall(, str(lmutil[licsPos[i]])) # expiry trying
    lstdata = []
    

    for ii in range(licsPos[i], licsPos[i + 1]):
        if lmutil[ii].__contains__("expiry"):
            expiry = re.findall(r'expiry.{0,100}\b', lmutil[ii].strip())
            expiry = str(expiry[0]).split(" ")[1]

        dt = lmutil[ii].strip()
        if (dt != ''):
            lstdata.append(lmutil[ii])
        
        if (dt.__contains__('start ')):
            users.append({"username" : dt.split(" ")[0], "arm" : dt.split(" ")[1]})
    
    aaa.addlicences({"name" : licName, "total" : licTotal, "using" : licUsing, "expiry" : expiry, "users": users})
    users = list()
    expiry = "None"


print(aaa.results())
