print("\n---> Parametreler ve Argümanlar | Parameters and Arguments <---")
# Parametre ve argüman kelimeleri çoğunlukla aynı amacı belirtmek için kullanılırlar ve temel olarak fonksiyona
    # aktarılan bilgiler olarak tanımlanırlar.
# Bir fonksiyonun bakış açısından:
    # Parametre, işlev tanımında parantez içinde listelenen değişkendir.
    # Argüman, çağrıldığında fonksiyona gönderilen değerdir.
# Bir programlama dili ile program geliştirirken, önemli özelliklerden bir tanesi, fonksiyonlara aktarılan değerlerin
# (argümanların) parametrelere nasıl atandığıdır. Python'da fonksiyonlara istediğiniz sayıda parametre verebilirsiniz.
# Her parametreyi virgülle ayırmalı ve her parametre için ayrı bir isim belirlenmelidir

print("Example 1 --> Parametreler ve Argümanlar | Parameters and Arguments")
def fonksiyon(parametre1, parametre2): # Fonksiyon tanımlama | Function definition
    print(parametre1, parametre2) # Fonksiyonun gövdesi | Function body

fonksiyon("Merhaba", "Dünya") # Fonksiyonu çağır | Call the function
print("Program ended | Program sonlandı\n")

print("Example 2 --> Required Arguments | Zorunlu Argümanlar")
def sum(a, b): # Fonksiyon tanımlama | Function definition
    return a + b # Fonksiyonun sonucunu döndürür | Returns the result of the function

print(sum(3, 4))
print("Program ended | Program sonlandı\n")

print("Example 3 --> Required Arguments | Zorunlu Argümanlar")
def listeIslemleri(liste): # Fonksiyon tanımlama | Function definition
    liste.append(4) # Fonksiyonun gövdesi | Function body
    print(liste) # Fonksiyonun gövdesi | Function body

L = [1, 2, 3] # Liste | List
listeIslemleri(L) # Fonksiyonu çağır | Call the function
print(L) # Sonucu yazdır | Print the result
print("Program ended | Program sonlandı\n")

print("\n---> Varsayılan Parametreler | Default Parameters <---")
# Varsayılan parametreler, bir fonksiyona argüman olarak geçirilmezse kullanılacak değerlerdir.
# Varsayılan parametreler, fonksiyon tanımında parametrelerin yanında belirtilir.
# Varsayılan parametrelerin, fonksiyon tanımında en sonda olması gerekir.

print("Example 1 --> Varsayılan Parametreler | Default Parameters")
def selamla(isim="Dünya"): # Fonksiyon tanımlama | Function definition
    print("Merhaba", isim) # Fonksiyonun gövdesi | Function body

selamla("Ahmet") # Fonksiyonu çağır | Call the function
selamla() # Fonksiyonu çağır | Call the function
print("Program ended | Program sonlandı\n")

print("Example 2 --> Varsayılan Parametreler | Default Parameters")
def selamla(isim="Dünya", soyisim=""):  # Fonksiyon tanımlama | Function definition
    print("Merhaba", isim, soyisim) # Fonksiyonun gövdesi | Function body

selamla("Ahmet", "Yılmaz") # Fonksiyonu çağır | Call the function
selamla("Ahmet") # Fonksiyonu çağır | Call the function
selamla() # Fonksiyonu çağır | Call the function
print("Program ended | Program sonlandı\n")

print("Example 3 --> Varsayılan Parametreler | Default Parameters")
def selamla(isim, soyisim=""):  # Fonksiyon tanımlama | Function definition
    print("Merhaba", isim, soyisim) # Fonksiyonun gövdesi | Function body

selamla("Ahmet", "Yılmaz")
selamla("Ahmet")
# selamla()
print("Program ended | Program sonlandı\n")

print("\n---> Esnek Sayıda Parametreler | Flexible Number of Parameters <---")
# Esnek sayıda parametreler, fonksiyona istediğiniz sayıda parametre geçmenizi sağlar.
# Esnek sayıda parametreler, fonksiyon tanımında parametrelerin yanında * ile belirtilir.
# Esnek sayıda parametreler, fonksiyon içinde tuple olarak kullanılır.

print("Example 1 | Flexible Number of Parameters | Esnek Sayıda Parametreler")
def selamla(*args):
    print("Merhaba", args)

selamla("Ahmet", "Yılmaz", 23)
selamla("Ahmet")
selamla()
print("Program ended | Program sonlandı\n")

print("Example 2 | Flexible Number of Parameters | Esnek Sayıda Parametreler")
def selamla(*args):
    for i in args:
        print("Merhaba", i)

selamla("Ahmet", "Yılmaz", 23)
selamla("Ahmet")
selamla()
print("Program ended | Program sonlandı\n")

print("Example 3 | Flexible Number of Parameters | Esnek Sayıda Parametreler")
def selamla(*args):
    for i in args:
        print("Merhaba", i)

selamla("Ahmet", "Yılmaz", 23)
selamla("Ahmet")
selamla()
print("Program ended | Program sonlandı\n")

print("\n---> Esnek Sayıda Anahtar Kelimeli Parametreler | Flexible Number of Keyword Parameters <---")
# Esnek sayıda anahtar kelimeli parametreler, fonksiyona istediğiniz sayıda anahtar kelime parametre geçmenizi sağlar.
# Esnek sayıda anahtar kelimeli parametreler, fonksiyon tanımında parametrelerin yanında ** ile belirtilir.
# Esnek sayıda anahtar kelimeli parametreler, fonksiyon içinde sözlük olarak kullanılır.

print("Example 1 --> Esnek Sayıda Anahtar Kelimeli Parametreler | Flexible Number of Keyword Parameters")
def selamla(**kwargs):
    print("Merhaba", kwargs)

selamla(isim="Ahmet", soyisim="Yılmaz", numara=23)
selamla(isim="Ahmet")
selamla()
print("Program ended | Program sonlandı\n")

print("Example 2 --> Esnek Sayıda Anahtar Kelimeli Parametreler | Flexible Number of Keyword Parameters")
def selamla(**kwargs):
    for key, value in kwargs.items():
        print("Merhaba", key, value)

selamla(isim="Ahmet", soyisim="Yılmaz", numara=23)
selamla(isim="Ahmet")
selamla()
print("Program ended | Program sonlandı\n")
