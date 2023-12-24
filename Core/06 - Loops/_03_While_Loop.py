'''
    Loops (Döngüler)
    Bir dizi talimatı tekrar tekrar çalıştırmak isteyebiliriz. Bu eyleme iterasyon ya da döngü denir.
    Bir koleksiyonun tüm olası durumları veya tüm elemanları üzerinde çalışmak isteyebiliriz.
    Bu durumda da iterasyon ya da döngü kullanırız. Python'da döngüler for ve while olarak ikiye ayrılır.

     Pythonda döngüler for ve while olarak ikiye ayrılır.
        - Loops in Python are divided into two as for and while.

    while döngüsü, belirli bir koşul sağlanana kadar çalışır.
    while döngüsü, bir dizi üzerinde veya bir sayı aralığında çalışabilir.
    while döngüsü, bir dizi üzerinde çalışıyorsa, her bir eleman için döngüyü çalıştırır.
    while döngüsü, bir sayı aralığında çalışıyorsa, belirtilen sayı aralığında döngüyü çalıştırır.

        - The while loop works until a certain condition is met. The while loop can work on an array or in a number range.
        If the while loop is working on an array, it runs the loop for each element. If the while loop is working in a
        number range, it runs the loop in the specified number range.

    for döngüsünden farklı olarak while döngüsünde bir şartın doğruluğu devam edene kadar blok içerisindeki kodlar çalışır.
    while döngüsü, belirli bir koşul sağlanana kadar çalışır. Koşul sağlanmazsa, while döngüsü çalışmaz.
    while döngüsünde ayrıca bir sayaç değişkeni kullanılabilir. Bu değişken, döngünün kaç kez çalıştığını tutar.
    while döngüsünde sayaç değişkeni kullanılıyorsa, döngü içerisinde sayaç değişkeninin değeri artırılmalıdır.

    "Bir while döngüsü", kendisinden sonra bir else ifadesine sahip olabilir.
    Koşul yanlış olduğunda, else ifadesinin altındaki blok yürütülür.
    Ancak, break deyimi ile döngüden ayrılırsanız  veya return deyimi kullanırsanız else bloğu çalıştırılmaz.
    Döngü çalışırken herhangi bir aşamada döngüden çıkmak ya da döngüyü sonlandırmak için "break" deyimini kullanırız.

        - Unlike the for loop, the code in the block continues to run until the truth of a condition is met in the while loop.
        The while loop works until a certain condition is met. If the condition is not met, the while loop does not work.
        A counter variable can also be used in the while loop. This variable holds how many times the loop has run.
        If a counter variable is used in the while loop, the value of the counter variable should be increased in the loop.

        "A while loop" can have an else statement after it.
        When the condition is false, the block under the else statement is executed.
        However, if you exit the loop with the break statement or use the return statement, the else block is not executed.
        We use the "break" statement to exit the loop or terminate the loop at any stage while the loop is running.
'''

print("---> While Loop <---")
print("Example 1")
i = 4 # Başlangıç değeri | Start value
while i > 1: # Koşul ve koşul değeri | Condition and condition value
    print(i) # i'yi yazdır | Print i
    i = i - 1 # i'yi 1 azalt | Decrease i by 1
print("Program ended | Program sonlandı\n")

print("Example 2")
i = 1 # Başlangıç değeri | Start value
while i < 10: # Koşul ve koşul değeri | Condition and condition value
    print("Merhaba Dunya", i) # i'yi yazdır | Print i
    i = i + 1 # i'yi 1 artır | Increase i by 1
print("Program ended | Program sonlandı\n")

print("Example 3")
L = [10, 5, 15, 25, 0] # Bir dizi oluştur | Create an array
N = len(L) # Dizinin uzunluğunu hesapla | Calculate the length of the array
i = 0 # Başlangıç değeri | Start value
total = 0 # Toplam değeri | Total value
while i < N: # Koşul ve koşul değeri | Condition and condition value
    total = total + L[i] # Toplam değerine dizinin i. elemanını ekle | Add the i. element of the array to the total value
    i = i + 1 # i'yi 1 artır | Increase i by 1
avg = total / N # Ortalama değerini hesapla | Calculate the average value
print(total) # Toplam değerini yazdır | Print the total value
print(avg) # Ortalama değerini yazdır | Print the average value
print("Program ended | Program sonlandı\n")

print("\n---> While else Loop <---")
print("Example 1")
# While'da else kullanımı | While else usage
i = 1 # Başlangıç değeri | Start value
while i < 10: # Koşul ve koşul değeri | Condition and condition value
    print("Merhaba Dunya", i) # i'yi yazdır | Print i
    i = i + 1 # i'yi 1 artır | Increase i by 1
else: # Koşul sağlanmazsa çalışır | Works if the condition is not met
    print("Döngü bitti")
print("Program ended | Program sonlandı\n")

print("Example 4")
a = 3 # Başlangıç değeri | Start value
while a > 0: # Koşul ve koşul değeri | Condition and condition value
    print(a) # a'yı yazdır | Print a
    a -=1 # a'yı 1 azalt | Decrease a by 1
    if a == 1: break; # a 1'e eşitse döngüden çık | If a is equal to 1, exit the loop
else: # Koşul sağlanmazsa çalışır | Works if the condition is not met
    print("0 sayisina ulasildi") # 0 sayısına ulaşıldığında yazdır | Print when 0 is reached
print("Program ended | Program sonlandı\n")

print("\n--->Single Line While Loop | Tek Satır While Loop<---")
# Tek satır while döngüsü kullanımı mümükündür. | Single line while loop usage is possible.
# while koşul: işlem
# while condition: process
print("Example 1")
i = 1 # Başlangıç değeri | Start value
while i < 10: print(i); i += 1 # i'yi yazdır ve 1 artır | Print i and increase by 1
print("Program ended | Program sonlandı\n")

print("Example 2")
i = 1 # Başlangıç değeri | Start value
while i < 10: print("Merhaba Dunya", i); i += 1 # i'yi yazdır ve 1 artır | Print i and increase by 1
print("Program ended | Program sonlandı\n")




