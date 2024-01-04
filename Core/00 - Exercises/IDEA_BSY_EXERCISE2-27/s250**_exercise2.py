'''
    KONU
        İnternette sosyal medya platformlarında, işimizle alakalı mecralarda ya da bankacılık işlemlerinde
        farklı hesaplar ve bu hesaplarla ilişkili farklı farklı şifrelere ihtiyaç duyarız. Bu ödev kapsamında da
        kullanıcılardan belirlenen kurallara uygun bir şifre isteyip bu şifrenin geçerliliğini ve güçlülüğünü
        ölçen bir program tasarlayacağız

    AYRINTILAR
        1. Tasarlayacağınız program ilk olarak kullanıcıdan girdi olarak bir şifre isteyecektir. --> OK
        2. Şifre geçerliliği aşağıdaki maddelere bağlı olarak tespit edildiğinde:
            a. Kurallara uygun şifre için → "Geçerli Şifre"
            b. Kuralları ihlal eden şifre için → "Geçersiz Şifre" mesajı ekrana basılacaktır.
        3. Şifre uzunluğu 4 ile 8 arasında olabilir:
            a. 4’ten daha az karakter içeren şifreler için → "Şifre çok kısa"
            b. 8’den fazla karakter içeren şifreler için → "Şifre en fazla 8 karakter olabilir" mesajı
        ekrana basılacaktır.
        4. Şifrede İngiliz alfabesindeki küçük harflerden (‘a’ dan ‘z’ ye) en az bir adet yer almalıdır.
            Yer almadığı takdirde "Şifre en az bir küçük harf içermeli" mesajı ekrana basılacaktır.
        5. Şifrede İngiliz alfabesindeki büyük harflerden (‘A’ dan ‘Z’ ye) en az bir adet yer almalıdır.
            Yer almadığı takdirde "Şifre en az bir büyük harf içermeli" mesajı ekrana basılacaktır.
        6. Şifrede en az bir rakam bulunmalıdır. Bu kuralı ihlale yönelik ekrana basılacak olan mesaj
            "Şifre en az bir rakam içermeli" şeklindedir.
        7. Şifrede rakamlar ve İngiliz alfabesinde yer alan harfler haricinde yalnızca şu karakterler
        bulunabilir:
            a. ‘(‘ → parantez açma
            b. ‘)’ → parantez kapama
            c. ‘*’ → yıldız (asteriks)
            d. ‘+’ → artı
            e. ‘,‘→ virgül
            f. ‘
            -‘→ kısa çizgi (tire)
            g. ‘.’ → nokta
            Yukarıdaki karakterlerden en az biri şifrede yer almadığında "Şifre izin verilen özel
            karakterlerden en az birini içermeli" mesajı ekrana basılacaktır.
        8. Şifre Türkçe karakter ya da bir önceki maddede açıklanan özel karakterler haricinde başka
            özel karakterler içeremez. Bu kuralın ihlalinde ekrana basılacak olan mesaj da "Şifre
            yalnızca sayı, harf ve izin verilen özel karakterlerden oluşmalı" şeklindedir.
        9. Yukarıda belirtilen kurallardan hiçbiri ihlal edilmediği durumda şifre geçerli olacaktır.
            Geçerli olan şifredeki her bir karakterin özelliğine göre bir puan atanıp şifrenin güçlülük
            skoru hesaplanacaktır. Farklı karakterlerin değerleri aşağıda listelenmiştir.
                a. Küçük harf → 3 puan
                b. Büyük harf → 5 puan
                c. Rakam → 2 puan
                d. Özel karakter → 4 puan

        Güçlülük skoru aşağıdaki formüle göre hesaplanmaktadır:
        G = 3 * (Küçük_Harf_Sayısı + 1) * 5 * (Büyük_Harf_Sayısı + 1) * 2 * (Rakam_Sayısı + 1) * 4 * (Özel_Karakter_Sayısı + 1) − 120

            Örneğin “OdTu.56*” şifresinin skoru hesaplanırken:
                • ‘O’ ve ‘T’ harfleri ile Büyük_Harf_Sayısı = 2,
                • ‘d’ ve ‘u’ harfleri ile Küçük_Harf_Sayısı = 2,
                • ‘5’ ve ‘6’ rakamları ile Rakam_Sayısı = 2,
                • ‘.’ ve ‘*’ özel karakterler olduğundan Özel_Karakter_Sayısı = 2
            olarak değerlendirilir ve Bu şifrenin güçlük skoru
            G = 3 * (2 + 1) * 5 * (2 + 1) * 2 * (2 + 1) * 4 * (2 + 1) − 120 = 9600

            işlemlerinden 9600 olarak hesaplanır. Hesaplanan skora göre:
                • Eğer skor 2000’den küçükse:
                    o Ekrana “Çok Zayıf Şifre” bastırılacak
                • Eğer skor >= 2000 ve skor < 4000 ise
                    o Ekrana “Zayıf Şifre” bastırılacak
                • Eğer skor >= 4000 ve skor < 6000 ise
                    o Ekrana “Ortalama Şifre” bastırılacak
                • Eğer skor >= 6000 ve skor < 9000 ise
                    o Ekrana “Güçlü Şifre” bastırılacak
                • Eğer skor >= 9000 ise
                    o Ekrana “Çok Güçlü Şifre” bastırılacak

        Not: Programınız değerlendirilirken aynı anda birden fazla kuralın ihlal edildiği girdi
        verilmeyecektir. Dolayısıyla tasarımınızda kuralları kontrol sıranızın önemi yoktur.

        Önemli Not: Değerlendirmede temelde kara kutu test (black-box testing) yöntemi
        uygulanacağından girdi alırken veya diğer işlem sırasında programınızın istenen mesaj formatı
        haricinde farklı çıktılarının olmaması gerekmektedir. Bu nedenle kural ihlallerinin mesajını
        doğrudan programa kopyalarak uygulamak, gereksiz puan kaybını engelleyebilir.

        TAVSİYE BAĞLANTILAR
            • ASCII tablosu: https://en.wikipedia.org/wiki/ASCII
            • String yöntemleri: https://docs.python.org/3/library/string.html
'''


