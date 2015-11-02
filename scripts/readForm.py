#!/usr/bin/env python3

import cgi,cgitb,createObject,datetime

cgitb.enable()

print("Content-Type: text/html")
print()
print("""
    <TITLE>Add Item</TITLE>
    <H1>Add Item</H1>
""")


formData = cgi.FieldStorage()
	
desc = formData['itemDesc'].value
donor = formData['itemDonorName'].value
imgurl = formData['itemImgURL'].value
name = formData['itemName'].value
startPrice = int(formData['itemPrice'].value)

openDate = str(formData['itemOpenDate'].value)
openTimeRaw = str(formData['itemOpenTime'].value)

closeDate = str(formData['itemCloseDate'].value)
closeTimeRaw = str(formData['itemCloseTime'].value)

# Process date/time into correct formats
	# html date output: YYYY-MM-DD
	# html time output: HH(24):MM

openYear = openDate[0:3]
openMonth = openDate[5:6]
openDay = openDate[8:9]
openHour = openTimeRaw[0:1]
openMin = openTimeRaw[3:4]

closeYear = closeDate[0:3]
closeMonth = closeDate[5:6]
closeDay = closeDate[8:9]
closeHour = closeTimeRaw[0:1]
closeMin = closeTimeRaw[3:4]


openTime = datetime.datetime(openYear,openMonth,openDay,openHour,openMin).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
closeTime = datetime.datetime(closeYear,closeMonth,closeDay,closeHour,closeMin).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

print("<p>name:", name, "</p>")
print("<p>desc:", desc, "</p>")
print("<p>donor:", donor, "</p>")
print("<p>startPrice:", startPrice, "</p>")
print("<p>imgurl:", imgurl, "</p>")
print("<p>openTime:", openTime, "</p>")
print("<p>closeTime:", closeTime, "</p>")


print("<p>", createObject.create(name,desc,donor,startPrice,imgurl,openTime,closeTime), "</p>")