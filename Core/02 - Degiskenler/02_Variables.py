'''
    Programlamada veri depolama ve yönetmenin temel birimidir. Bir değişken, bir değeri temsil eden ve program
    içinde kullanılabilen bir isimdir. Değişkenler çeşitli veri tipleri ile ilişkilendirilebilir ve probram içinde
    verilen depolanması, işlenmesi ve kullanılması içindir.

    Bir programcı, verileri doğrudan bir programa girmek yerine, verileri temsil etmek için değişkenleri kullanır
    Ardından program çalıştırıldığında değişkenler gerçek verilerle değiştirilir. Bu aynı programın farklı veri kümelerini
    işlemesini mümkün kılar.

    Değişkenlerin tersi ise sabittir (constant). Sabitler, asla değişmeyen değerlerdir.

    Diğer bir deyişle, verileri kaydettiğimiz hafıza "kutucukları"na
    (daha teknik ifade etmek gerekirse, hafızadaki adreslerine) verdiğimiz isimlere, değişken diyoruz.
    Gerek karakter dizilerinin, gerek sayıların her seferinde yeniden yeniden yazılması yerine, bunlara "isim" vererek,
    yani değişken oluşturarak tekrar tekrar kullanabiliriz.
'''

print("\nDeğişken tanımlama")
'''
    1. Değişken Tanımlama:
        Değişken tanımlamak için sadece ismi belirtmek yeterlidir. Değişkenler, değer atandığında otomatik olarak oluşturulur.

        x = 19  -----> x adında bir değişken tanımla ve değerini 10 yap
'''
x = 19


print("\nDeğişken Adlandırma Kuralları")
'''
    2. Değişken isimlendirme kuralları:
        Değişken isimleri harfle veya alt çizgi (_) ile başlamalıdır.
        Harf, rakam ve alt çizgi içerebilir, ancak rakamla başlayamaz.
        Büyük-küçük harf duyarlıdır.
        Python'un anahtar kelimeleri (if, else, while, gibi) değişken ismi olarak kullanılamaz.
'''
# Örnek Değişken tanımlamaları

ilkDegiskenimiz = "ilk değişken değeri" # Büyük küçük harf duyarlı değişken
_ilkDegiskenimiz = "_ilk Değişken Değeri"
# 1nciDegisken # rakam içerebilir ama rakamla başlayamaz.


print("\nDeğişkenler arası atama işlemi (Swapping Variables)")
'''
    3. Değişkenler arası atama işlemi (Swapping Variables)
        Değişkenler arası değer aktarımı ve matematiksel işlemler yapılabilir.
'''
a = 5
b = a  # a'nın değerini b'ye aktar
c = a + b  # a ve b'nin toplamını c'ye ata

print("\nDeğişken Türleri")
''' 
Pythonda değişkenlerin türleri dinamik olarak belirlenir, Yani bir değişkenin türünü belirtmek için önceden bir
tanımlama yapmaya gerek yoktur. Python otomatik olarak türleri belirler.
 '''
x = 5          # x bir tam sayı (int)
y = 3.14       # y bir ondalık sayı (float)
isim = "Ali"   # isim bir karakter dizisi (string)
