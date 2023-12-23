'''
    Tuple veri türü
        İçerisinde farklı veri tiplerini barındırabilir.
        Oluşturulduğu şekliyle kalan bir veri tipidir. (Değiştirilemez) (Immutable)
        Birden fazla değerin tek bir değişken içinde saklanmasını sağlar. (List, dict ve sets ile birlikte)
'''

print("Tuple oluşturma")

animals = ("horse", "dog", "bear", "squirrel", "rhino")
print(type(animals))
print(animals)

print("\nTuple packing")
'Parantez olmadan tuple oluşturma işlemine tuple paketleme adı verilir.'
packingTuple = 4, 6.0, 'python'
print(type(packingTuple))
print(packingTuple)

print("\nTuple Unpacking")
a,b,c = packingTuple
print(a)
print(b)
print(c)

print("\nTuple'daki elemanlara erişme")
' Tuple\'da ilk elemanın indis sayısı 0dır yani 0dan başlar'
notes = (80, 75, 67, 93, 35, 34)
print(notes)
print(notes[0]) # Output: 80
print(notes[1]) # Output: 75
print(notes[3]) # Output: 93
print(notes[5]) # Output: 34

print("\nTuple'a yeni eleman ekleme")
print("Elemanları değiştirilemez ve bu nedenle hata alırız, yeni eleman da ekleyemeyiz.")
print("TypeError: 'tuple' object does not support item assignment hatasını alırız")

print("\nSlicing [] Tuple'i dilimlemek")
'''
Tuple dilimleme (slicing), bir tuple'ın belirli bir alt kümesini seçmek için kullanılan bir işlemdir. 
Tuple'lar, değiştirilemeyen (immutable) veri türleri olduğu için, dilimleme sırasında orijinal tuple'ın kendisi 
değiştirilmez.
'''
# Bir tuple oluşturalım
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Tuple'ın belirli bir aralığına erişim sağlayalım ((5) son indeks hariç)
subset = my_tuple[2:5]
print(subset)  # Output: (3, 4, 5)

# Başlangıç ve bitiş indeksleri kullanarak dilimleme ((7) son indeksi hariç)
subset = my_tuple[1:7]
print(subset)  # Output: (2, 3, 4, 5, 6, 7)

# Başlangıç indeksi belirtilmezse, tuple'ın başından başlar ((5) son indeks hariç)
subset = my_tuple[:5]
print(subset)  # Output: (1, 2, 3, 4, 5)

# Bitiş indeksi belirtilmezse, tuple'ın sonuna kadar alır
subset = my_tuple[5:]
print(subset)  # Output: (6, 7, 8, 9, 10)

# Negatif indeksler kullanarak tuple'ın sonundan başlayabiliriz (son eleman hariç -1 9'a denk gelir.)
subset = my_tuple[-4:-1]
print(subset)  # Output: (7, 8, 9)

# Belirli bir adımda dilimleme yapabiliriz
subset = my_tuple[1:8:2]
print(subset)  # Output: (2, 4, 6, 8)
'''
[başlangıç:bitiş:adım] şeklinde gerçekleşir. Başlangıç ve bitiş indeksleri dilimlenen alt kümenin sınırlarını belirtir, 
adım ise kaçar kaçar ilerleyeceğimizi belirtir. İndekslerin dışında belirtilmemesi durumunda, 
başlangıç ve bitiş indeksleri varsayılan olarak sırasıyla başlangıç ve son değerlerini alır.
'''

print("\ndel (Tuple silme işlemi)")
'''
Python'da tuple veri yapısı değiştirilemezdir (immutable). 
Yani bir tuple'ın bir parçasını silmek mümkün değildir. Dolayısıyla bütün tuple'ı silmek zorundayız.  
'''
del my_tuple
print("del tuple_name")

print("\nFarklı veri tiplerini barındıran tuple")
# Bos tuple
bos_tuple = ()
print("Boş tuple: ", bos_tuple)

# String içeren tuple
dizi_tuple = ("ali", "veli", "can")
print("Dizi tuple :", dizi_tuple)

# karisik veri tipleri ile tuple
kar_tuple = ("İDEA", 24.4, 8)
print("Karışık tuple :", kar_tuple)

# iç içe tuple (
nested_tuple = ("İDEA", (9,7,6), [2, 1, 0])
print("Nested (İç içe) tuple : ", nested_tuple)

print("\nİç içe tuple elemanlarına erişme")
nested_tuple = ("İDEA", (9,7,6), [2, 1, 0])
'Yukarıda iç içe oluşturulmuş bir tuple bulunmaktadır.' \

'ilk tuple elemanlarını yazdıralım'
print(nested_tuple[0])

'İkinci tuple elemanlarını yazdıralım'
print(nested_tuple[1])

'Üçüncü tuple elemanlarını yazdıralım'
print(nested_tuple[2])

print("\n-----------------------------------------------------")

print("\nTuple Fonksiyonları")
my_tuple = (2, 3, 1, 10, 5, 6, 9, 8, 7, 4, 3, 1, 4, 6, 9, 2)

print("\nlen() - Tuple uzunluğunu döndürür")
print("len() : ", len(my_tuple))

print("\nmax() ve min() - En Büyük ve En Küçük Eleman")
print("max() : ", max(my_tuple))
print("min() :", min(my_tuple))

print("\nsum() - Elemanların Toplamı")
print("sum() : ", sum(my_tuple))

print("\ntuple() - Başka Bir Veri Türünden Tuple Oluşturma")
my_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(my_list)
print("My List :", my_list)
print("Converted tuple :", converted_tuple)

print("\nsorted() - Sıralanmış Tuple")
print("sorted(): ", tuple(sorted(my_tuple))) #tuple içerisinde bu işlemi yapmazsak dönüş list olur.

print("\ncount() - Belirli Elemanın Sayısı")
print("count(2): ", my_tuple.count(2))

print("\nindex() - Elemanın İlk İndisi")
print("index(5) : ", my_tuple.index(5))

print("\nany() ve all() - Elemanlardan Birisi veya Hepsi Doğru mu")
('any() fonksiyonu tupleın elemanlarından en az biri DOĞRU ise TRUE değerini döndürür. '
 'Tüm elemanlar YANLIŞ veya tuple boş ise FALSE döndürür. any() fonksiyonu Python 3.7 versiyonunda çalışmamaktadır.')

('all() fonksiyonu tupledaki tüm elemanlar DOĞRU olduğunda TRUE döndürürken, diğer durumlarda FALSE döndürür.')

my_tuple_1 = (True, False, True)
my_tuple_2 = (True, True, True)

print(any(my_tuple_1), all(my_tuple_1))  # Output: True False
print(any(my_tuple_2), all(my_tuple_2))  # Output: True True