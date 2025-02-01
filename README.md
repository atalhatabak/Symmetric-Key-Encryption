# Symmetric-Key-Encryption
Girilen key ile bir metni şifreleyen ve şifrelenmiş metni geri çözen bir algoritma


        Kullanım: python hash [mission] [params] \n
        Örnek Kullanım: python hash.py -E -T "Örnek Metin" -K test
        Mission:
            --encrypt | -E  girilen metini şifreler
            --decrypt | -D şifreli metini çözer \n
        Params:
            --text | -T Şifrelenecek veya çözülecek Metin
            --key | -K Şifrelenecek veya çözülecek metinin şifreleme key'i 
            --help | -H \n
        Return:
            Mission'a göre şifrelenmiş metin veya çözülmüş metin

örn komut <br>
<code>python hash.py -E -T "Projenin ilk versiyonu Github'a Yüklenmeye Hazır" -K "Github"</code><br>
çıktı:<br>
<code>-ğ_=,t\yzİz?@UKq^Ez}?:{3
:Gt{*xpU#g=x-BCq{rXX(~o_-</code><br>
![Screenshot_20240211_043715](https://github.com/atalhatabak/Symmetric-Key-Encryption/assets/56918326/0e83cefd-ee40-4cd7-b5ff-cebaaaa2b56f)<br>

örn komut <br>
<code>python hash.py -D -T "-ğ_=,t\yzİz?@UKq^Ez}?:{3
:Gt{*xpU#g=x-BCq{rXX(~o_-" -K "Github"</code><br>
çıktı:<br>
<code>Projenin ilk versiyonu Github'a Yüklenmeye Hazır</code><br>
![Screenshot_20240211_043803](https://github.com/atalhatabak/Symmetric-Key-Encryption/assets/56918326/d4ebc952-887f-4b83-acca-1aec2527e276)
