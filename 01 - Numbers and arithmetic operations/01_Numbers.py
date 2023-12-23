import math

'''
Python'da Sayılar

    - Tam Sayılar / Integers (int)  : Tam sayılar pozitif ve negatif tamsayı değerlerini ifade eder.
    Herhangi bir uzunlukta bir tam sayı değerini tutabilir.

    - Floating point (float) : Noktadan sonra bir değere sahip olan sayılar floating point (Kayan noktalı)
    sayı olarak adlandırılır. Örneğin: 25.7, 0.23, ve -45.1 sayıları float'tır. Ancak 34 ve -15 integer sayılardır.

    - Complex Sayılar (x+yj): Karmaşık sayılar gerçek ve sanal bölümleri olan sayılardır.
    Reel (gerçel) sayılara ek olarak sanal (imaginer) kısım da bu sayı sistemi içinde kullanılmaktadır.
    Karmaşık sayılarda bir kayan nokta sayısından veya tamsayıdan sonra sanal kısmı ifade etmek için "i" harfi
    kullanılmaktadır.
        Örneğin: 3 + 5i karmaşık sayısını ele alalım.
        Burada 3 reel kısmı gösterirken, 5i ise sanal kısmı ifade etmektedir.
        Yanlız Python'da sanal gösterim için "j harfi kullanılır. Örneğin Python derleyicisi 15 - 1.6j kompleks sayısında,
        15 sayısını gerçel kısım, 2.6j sayısını ise sanal kısmı olarak işleme almaktadır.
'''

# Aritmetik Operatörler
'''
    Aritmetik Operatörler:
        + : Toplama
        - : Çıkarma
        * : Çarpma
        / : Bölme (gerçek sayı bölmesi)
        // : Bölme (tam sayı bölmesi)
        % : Modülüs (kalanı verir)
        ** : Üs alma
'''

# -------------------------------------------------------------------------------------------------------------------

# Tam sayılar / Integers
'''
Pozitif ve negatif tam sayı değerlerini temsil eden bir veri türüdür. Tam sayılar, int adı verilen veri tipi ile
temsil edilir.
'''

# -------------------------------------------------------------------------------------------------------------------

# Tam sayı tanımlama
' Tamsayıları tanımlamak için doğrudan bir sayı kullanabiliriz. '
x = 54  # Pozitif tam sayı
y = -34 # Negatif tam sayı

# -------------------------------------------------------------------------------------------------------------------

# Temel Aritmetik işlemler
print("--> Temel Aritmetik İşlemler <--")
' Toplama, Çıkartma, Çarpma, Bölme '

a = 10
b = 3

addition = a  + b
substraction = a - b
multiplication = a * b
division = a / b


print("Toplama:", a)
print("Çıkartma:", substraction)
print("Çarpma:", multiplication)
print("Bölme:", division)

print("---------------o---------------")
# -------------------------------------------------------------------------------------------------------------------

# Üs Alma ve Mod Alma
print("--> Üs ve Mod Alma <--")
' ** operatörü ile üs alma '
base = 2
exponent = 3
result1 = base ** exponent # 2^3 = 8

' % operatörü ile mod alma '
result2 = 10 % 3 # 10'un 3'e bölümünden kalan

print("Üs alma sonucu:", result1, "\nMod alma sonucu:", result2)

print("---------------o---------------")
# -------------------------------------------------------------------------------------------------------------------

# round() fonksiyonu
print("--> round() Fonksiyonu <--")
' Bir sayıyı belirli bir ondalık basamak sayısına yuvarlamak için kullanılır '
' yuvarlanan_sayi = round(sayi, n..digit) '
' sayi : Yuvarlanacak olan sayıyı temsil eder '
' n..digit : İsteğe bağlı bir parametre olup, sayının kaç ondalık basamağa kadar yuvarlanacağını belirtir. '

pi = 3.14159265358979323846264338327950288419716939937510
print("Yuvarlanacak sayı:", pi)
print("Yuvarlanmış sayı : ", round(pi))
print("Yuvarlanmış sayı (nsayi): ", round(pi, 3))

print("---------------o---------------")
# -------------------------------------------------------------------------------------------------------------------

# abs() fonksiyonu
print("--> abs() fonksiyonu <--")
' Bir sayının mutlak değerini döndürmek için kullanılır. '
' Mutlak değer, bir sayının negatifse pozitif, pozitifse kendisi olarak alınan değeridir. '

absNum = -5
absoluteValue = abs(absNum)
print("Sayi : ", absNum)
print("Sayının mutlak değeri: ", absoluteValue)

print("---------------o---------------")
# -------------------------------------------------------------------------------------------------------------------

# pow() fonksiyonu
print("pow() fonksiyonu")
' Bir sayının üssünü hesaplamak için kullanılır. '
' pow(x, y) ifadesi x^y işlemine karşılık gelir. '
base = 2
exponent = 3

result = pow(base, exponent)

print("pow işlemi sonucu :", result)

' Üçüncü bir üs modülü (modulus) parametresi de alabilir. Yani pow(x,y,z) ifadesi x^y%z işlemine karşılık gelir'
modulus = 5
result = pow(base, exponent, modulus)
print("\npow(x,y,z)\nx^y%z = ", result)

