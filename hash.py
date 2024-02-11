import sys
import string
import hashlib

def help () :
    print("""
        Şifreleme Key'i ile değişken gösteren çift yönlü şifreleme algoritması \n
        Kullanım: python Hash [mission] [params] \n
        Örnek Kullanım: python Hash.py -E -T "Örnek Metin" -K test
        Mission:
            --encrypt | -E  girilen metini şifreler
            --decrypt | -D şifreli metini çözer \n
        Params:
            --text | -T Şifrelenecek veya çözülecek Metin
            --key | -K Şifrelenecek veya çözülecek metinin şifreleme key'i 
            --help | -H \n
        Return:
            Mission'a göre şifrelenmiş metin veya çözülmüş metin
    """)
    sys.exit()

chars = "çÇöÖüÜğĞşŞıİ" + string.ascii_letters + string.digits + string.punctuation + string.whitespace # Büyük, küçük harfler, noktalama işaretleri, boşluk karakterleri ve sayıları içeren bir dizi len(chars)=112 chars[111] son karakter

def makeKey (text, keyM) : # girilen key algoritmaya uygun hale getiriliyor. 
    keyM = hashlib.sha256(key.encode('utf-8')).hexdigest() # key sha256 ile şifreleniyor
    i = 0
    while  len(text) > len(keyM )  : # text'in karakter sayısı key'in karakter sayısından büyük ise... ki genelde öyle olacaktır
        keyM = keyM + keyM[i] # key'e key'in ilk karakterinden itibaren eşitlenene kadar karakter ekleniyor. örn Deneme -> DenemeDen
    return keyM

def encrypt (text, key) : # Şifreleme Algoritması -E --encrypt
    key = makeKey(text, key)
    newText = ""
    i = 0  
    while i < len(text):
        newText = newText + chars[ ( chars.index( text[i] ) +  chars.index( key[i] ) ) % len(chars)  ] # yeni diziye chars dizisindeki rastgele karakter atanıyor. KeyVar = girilen text ve key e göre rastgele bir sayı
        i+=1
    return "-"+newText+"-" # Şifrelenmiş veri başında ve sonunda tire ile return olarak dönüyor

def decrypt (text, key) : # Çözme Algoritması -D --decrypt
    text = text[1:-1] #Şifrelenmiş verinin başındaki ve sonundaki tire alınıyor
    key = makeKey(text, key)
    newText = ""
    i = 0
    while i < len(text):
        newText = newText + chars[ ( chars.index( text[i] ) -  chars.index( key[i] ) ) % len(chars)  ]
        i+=1
    return newText

command = sys.argv[1:] # konsoldan alınan parametreler

help() if "--help" in command or "-H" in command else "" # help parametresi girilmiş ise help fonksiyonu çağrılıyor
mission = None if ( ( "--encrypt" in command or "-E" in command) and ("--decrypt" in command or "-D" in command ) ) else  "encrypt" if ( "--encrypt" in command or "-E" in command ) else  "decrypt" if ( "--decrypt" in command or "-D" in command )  else None 
    # iki parametre girilmiş veya hiç girilmemişse değeri None yap bir defa girilmiş ise normal değeri ata
text = command[command.index("--text" if "--text" in command else "-T") + 1] if ("--text" in command or "-T" in command) else None # text parametresi girilmiş ise değeri ata girilmemişse None yap
key = command[command.index("--key" if "--key" in command else "-K") + 1] if ("--key" in command or "-K" in command) else None # same
problem = True if mission is None or text is None or key is None else False # eğer herhangi bir parametre girilmemiş ise problem True olarak değiştiriliyor

print("--Görev parametresi girilmemiş veya hatalı girilmiş \n" if mission is None else "" , end='' ) # eğer herhangi bir parametre girilmemiş ise Hata mesajları yazılıyor
print("--text parametresi girilmemiş \n" if text is None else "" , end='')
print("--key parametresi girilmemiş \n" if key is None else "" , end='')

sys.exit("Uygulama Sonlanıyor \n Yardım için --help komutunu kullanabilirsiniz") if problem else "" # eğer problem varsa uygulama sonlanıyor
print(encrypt(text, key) if mission == "encrypt" else decrypt(text, key)) # Tüm parametreler düzgün girilmiş ise ilgili fonksiyon çalışıyor ve çıktı yazdırılıyor