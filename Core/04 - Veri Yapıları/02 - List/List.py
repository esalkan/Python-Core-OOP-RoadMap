'''
"list" Veri Türü
    Python, Java ve C++'ın aksine array veri yapısına sahip değildir. Python'da array, list veri yapısı ile uygulanır.
    "list" yapısı, "tuple" veri yapısından farklı olarak
        mutable (değiştirilebilir)
        eleman ekleme,
        silme
        yerlerini değiştirme
    özelliği bulunan yapıdır.

    "tuple"da olduğu gibi "list" veri türünde farklı tipte verilerin bir arada tutulması mümkündür.

     List veri yapısını oluşturmak için virgülle ayrılmış elemanları köşeli parantez [] içinde belirtmeniz gerekir.
        meyveler = ["elma", "armut", "çilek"]
        sayılar = [1, 2, 3, 4, 5]
        karışık = [1, "elma", 3.14, True]

     Python yorumlayıcısı dinamik olarak her veri yapısını belirleyecek yeteneklere sahiptir.
     Bu nedenle list veri yapısında farklı tipte verileri bir arada tutmak mümkündür.
        liste = [1, "elma", 3.14, True]

'''

# Python'da list() yaratmak için 3 farklı yol vardır.
print("\nPython'da list() yaratmak için 3 farklı yol vardır.")
print("Yöntem 1: liste = list()")
# 1. Yöntem
liste = list()
print("list(): ",liste)

# 2. Yöntem
print("\nYöntem 2: liste = []")
liste = []
print("Liste[] ",liste)

# 3. Yöntem
print("\nYöntem 3: liste = [1, 2, 3, 4, 5]")
liste = [1, 2, 3, 4, 5]
print("Liste = ", liste)

# Listelerdeki elemanlara erişmek için index kullanılır.
# Listelerde indexler 0'dan başlar.
# Listelerde indexler negatif olabilir.

print("\nliste = [1, 2, 3, 4, 5]")
liste = [1, 2, 3, 4, 5]
print(liste[0])  # 1
print(liste[4])  # 5
print(liste[-1])  # 5
print(liste[-5])  # 1

# Python'da bir list()'in yeniden atanması mümkündür.
print("\nPython'da bir list()'in yeniden atanması")
print("liste = [1, 2, 3, 4, 5] \nliste = [6, 7, 8, 9, 10]")
liste = [1, 2, 3, 4, 5]
liste = [6, 7, 8, 9, 10]
print(liste)  # [6, 7, 8, 9, 10]

# Python'da bir list()'in elemanlarının değiştirilmesi mümkündür.
print("\nPython'da bir list()'in elemanlarının değiştirilmesi")
print("liste = [1, 2, 3, 4, 5] \nliste[0] = 6")
liste = [1, 2, 3, 4, 5]
liste[0] = 6
print(liste)  # [6, 2, 3, 4, 5]

# Python'da bir list()'in elemanlarının silinmesi mümkündür.
print("\nPython'da bir list()'in elemanlarının silinmesi")
print("liste = [1, 2, 3, 4, 5] \ndel liste[0]")
liste = [1, 2, 3, 4, 5]
del liste[0]
print(liste)  # [2, 3, 4, 5]

# Python'da list() fonksiyonları
print("\nPython'da list() fonksiyonları")

print("\nappend() fonksiyonu, listeye eleman eklemek için kullanılır.")
print("The append() function is used to add elements to the list.")
liste = [1, 2, 3, 4, 5]
liste.append(6)
print(liste)  # [1, 2, 3, 4, 5, 6]

print("\ninsert() fonksiyonu, listeye eleman eklemek için kullanılır.")
print("The insert() function is used to add elements to the list.")
liste = [1, 2, 3, 4, 5]
liste.insert(0, 6)
print(liste)  # [6, 1, 2, 3, 4, 5]

print("\nremove() fonksiyonu, listeden eleman silmek için kullanılır.")
print("The remove() function is used to delete an item from the list.")
liste = [1, 2, 3, 4, 5]
liste.remove(1)
print(liste)  # [2, 3, 4, 5]

print("\npop() fonksiyonu, listeden eleman silmek için kullanılır.")
print("The pop() function is used to delete an item from the list.")
liste = [1, 2, 3, 4, 5]
liste.pop(0)
print(liste)  # [2, 3, 4, 5]

print("\nindex() fonksiyonu, listedeki elemanın indexini bulmak için kullanılır.")
print("The index() function is used to find the index of the element in the list.")
liste = [1, 2, 3, 4, 5]
print(liste.index(1))  # 0

print("\ncount() fonksiyonu, listedeki elemanın kaç defa geçtiğini bulmak için kullanılır.")
print("The count() function is used to find how many times the element in the list is passed.")
liste = [1, 2, 3, 4, 5, 1, 1, 1]
print(liste.count(1))  # 4