print("---------------o---------------")
# -------------------------------------------------------------------------------------------------------------------

# Math kütüphanesi
print("Math kütüphanesi/modülü")
' Math modülü/kütüphanesi matematiksel fonksiyonları ve sabitleri içeren bir modül/kütüphanedir. '
'''
    Fonksiyonlar:
        Temel Matematik Fonksiyonları:
            - math.ceil(x): x'in tavanını (yukarıya doğru en yakın tam sayıyı) döndürür.
            - math.floor(x): x'in tabanını (aşağıya doğru en yakın tam sayıyı) döndürür.
            - math.trunc(x): x'in kesilmiş değerini (ondan sonraki kısmı atarak) döndürür.
            - math.copysign(x, y): x'in işaretini, y'nin işaretini alarak değiştirir.
            - math.fabs(x): x'in mutlak değerini döndürür.
            - math.factorial(x): x'in faktöriyelini hesaplar.
            - math.fmod(x, y): x'in y'ye bölümünden kalanı döndürür.
            - math.frexp(x): x'i bir ondalık mertebe ve bir iki kuvvetine ayırır.
            - math.fsum(iterable): Bir iterable'ın elemanlarının toplamını hassas bir şekilde döndürür.
        
        Üs ve Kök Hesaplamaları:
            - math.pow(x, y): x'in y. kuvvetini döndürür.
            - math.sqrt(x): x'in karekökünü döndürür.
            - math.exp(x): e^x işlemini hesaplar.
            - math.log(x[, base]): x'in logaritmasını, belirtilen taban (varsayılan olarak e) üzerinden döndürür.

        Trigonometrik Fonksiyonlar:
            - math.sin(x), math.cos(x), math.tan(x): Sırasıyla sinüs, kosinüs ve tanjant fonksiyonlarını hesaplar.
            - math.asin(x), math.acos(x), math.atan(x): Sırasıyla arkussin, arkuskosin ve arkustanjant fonksiyonlarını hesaplar.
            - math.atan2(y, x): Verilen koordinatlardaki (x, y) noktasının arkustanjantını hesaplar.

        Hiperbolik Fonksiyonlar:
            - math.sinh(x), math.cosh(x), math.tanh(x): Sırasıyla hiperbolik sinüs, kosinüs ve tanjant fonksiyonlarını hesaplar.

        Sayı Yuvarlama:
            - math.ceil(x): x'in tavanını döndürür.
            - math.floor(x): x'in tabanını döndürür.
            - math.trunc(x): x'in tam kısmını döndürür.

        Sayılar Arası İlişkiler:
            - math.isclose(a, b): a ve b sayılarının eşit olup olmadığını kontrol eder.

        Faktöriyel ve Kombinasyonlar:
            - math.factorial(x): x'in faktöriyelini hesaplar.
            - math.comb(n, k): n'in k'ye olan kombinasyonunu hesaplar.

        Sabitler:
            - math.pi: π (pi) sayısını temsil eder.
            - math.e: e sayısını temsil eder.
'''

' Temel Matematik Fonksiyonları: '
print("\nTemel matematik fonksiyonları")

print("\nmath.ceil(x)")
" x'in tavanını (yukarıya doğru en yakın tam sayıyı) döndürür."
result = math.ceil(4.25)
print(result)  # Çıktı: 5

print("\nmath.floor(x)")
" x'in tabanını (aşağıya doğru en yakın tam sayıyı) döndürür. "
result = math.floor(4.75)
print(result)  # Çıktı: 4

print("\nmath.trunc(x)")
"x'in kesilmiş değerini (ondan sonraki kısmı atarak) döndürür."
result = math.trunc(4.99)
print(result)  # Çıktı: 4

print("\nmath.copysign(x, y)")
"x'in işaretini, y'nin işaretini alarak değiştirir."
result = math.copysign(3.14, -1)
print(result)  # Çıktı: -3.14

print("\nmath.fabs(x)")
"x'in mutlak değerini döndürür."
result = math.fabs(-3.14)
print(result)  # Çıktı: 3.14

print("\nmath.factorial(x)")
"x'in faktöriyelini hesaplar."
result = math.factorial(5)
print(result)  # Çıktı: 120

print("\nmath.fmod(x, y)")
"x'in y'ye bölümünden kalanı döndürür."
result = math.fmod(10, 3)
print(result)  # Çıktı: 1.0

print("\nmath.frexp(x)")
"x'i bir ondalık mertebe ve bir iki kuvvetine ayırır."
mantissa, exponent = math.frexp(16)
print(mantissa, exponent)  # Çıktı: 0.5 5

print("\nmath.fsum(iterable)")
"Bir iterable'ın elemanlarının toplamını hassas bir şekilde döndürür."
result = math.fsum([0.1, 0.2, 0.3])
print(result)  # Çıktı: 0.6

print("---------------o---------------")

# Üs ve Kök Hesaplamaları:
print("\nÜs ve Kök Hesaplamaları:")

