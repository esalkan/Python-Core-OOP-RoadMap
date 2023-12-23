'''
    set (küme), içinde bir dizi değeri barındırır. Sıralıdır ancak indekslemeyi desteklemez.
    Bir küme yaratmak için, { } parantezlerinin içine virgülle ayrılmış bir dizi öğe yazmamız gerekir.
    Bundan sonra da her zamanki gibi onu bir Python değişkenine atamalıyız.
    Bir küme tıpkı list[], tuple() ve dict{} veri yapılarında olduğu gibi içinde farklı veri türlerini barındırabilir.

    Python'da setler, matematikteki kümelerin karşılığıdır.
        Setler, birbirinden farklı elemanları içinde barındırır.
        Setlerde sıralama yoktur.
        Setlerde indexleme yoktur.
        Setlerde key-value yapısı yoktur.
        Setlerde elemanlar değiştirilebilir.
        Setlerde elemanlar tekrar edemez.
'''

print("\n1. Set Oluşturma")
print("1. Yöntem")
print("boş set oluşturma")
print("set = set()")
sett = set()
print(sett)

print("\n2. Yöntem")
print("set fonksiyonu ile set oluşturma")
print("set = set([1,2,3])")
sett = set([1,2,3])
print(sett)

print("\n3. Yöntem")
print("set fonksiyonu ile set oluşturma")
print("set = set((1,2,3))")
sett = set((1,2,3))
print(sett)

print("\n4. Yöntem")
print("set fonksiyonu ile set oluşturma")
print("set = set(\"Python\")")
sett = set("Python")
print(sett)

print("\n2. Set Elemanlarına Erişme")
print("for döngüsü ile set elemanlarına erişme")
print("for i in set:")
print("    print(i)")
for i in sett:
    print(i)

print("\nin operatörü ile varlık kontrolü")
print("1 in set")
print(1 in sett)

print("\nif 1 in set:")
print("    print(\"1 set içinde\")")
if 1 in sett:
    print("1 set içinde")


print("\n3. Set Elemanlarını günceleme")
print("add fonksiyonu ile set elemanlarına ekleme")
print("set.add(4)")
sett.add(4)
print(sett)

print("\nupdate fonksiyonu ile set elemanlarına ekleme")
print("set.update([5,6,7])")
sett.update([5,6,7])
print(sett)

print("\ndiscard fonksiyonu ile set elemanları silme")
print("set.discard(7)")
sett.discard(7)
print(sett)

print("\nremove fonksiyonu ile set elemanları silme")
print("set.remove(6)")
sett.remove(6)
print(sett)

print("\n4. Set Elemanlarını silme")
print("set.clear()")
sett.clear()
print(sett)

print("\n5. Setlerde Matematiksel İşlemler")
print("set1 = set([1,2,3])")
set1 = set([1,2,3])
print(set1)
print("set2 = set([2,3,4])")
set2 = set([2,3,4])
print(set2)
print("set1 | set2")
print(set1 | set2)
print("set1 & set2")
print(set1 & set2)
print("set1 - set2")
print(set1 - set2)
print("set2 - set1")
print(set2 - set1)
print("set1 ^ set2")
print(set1 ^ set2)
print("set1 <= set2")
print(set1 <= set2)
print("set1 >= set2")
print(set1 >= set2)
print("set1 < set2")
print(set1 < set2)
print("set1 > set2")
print(set1 > set2)

print("\n6. Set Fonksiyonları")
print("\nunion fonksiyonu")
print("union fonksiyonu iki kümenin birleşimini döndürür")
print("set1.union(set2)")
print(set1.union(set2))

print("\nintersection fonksiyonu")
print("intersection fonksiyonu iki kümenin kesişimini döndürür")
print("set1.intersection(set2)")
print(set1.intersection(set2))

print("\ndifference fonksiyonu")
print("difference fonksiyonu iki kümenin farkını döndürür")
print("set1.difference(set2)")
print(set1.difference(set2))

print("\nsymmetric_difference fonksiyonu")
print("symmetric_difference fonksiyonu iki kümenin simetrik farkını döndürür")
print("set1.symmetric_difference(set2)")
print(set1.symmetric_difference(set2))

print("\nisdisjoint fonksiyonu")
print("isdisjoint fonksiyonu iki kümenin kesişiminin boş olup olmadığını kontrol eder")
print("set1.isdisjoint(set2)")
print(set1.isdisjoint(set2))