print("\nsort() fonksiyonu, listeyi sıralamak için kullanılır.")
print("The sort() function is used to sort the list.")
liste = [5, 4, 3, 2, 1]
liste.sort()
print(liste)  # [1, 2, 3, 4, 5]

print("\nreverse() fonksiyonu, listeyi ters çevirmek için kullanılır.")
print("The reverse() function is used to reverse the list.")
liste = [1, 2, 3, 4, 5]
liste.reverse()
print(liste)  # [5, 4, 3, 2, 1]

print("\ncopy() fonksiyonu, listeyi kopyalamak için kullanılır.")
print("The copy() function is used to copy the list.")
liste = [1, 2, 3, 4, 5]
liste2 = liste.copy()
print(liste2)  # [1, 2, 3, 4, 5]

print("\nclear() fonksiyonu, listeyi temizlemek için kullanılır.")
print("The clear() function is used to clear the list.")
liste = [1, 2, 3, 4, 5]
liste.clear()
print(liste)  # []

print("\nextend() fonksiyonu, listeye eleman eklemek için kullanılır.")
print("The extend() function is used to add elements to the list.")
liste = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10]
liste.extend(liste2)
print(liste)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nlen() fonksiyonu, listenin eleman sayısını bulmak için kullanılır.")
print("The len() function is used to find the number of elements in the list.")
liste = [1, 2, 3, 4, 5]
print(len(liste))  # 5

print("\nmin() fonksiyonu, listenin en küçük elemanını bulmak için kullanılır.")
print("The min() function is used to find the smallest element of the list.")
liste = [1, 2, 3, 4, 5]
print(min(liste))  # 1

print("\nmax() fonksiyonu, listenin en büyük elemanını bulmak için kullanılır.")
print("The max() function is used to find the largest element of the list.")
liste = [1, 2, 3, 4, 5]
print(max(liste))  # 5

print("\nsum() fonksiyonu, listenin elemanlarının toplamını bulmak için kullanılır.")
print("The sum() function is used to find the total of the elements in the list.")
liste = [1, 2, 3, 4, 5]
print(sum(liste))  # 15

print("\nlist() fonksiyonu, str bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a str expression to a list.")
liste = list("Python")
print(liste)  # ['P', 'y', 't', 'h', 'o', 'n']

print("\nlist() fonksiyonu, tuple bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a tuple expression to a list.")
liste = list((1, 2, 3, 4, 5))
print(liste)  # [1, 2, 3, 4, 5]

print("\nlist() fonksiyonu, range bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a range expression to a list.")
liste = list(range(1, 6))
print(liste)  # [1, 2, 3, 4, 5]

print("\nlist() fonksiyonu, set bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a set expression to a list.")
liste = list({1, 2, 3, 4, 5})
print(liste)  # [1, 2, 3, 4, 5]

print("\nlist() fonksiyonu, dict bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a dict expression to a list.")
liste = list({"bir": 1, "iki": 2, "üç": 3, "dört": 4, "beş": 5})
print(liste)  # ['bir', 'iki', 'üç', 'dört', 'beş']

print("\nlist() fonksiyonu, list bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a list expression to a list.")
liste = list((i for i in range(1, 6)))
print(liste)  # [1, 2, 3, 4, 5]

print("\nlist() fonksiyonu, filter bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a filter expression to a list.")
liste = list(filter(lambda x: x > 5, range(1, 11)))
print(liste)  # [6, 7, 8, 9, 10]

print("\nlist() fonksiyonu, map bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a map expression to a list.")
liste = list(map(lambda x: x * 2, range(1, 6)))
print(liste)  # [2, 4, 6, 8, 10]

print("\nlist() fonksiyonu, zip bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a zip expression to a list.")
liste = list(zip(range(1, 6), range(6, 11)))
print(liste)  # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

print("\nlist() fonksiyonu, enumerate bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert an enumerate expression to a list.")
liste = list(enumerate(range(1, 6)))
print(liste)  # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print("\nlist() fonksiyonu, reversed bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a reversed expression to a list.")
liste = list(reversed(range(1, 6)))
print(liste)  # [5, 4, 3, 2, 1]

print("\nlist() fonksiyonu, sorted bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert a sorted expression to a list.")
liste = list(sorted(range(1, 6)))
print(liste)  # [1, 2, 3, 4, 5]

print("\nlist() fonksiyonu, eval bir ifadeyi listeye çevirmek için kullanılır.")
print("The list() function is used to convert an eval expression to a list.")
liste = list(eval("range(1, 6)"))
print(liste)  # [1, 2, 3, 4, 5]
