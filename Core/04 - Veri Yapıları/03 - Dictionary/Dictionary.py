'''
    sadece indeksler yardımıyla değil, anahtar kullanarak da işlemler yapabiliriz.
    Bu nedenle "dict" (dictionary kelimesinin kısaltmasıdır ve Türkçesi sözlük demektir) veri yapısı geliştirilmiştir.
    Bu veri yapısında belirli bir anahtara karşılık gelen bir değer bulunmaktadır.
    Bu tek bir değer olabileceği gibi, "tuple", "list" ve "dict" türünde veri yapısı da olabilir.

    Sözlükler (Dictionary)
    - Sözlükler, key-value (anahtar-değer) yapısına sahiptir.
    - Sözlüklerde key değerleri unique'dir. Yani aynı key değerini iki kere yazamayız.
    - Sözlüklerde value değerleri unique olmak zorunda değildir.
    - Sözlüklerde key değerleri immutable olmak zorundadır. Yani listeler ve sözlükler key değeri olarak kullanılamaz.
    - Sözlüklerde key değerleri sıralı değildir.
    - Sözlüklerde index kullanılamaz.
    - Sözlüklerde key değerleri unique ve immutable olmak zorunda olduğu için hash fonksiyonlarından geçirilirler.
    - Sözlüklerde key değerleri string, integer ve tuple olabilir.
    - Sözlüklerde value değerleri list, set, dict, tuple, int, str, float, boolean, None olabilir.
    - Sözlüklerde key değerleri değişmez. Value değerleri değişebilir.
    - Sözlüklerde key değerleri indexlenemez. Value değerleri indexlenebilir.
    - Sözlüklerde key değerleri ile value değerleri arasında bir ilişki vardır. Bu ilişkiyi kurmak için key değerleri kullanılır.

'''
print("\n1. Sözlük Oluşturma")
print("\n 1. Yöntem")
print("boş sözlük oluşturma")
print("sözlük = {}")
sozluk = {}
print(sozluk)

print("\n2. Yöntem")
print("dict fonksiyonu ile sözlük oluşturma")
print("sözlük = dict()")
sozluk = dict()
print(sozluk)

print("\n3. Yöntem")
print("key-value (anahtar-değer) yapısına sahip sözlük oluşturma")
print("sözlük = {\"bir\":1, \"iki\":2, \"üç\":3}")
sozluk = {"bir":1, "iki":2, "üç":3}
print(sozluk)

print("\n4. Yöntem")
print("dict fonksiyonu ile key-value (anahtar-değer) yapısına sahip sözlük oluşturma")
print("sözlük = dict(bir=1, iki=2, üç=3)")
sozluk = dict(bir=1, iki=2, üç=3)
print(sozluk)

print("\n5. Yöntem")
print("dict fonksiyonu ile liste kullanarak sözlük oluşturma")
print("sözlük = dict([(1,\"bir\"), (2,\"iki\"), (3,\"üç\")])")
sozluk = dict([(1,"bir"), (2,"iki"), (3,"üç")])
print(sozluk)

print("\n6. Yöntem")
print("zip fonksiyonu iki listeyi birleştirerek bir tuple listesi oluşturma.")
print("sözlük = dict(zip([1,2,3],[\"bir\",\"iki\",\"üç\"]))")
sozluk = dict(zip([1,2,3],["bir","iki","üç"]))
print(sozluk)

print("\n2. Sözlük Elemanlarına Erişme")
print("indeks kullanarak sözlük elemanlarına erişme")
print("sözlük[\"bir\"]")
print(sozluk[1])

print("\nget fonksiyonu ile sözlük elemanlarına erişme")
print("sözlük.get(\"bir\")")
print(sozluk.get("bir"))

print("\n3.Sözlük elemanlarını güncelleme")
print("key değeri ile sözlük elemanlarını güncelleme")
print("sözlük[\"bir\"] = 1")
sozluk["bir"] = 1
print(sozluk)

print("\nupdate fonksiyonu ile sözlük elemanlarını güncelleme")
print("sözlük.update({\"bir\":1})")
sozluk.update({"bir":1})
print(sozluk)

print("\n4. Sözlüğe yeniden atama")
print("Sözlüğün içeriğini değiştirmek için yeniden atama")
print("sözlük = {1:\"bir\", 2:\"iki\", 3:\"üç\"}")
sozluk = {1:"bir", 2:"iki", 3:"üç"}
print(sozluk)

print("\n5. Sözlük elemanlarını silme")
print("del sözlük[1]")
del sozluk[1]
print(sozluk)

print("pop fonksiyonu ile sözlük elemanlarını silme")
print("sözlük.pop(2)")
sozluk.pop(2)
print(sozluk)

print("\npopitem fonksiyonu ile sözlük elemanlarını silme")
print("sözlük.popitem()")
sozluk.popitem()
print(sozluk)

print("\nclear fonksiyonu ile sözlük elemanlarını silme")
print("sözlük.clear()")
sozluk.clear()
print(sozluk)

print("\ndel fonksiyonu ile sözlük elemanlarını silme")
print("del sözlük")
del sozluk
#print(sozluk)

sozluk = {1:"bir", 2:"iki", 3:"üç"}

print("\n6. Sözlük Fonksiyonları")
print("\nsorted() fonksiyonu")
print("sorted(sözlük)")
print("sorted fonksiyonu sözlükteki key değerlerini sıralar.")
print(sorted(sozluk))