# Kontrol Değişkenleri
lowerCaseAlphabets = "abcdefghijklmnopqrstuvwxyz"
upperCaseAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
allowedSpecialCharacters = "()*+,'.-"

# Sayaç Değişkenleri
lowerCaseAlphabetsCount = 0
upperCaseAlphabetsCount = 0
numbersCount = 0
allowedSpecialCharactersCount = 0

userPassword = input("Lütfen bir şifre giriniz: ") # Kullanıcıdan şifre al

if len(userPassword) < 4: # Şifre uzunluğu kontrolü
    print("Şifre çok kısa")
elif len(userPassword) > 8:
    print("Şifre en fazla 8 karakter olabilir")
else: # Şifre uzunluğu 4 ile 8 arasında ise
    for i in userPassword: # Şifrenin her bir karakteri için kontrollerin yapılması
        if i in lowerCaseAlphabets:
            lowerCaseAlphabetsCount += 1
        elif i in upperCaseAlphabets:
            upperCaseAlphabetsCount += 1
        elif i in numbers:
            numbersCount += 1
        elif i in allowedSpecialCharacters:
            allowedSpecialCharactersCount += 1
        else: # Şifrede Türkçe karakter ya da bir önceki maddede açıklanan özel karakterler haricinde başka özel karakterler içeriyorsa
            print("Şifre yalnızca sayı, harf ve izin verilen özel karakterlerden oluşmalı")
            break
    else: # Şifrede Türkçe karakter ya da bir önceki maddede açıklanan özel karakterler haricinde başka özel karakterler içermiyorsa
        if lowerCaseAlphabetsCount == 0:
            print("Şifre en az bir küçük harf içermeli")
        elif upperCaseAlphabetsCount == 0:
            print("Şifre en az bir büyük harf içermeli")
        elif numbersCount == 0:
            print("Şifre en az bir rakam içermeli")
        elif allowedSpecialCharactersCount == 0:
            print("Şifre izin verilen özel karakterlerden en az birini içermeli")
        else: # Skor hesaplama ve güçlülük skoruna göre şifrenin güçlülük seviyesinin belirlenmesi
            score = 3 * (lowerCaseAlphabetsCount + 1) * 5 * (upperCaseAlphabetsCount + 1) * 2 * (numbersCount + 1) * 4 * (allowedSpecialCharactersCount + 1) - 120
            if score < 2000:
                print("Çok Zayıf Şifre")
            elif score >= 2000 and score < 4000:
                print("Zayıf Şifre")
            elif score >= 4000 and score < 6000:
                print("12Ortalama Şifre")
            elif score >= 6000 and score < 9000:
                print("Güçlü Şifre")
            else:
                print("Çok Güçlü Şifre")








