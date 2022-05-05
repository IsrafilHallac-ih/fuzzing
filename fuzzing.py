from email import header
import requests
dosya=open("fuzzing.txt","r")
icerik=dosya.read()
dosya.close()
header={"Cookie":"security=low;P HPSESSID=el4ukv0kqbvoirg7nkp4dncpk3"}
for i in icerik.split("\n"):
    print(i)
    url="http://10.10.10.10"+str(i)
    sonuc=requests.get(url=url,headers=header)
    if "200" in str(sonuc.status_code):
        print("Dosya veya Dizin var:",i)
    else:
        print("Dosya veya Dizin yok:",i)