print("\nmath.pow(x, y)")
"x'in y. kuvvetini döndürür."
result = math.pow(2, 3)
print(result)  # Çıktı: 8.0

print("\nmath.sqrt(x)")
"x'in karekökünü döndürür."
result = math.sqrt(25)
print(result)  # Çıktı: 5.0

print("\nmath.exp(x)")
'e^x işlemini hesaplar.'
result = math.exp(2)
print(result)  # Çıktı: 7.3890560989306495

print("\nmath.log(x[, base])")
"x'in logaritmasını, belirtilen taban (varsayılan olarak e) üzerinden döndürür."
result = math.log(8, 2)
print(result)  # Çıktı: 3.0 (log2(8))

print("---------------o---------------")

# Trigonometrik Fonksiyonlar:
print("\nTrigonometrik Fonksiyonlar:")

print("\nmath.sin(x)")
'Sinüs fonksiyonunu hesaplar.'
result = math.sin(math.radians(30))
print(result)  # Çıktı: 0.49999999999999994

print("\nmath.cos(x)")
'Kosinüs fonksiyonunu hesaplar.'
result = math.cos(math.radians(60))
print(result)  # Çıktı: 0.5000000000000001

print("\nmath.tan(x)")
'Tanjant fonksiyonunu hesaplar.'
result = math.tan(math.radians(45))
print(result)  # Çıktı: 0.9999999999999999

print("\nmath.asin(x)")
'Arkussin fonksiyonunu hesaplar.'
result = math.asin(0.5)
print(result)  # Çıktı: 0.5235987755982989 (radyan cinsinden)

print("\math.acos(x)")
'Arkuskosin fonksiyonunu hesaplar.'
result = math.acos(0.5)
print(result)  # Çıktı: 1.0471975511965979 (radyan cinsinden)

print("\nmath.atan(x)")
'Arkustanjant fonksiyonunu hesaplar.'
result = math.atan(1)
print(result)  # Çıktı: 0.7853981633974483 (radyan cinsinden)

print("\nmath.atan2(y, x)")
'Verilen koordinatlardaki (x, y) noktasının arkustanjantını hesaplar.'
result = math.atan2(1, 1)
print(result)  # Çıktı: 0.7853981633974483 (radyan cinsinden)

print("---------------o---------------")

# Hiperbolik Fonksiyonlar:
print("\nHiperbolik Fonksiyonlar:")

print("\nmath.sinh(x)")
'Hiperbolik sinüs fonksiyonunu hesaplar.'
result = math.sinh(1)
print(result)  # Çıktı: 1.1752011936438014

print("\nmath.cosh(x)")
'Hiperbolik kosinüs fonksiyonunu hesaplar.'
result = math.cosh(1)
print(result)  # Çıktı: 1.5430806348152437

print("\nmath.tanh(x)")
'Hiperbolik tanjant fonksiyonunu hesaplar.'
result = math.tanh(1)
print(result)  # Çıktı: 0.7615941559557649

print("---------------o---------------")

# Sayı Yuvarlama:
print("\nSayı Yuvarlama:")

print("\nmath.ceil(x)")
"x'in tavanını döndürür."
result = math.ceil(4.25)
print(result)  # Çıktı: 5

print("\nmath.floor(x)")
"x'in tabanını döndürür."
result = math.floor(4.75)
print(result)  # Çıktı: 4

print("\nmath.trunc(x)")
"x'in tam kısmını döndürür."
result = math.trunc(4.99)
print(result)  # Çıktı: 4

print("---------------o---------------")

# Sayılar Arası İlişkiler:
print("\nSayılar Arası İlişkiler:")

print("\nmath.isclose(a, b)")
'a ve b sayılarının eşit olup olmadığını kontrol eder.'
result = math.isclose(0.1 + 0.2, 0.3)
print(result)  # Çıktı: True

print("\nmath.isfinite(x)")
"x'in sonlu bir sayı olup olmadığını kontrol eder."
result = math.isfinite(3.14)
print(result)  # Çıktı: True

print("\nmath.isinf(x)")
"x'in sonsuz bir sayı olup olmadığını kontrol eder."
result = math.isinf(float('inf'))
print(result)  # Çıktı: True

print("\nmath.isnan(x)")
"x'in bir sayı olup olmadığını kontrol eder."
result = math.isnan(float('nan'))
print(result)  # Çıktı: True

print("---------------o---------------")

# Faktöriyel ve Kombinasyonlar:
print("\nFaltöriyel ve Kombinasyonlar")

print("\nmath.factorial(x)")
"x'in faktöriyelini hesaplar."
result = math.factorial(5)
print(result)  # Çıktı: 120

print("\nmath.comb(n, k)")
"n'in k'ye olan kombinasyonunu hesaplar."
result = math.comb(5, 2)
print(result)  # Çıktı: 10

print("---------------o---------------")

# Sabitler:
print("\nSabitler")

print("\nmath.pi")
'π (pi) sayısını temsil eder.'
result = math.pi
print(result)  # Çıktı: 3.141592653589793

print("\nmath.e ")
'e sayısını temsil eder.'
result = math.e
print(result)  # Çıktı: 2.718281828459045

print("---------------o---------------")
