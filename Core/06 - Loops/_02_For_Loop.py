'''
    Loops (Döngüler)
    Bir dizi talimatı tekrar tekrar çalıştırmak isteyebiliriz. Bu eyleme iterasyon ya da döngü denir.
    Bir koleksiyonun tüm olası durumları veya tüm elemanları üzerinde çalışmak isteyebiliriz.
    Bu durumda da iterasyon ya da döngü kullanırız. Python'da döngüler for ve while olarak ikiye ayrılır.

     Pythonda döngüler for ve while olarak ikiye ayrılır.
        - Loops in Python are divided into two as for and while.

     for döngüsü, belirli bir koşul sağlanana kadar çalışır.
     for döngüsü, bir dizi üzerinde veya bir sayı aralığında çalışabilir.
     for döngüsü, bir dizi üzerinde çalışıyorsa, her bir eleman için döngüyü çalıştırır.
     for döngüsü, bir sayı aralığında çalışıyorsa, belirtilen sayı aralığında döngüyü çalıştırır.

        - The for loop works until a certain condition is met. The for loop can work on an array or in a number range.
        If the for loop is working on an array, it runs the loop for each element. If the for loop is working in a
        number range, it runs the loop in the specified number range.
'''

print("---> For Loop <---")
# Range fonksiyonu, belirtilen sayı aralığında bir dizi oluşturur. Bu dizi, for döngüsü içerisinde kullanılabilir.
# The range function creates an array in the specified number range. This array can be used in the for loop.

# range(start, stop, step)

    # start: Başlangıç değeri
    # stop: Bitiş değeri
    # step: Artış değeri

    # start: Start value
    # stop: End value
    # step: Increment value

print("Example 1")
for i in range(5): # 0'dan 5'e kadar olan sayıları yazdırır. | Prints the numbers from 0 to 5.
    print(i) # i'yi yazdır | Print i
print("Program ended | Program sonlandı\n")

print("Example 2")
for i in range(1, 10): # 1'den 10'a kadar olan sayıları yazdırır. | Prints the numbers from 1 to 10.
    print("Merhaba Dunya", i) # i'yi yazdır | Print i
print("Program ended | Program sonlandı\n")

print("Example 3")
for i in range(1, 10, 2): # 1'den 10'a kadar olan sayıları 2 2 arttırarak yazdırır. | Prints the numbers from 1 to 10 by increasing 2 by 2
    print("Merhaba Dunya", i) # i'yi yazdır | Print i
print("Program ended | Program sonlandı\n")

print("Example 4")
for i in range(10, 1, -2): # 10'dan 1'e kadar olan sayıları 2 2 azaltarak yazdırır. | Prints the numbers from 10 to 1 by decreasing 2 by 2
    print("Merhaba Dunya", i) # i'yi yazdır | Print i
print("Program ended | Program sonlandı\n")

print("Example 5")
for i in range(0,10): # 0'dan 10'a kadar olan sayıları yazdırır. | Prints the numbers from 0 to 10.
    print ("%d sayisinin karesi: %d" % (i, i**2)) # i**2, i'nin karesini hesaplar. | i**2 calculates the square of i.
print("Program ended | Program sonlandı\n")

print("Example 6")
for i in range(21, 32):
    if i % 2 == 1: # Sayi tek mi? | Is the number odd?
        print(i*i) # Sayi tek ise karesini al. | If the number is odd, take the square.
    else: # Sayi cift mi? | Is the number even?
        print(i//2) # Sayi cift ise 2'ye bol. | If the number is even, divide by 2.
print("Program ended | Program sonlandı\n")

print("Example 7")
karisik = ["lorem","ipsum","sit","com","add",
           "sed","do","error","tango","inc","ut"] # Karisik bir dizi olustur. | Create a mixed array.
sesliler = [] # Bos bir dizi olustur. | Create an empty array.
sessizler = [] # Bos bir dizi olustur. | Create an empty array.
for kelime in karisik: # Karisik dizinin elemanlarini tek tek al. | Take the elements of the mixed array one by one.
    if kelime[0] in ['a','e','i','o','u']: # Kelimenin ilk harfi sesli mi? | Is the first letter of the word a vowel?
        sesliler += [kelime] # Kelimeyi sesliler dizisine ekle. | Add the word to the vowels array.
    else: # Kelimenin ilk harfi sessiz mi? | Is the first letter of the word a consonant?
        sessizler += [kelime] # Kelimeyi sessizler dizisine ekle. | Add the word to the consonants array.
print("Sessiz harf ile baslayanlar:", sessizler) # Sessizler dizisini yazdir. | Print the consonants array.
print("Sesli harf ile baslayanlar:", sesliler) # Sesliler dizisini yazdir. | Print the vowels array.
print("Program ended | Program sonlandı\n")