print("\nissubset fonksiyonu")
print("issubset fonksiyonu bir kümenin başka bir kümenin alt kümesi olup olmadığını kontrol eder")
print("set1.issubset(set2)")
print(set1.issubset(set2))

print("\nissuperset fonksiyonu")
print("issuperset fonksiyonu bir kümenin başka bir kümenin üst kümesi olup olmadığını kontrol eder")
print("set1.issuperset(set2)")
print(set1.issuperset(set2))

print("\ncopy fonksiyonu")
print("copy fonksiyonu setin kopyasını döndürür")
print("set1.copy()")
print(set1.copy())

print("\ndifference_update fonksiyonu")
print("difference_update fonksiyonu iki kümenin farkını döndürür")
print("set1.difference_update(set2)")
print(set1.difference_update(set2))

print("\nintersection_update fonksiyonu")
print("intersection_update fonksiyonu iki kümenin kesişimini döndürür")
print("set1.intersection_update(set2)")
print(set1.intersection_update(set2))

print("\nsymmetric_difference_update fonksiyonu")
print("symmetric_difference_update fonksiyonu iki kümenin simetrik farkını döndürür")
print("set1.symmetric_difference_update(set2)")
print(set1.symmetric_difference_update(set2))

print("\nupdate fonksiyonu")
print("update fonksiyonu iki kümenin birleşimini döndürür")
print("set1.update(set2)")
print(set1.update(set2))

print("\nDiğer set operasyonları")
print("1. Set İçinde Set")
print("set = {1:{1,2,3}, 2:{4,5,6}}")
sett = {1:{1,2,3}, 2:{4,5,6}}
print(sett)

print("\n2. Set İçinde Liste")
print("set = {1:[1,2,3], 2:[4,5,6]}")
sett = {1:[1,2,3], 2:[4,5,6]}
print(sett)

print("\n3. Set İçinde Tuple")
print("set = {1:(1,2,3), 2:(4,5,6)}")
sett = {1:(1,2,3), 2:(4,5,6)}
print(sett)

print("\n4. Set İçinde Dict")
print("set = {1:{1:\"bir\", 2:\"iki\", 3:\"üç\"}, 2:{4:\"dört\", 5:\"beş\", 6:\"altı\"}}")
sett = {1:{1:"bir", 2:"iki", 3:"üç"}, 2:{4:"dört", 5:"beş", 6:"altı"}}
print(sett)

print("\n5. Set İçinde String")
print("set = {1:\"bir\", 2:\"iki\", 3:\"üç\"}")
sett = {1:"bir", 2:"iki", 3:"üç"}
print(sett)

print("\n6. Set İçinde Integer")
print("set = {1:1, 2:2, 3:3}")
sett = {1:1, 2:2, 3:3}
print(sett)

print("\n7. Set İçinde Float")
print("set = {1:1.0, 2:2.0, 3:3.0}")
sett = {1:1.0, 2:2.0, 3:3.0}
print(sett)

print("\n8. Set İçinde Boolean")
print("set = {1:True, 2:False, 3:True}")
sett = {1:True, 2:False, 3:True}
print(sett)

print("\n9. Set İçinde None")
print("set = {1:None, 2:None, 3:None}")
sett = {1:None, 2:None, 3:None}
print(sett)

print("\n10. Set İçinde Set")
print("set = {1:{1,2,3}, 2:{4,5,6}}")
sett = {1:{1,2,3}, 2:{4,5,6}}
print(sett)

print("\n11. Set İçinde Liste")
print("set = {1:[1,2,3], 2:[4,5,6]}")
sett = {1:[1,2,3], 2:[4,5,6]}
print(sett)

print("\n12. Set İçinde Tuple")
print("set = {1:(1,2,3), 2:(4,5,6)}")
sett = {1:(1,2,3), 2:(4,5,6)}
print(sett)

print("\n13. Set İçinde Dict")
print("set = {1:{1:\"bir\", 2:\"iki\", 3:\"üç\"}, 2:{4:\"dört\", 5:\"beş\", 6:\"altı\"}}")
sett = {1:{1:"bir", 2:"iki", 3:"üç"}, 2:{4:"dört", 5:"beş", 6:"altı"}}
print(sett)