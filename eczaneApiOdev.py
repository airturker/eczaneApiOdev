import http.client
import json
conn=http.client.HTTPSConnection("api.collectapi.com")
headers = {
    'content-type': "application/json",
    'authorization': "apikey 1WGj2kLsPQrkKY0woHpy5B:4CcLtI3GdFIiibgIb2zhpl"
    }


il=input("il  giriniz : ")
if il=="":
    print("il bilgisi bos, varsayilan olarak Ankara yapildi")
    il=="Ankara"
else:
    il=il.strip().capitalize()

ilce=input("ilce giriniz : ")
if ilce=="":
    print("ilce bilgisi bos, varsayilan olarak Çankaya yapildi")
    ilce=="Çankaya"
else:
    ilce=ilce.strip().capitalize()
print(il,ilce)

bilgi="/health/dutyPharmacy?ilce="+ilce+"&il="+il
conn.request("GET",bilgi,headers=headers)
res=conn.getresponse()
data=res.read()
veri=data.decode("utf-8")
json_veri=json.loads(veri)

if json_veri["success"]==True:
    bilgi=json_veri["result"][0]
    print("eczane adi : "+ bilgi["name"]+"adresi : "+bilgi["address"])
else:
    print("istek basarisiz")