print("\nany() fonksiyonu")
print("any(sözlük)")
print("any fonksiyonu sözlükteki key değerlerinden herhangi biri True ise True değerini döndürür.")
print(any(sozluk))

print("\nall() fonksiyonu")
print("all(sözlük)")
print("all fonksiyonu sözlükteki key değerlerinin hepsi True ise True değerini döndürür.")
print(all(sozluk))

print("\nlen() fonksiyonu")
print("len(sözlük)")
print("len fonksiyonu sözlükteki key değerlerinin sayısını döndürür.")
print(len(sozluk))

print("\nkeys() fonksiyonu")
print("keys fonksiyonu sözlükteki key değerlerini döndürür.")
print("sözlük.keys()")
print(sozluk.keys())

print("\nvalues() fonksiyonu")
print("sözlük.values()")
print("values fonksiyonu sözlükteki value değerlerini döndürür.")
print(sozluk.values())

print("\nitems() fonksiyonu")
print("sözlük.items()")
print("items fonksiyonu sözlükteki key ve value değerlerini döndürür.")
print(sozluk.items())

print("\nget() fonksiyonu")
print("sözlük.get(1)")
print("get fonksiyonu sözlükteki key değerine karşılık gelen value değerini döndürür.")
print(sozluk.get(1))

print("\nsetdefault() fonksiyonu")
print("sözlük.setdefault(1)")
print("setdefault fonksiyonu sözlükteki key değerine karşılık gelen value değerini döndürür.")
print(sozluk.setdefault(1))

print("\ncopy() fonksiyonu")
print("sözlük.copy()")
print("copy fonksiyonu sözlüğün kopyasını döndürür.")
print(sozluk.copy())

print("\nfromkeys() fonksiyonu")
print("sözlük.fromkeys([1,2,3])")
print("fromkeys fonksiyonu sözlük oluşturur.")
print(sozluk.fromkeys([1,2,3]))

print("\nDiğer sözlük operasyonları")
print("1. Sözlük İçinde Sözlük")
print("sözlük = {1:{\"bir\":1, \"iki\":2, \"üç\":3}, 2:{\"dört\":4, \"beş\":5, \"altı\":6}}")
sozluk = {1:{"bir":1, "iki":2, "üç":3}, 2:{"dört":4, "beş":5, "altı":6}}
print(sozluk)

print("\n2. Sözlük İçinde Liste")
print("sözlük = {1:[1,2,3], 2:[4,5,6]}")
sozluk = {1:[1,2,3], 2:[4,5,6]}
print(sozluk)

print("\n3. Sözlük İçinde Tuple")
print("sözlük = {1:(1,2,3), 2:(4,5,6)}")
sozluk = {1:(1,2,3), 2:(4,5,6)}
print(sozluk)

print("\n4. Sözlük İçinde Set")
print("sözlük = {1:{1,2,3}, 2:{4,5,6}}")
sozluk = {1:{1,2,3}, 2:{4,5,6}}
print(sozluk)

print("\n5. Sözlük İçinde Dict")
print("sözlük = {1:{1:\"bir\", 2:\"iki\", 3:\"üç\"}, 2:{4:\"dört\", 5:\"beş\", 6:\"altı\"}}")
sozluk = {1:{1:"bir", 2:"iki", 3:"üç"}, 2:{4:"dört", 5:"beş", 6:"altı"}}
print(sozluk)

print("\n6. Sözlük İçinde String")
print("sözlük = {1:\"bir\", 2:\"iki\", 3:\"üç\"}")
sozluk = {1:"bir", 2:"iki", 3:"üç"}
print(sozluk)

print("\n7. Sözlük İçinde Integer")
print("sözlük = {1:1, 2:2, 3:3}")
sozluk = {1:1, 2:2, 3:3}
print(sozluk)

print("\n8. Sözlük İçinde Float")
print("sözlük = {1:1.0, 2:2.0, 3:3.0}")
sozluk = {1:1.0, 2:2.0, 3:3.0}
print(sozluk)

print("\n9. Sözlük İçinde Boolean")
print("sözlük = {1:True, 2:False, 3:True}")
sozluk = {1:True, 2:False, 3:True}
print(sozluk)

print("\n10. Sözlük İçinde None")
print("sözlük = {1:None, 2:None, 3:None}")
sozluk = {1:None, 2:None, 3:None}
print(sozluk)

print("\n11. Sözlük İçinde Karışık Veri Yapıları")
print("sözlük = {1:{1:\"bir\", 2:\"iki\", 3:\"üç\"}, 2:[4,5,6], 3:(7,8,9), 4:{10,11,12}, 5:\"beş\", 6:6, 7:7.0, 8:True, 9:None}")
sozluk = {1:{1:"bir", 2:"iki", 3:"üç"}, 2:[4,5,6], 3:(7,8,9), 4:{10,11,12}, 5:"beş", 6:6, 7:7.0, 8:True, 9:None}
print(sozluk)

print("\n12. Sözlük İçinde Karışık Veri Yapılarına Erişme")
print("sözlük[1][1]")
print(sozluk[1][1])

print("\n13. Sözlük İçinde Karışık Veri Yapılarına Ekleme")
print("sözlük[1][4] = \"dört\"")
sozluk[1][4] = "dört"
print(sozluk)

print("\n14. Sözlük İçinde Karışık Veri Yapılarından Silme")
print("del sözlük[1][4]")
del sozluk[1][4]

print("\n15. Sözlük İçinde Karışık Veri Yapılarından Güncelleme")
print("sözlük[1][1] = \"Bir\"")
sozluk[1][1] = "Bir"
print(sozluk)