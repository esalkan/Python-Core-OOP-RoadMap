'''
    İç içe döngüler | Nested loops

     iç içe döngüler, bir döngü içinde başka bir döngü kullanma anlamına gelir.
     Bu, programcılara çeşitli durumları işlemeleri ve daha karmaşık yapılar oluşturmaları için esneklik sağlar.
     İki yaygın iç içe döngü türü for içinde for ve while içinde for'dur.

            - Nested loops mean using another loop within a loop.
            This gives programmers flexibility to process various situations and create more complex structures.
            Two common nested loop types are for in for and while in for.

    ---> for içinde for | for in for <---
         for içinde for döngüsü, bir döngü içinde başka bir döngü kullanma anlamına gelir.
         Bu, programcılara çeşitli durumları işlemeleri ve daha karmaşık yapılar oluşturmaları için esneklik sağlar.

            - for in for loop means using another loop within a loop.
            This gives programmers flexibility to process various situations and create more complex structures.

    ---> while içinde for | while in for <---
        while içinde for döngüsü, bir döngü içinde başka bir döngü kullanma anlamına gelir.
        Bu, programcılara çeşitli durumları işlemeleri ve daha karmaşık yapılar oluşturmaları için esneklik sağlar.

            - while in for loop means using another loop within a loop.
            This gives programmers flexibility to process various situations and create more complex structures.

    ---> for içinde while | for in while <---
        for içinde while döngüsü, bir döngü içinde başka bir döngü kullanma anlamına gelir.
        Bu, programcılara çeşitli durumları işlemeleri ve daha karmaşık yapılar oluşturmaları için esneklik sağlar.

            - for in while loop means using another loop within a loop.
            This gives programmers flexibility to process various situations and create more complex structures.

    ---> while içinde while | while in while <---
        while içinde while döngüsü, bir döngü içinde başka bir döngü kullanma anlamına gelir.
        Bu, programcılara çeşitli durumları işlemeleri ve daha karmaşık yapılar oluşturmaları için esneklik sağlar.

            - while in while loop means using another loop within a loop.
            This gives programmers flexibility to process various situations and create more complex structures.
'''

print("---> for içinde for | for in for <---")
print("Example 1")
for i in range(1, 4): # 1'den 4'e kadar olan sayıları yazdırır. | Prints the numbers from 1 to 4.
    for j in range(1, 4): # 1'den 4'e kadar olan sayıları yazdırır. | Prints the numbers from 1 to 4.
        print(i, j) # i ve j'yi yazdır | Print i and j
print("Program ended | Program sonlandı\n")

print("Example 2")
for i in range(0, 3): # 0'dan 3'e kadar olan sayıları yazdırır. | Prints the numbers from 0 to 3.
    for j in range(0, i + 1):  # 0'dan i'ye kadar olan sayıları yazdırır. | Prints the numbers from 0 to i.
        print ("i : ", i, "j : ", j, sep="\t") # i ve j'yi yazdır | Print i and j
print("Program ended | Program sonlandı\n")

print("---> for içinde while | for in while <---")
print("Example 1")
for i in range(1, 4): # 1'den 4'e kadar olan sayıları yazdırır. | Prints the numbers from 1 to 4.
    j = 1 # Başlangıç değeri | Start value
    while j < 4: # Koşul ve koşul değeri | Condition and condition value
        print(i, j) # i ve j'yi yazdır | Print i and j
        j += 1 # j'yi 1 artır | Increase j by 1
print("Program ended | Program sonlandı\n")

print("---> while içinde while | while in while <---")
print("Example 1")
i = 1 # Başlangıç değeri | Start value
while i < 4: # Koşul ve koşul değeri | Condition and condition value
    j = 1 # Başlangıç değeri | Start value
    while j < 4: # Koşul ve koşul değeri | Condition and condition value
        print(i, j) # i ve j'yi yazdır | Print i and j
        j += 1 # j'yi 1 artır | Increase j by 1
    i += 1 # i'yi 1 artır | Increase i by 1
print("Program ended | Program sonlandı\n")

print("---> while içinde for | while in for <---")
print("Example 1")
i = 1 # Başlangıç değeri | Start value
while i < 4: # Koşul ve koşul değeri | Condition and condition value
    for j in range(1, 4): # 1'den 4'e kadar olan sayıları yazdırır. | Prints the numbers from 1 to 4.
        print(i, j) # i ve j'yi yazdır | Print i and j
    i += 1 # i'yi 1 artır | Increase i by 1
print("Program ended | Program sonlandı\n")



