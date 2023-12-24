'''
    Break and Continue Statements | Devam ve Döngüyü Kırma İfadeleri
    Döngülerde bazı durumlarda döngüyü kırmak veya devam etmek isteyebiliriz. Bu durumda break ve continue ifadelerini kullanırız.
    break ifadesi, döngüyü kırar ve döngüden çıkar.
    continue ifadesi, döngüyü kırar ve döngüye devam eder.

        - We may want to break or continue the loop in some cases in loops. In this case, we use the break and continue statements.
        The break statement breaks the loop and exits the loop.
        The continue statement breaks the loop and continues the loop.

    break ifadesi, döngüyü kırar ve döngüden çıkar.
    continue ifadesi, döngüyü kırar ve döngüye devam eder.

        - The break statement breaks the loop and exits the loop.
        The continue statement breaks the loop and continues the loop.

    Yazım kuralları | Writing rules
        - break ve continue ifadeleri, sadece döngülerde kullanılabilir.
        - break and continue statements can only be used in loops.

    Örnekler | Examples
        for <variable> in <sequence>:
            if <condition>: break # Döngüyü kırar ve döngüden çıkar | Breaks the loop and exits the loop
            if <condition>: continue # Döngüyü kırar ve döngüye devam eder | Breaks the loop and continues the loop

        while <condition>:
            if <condition>: break # Döngüyü kırar ve döngüden çıkar | Breaks the loop and exits the loop
            if <condition>: continue # Döngüyü kırar ve döngüye devam eder | Breaks the loop and continues the loop

    Nested example | İç içe örnek
        for <variable> in <sequence>:
            for <variable> in <sequence>:
                if <condition>: break # Döngüyü kırar ve döngüden çıkar | Breaks the loop and exits the loop
                if <condition>: continue # Döngüyü kırar ve döngüye devam eder | Breaks the loop and continues the loop
            if <condition>: break # Döngüyü kırar ve döngüden çıkar | Breaks the loop and exits the loop
            if <condition>: continue # Döngüyü kırar ve döngüye devam eder | Breaks the loop and continues the loop
        if <condition>: break # Döngüyü kırar ve döngüden çıkar | Breaks the loop and exits the loop
        if <condition>: continue # Döngüyü kırar ve döngüye devam eder | Breaks the loop and continues the loop

        while <condition>:
            while <condition>:
                if <condition>: break # Döngüyü kırar ve döngüden çıkar | Breaks the loop and exits the loop
                if <condition>: continue  # Döngüyü kırar ve döngüye devam eder | Breaks the loop and continues the loop
            if <condition>: break # Döngüyü kırar ve döngüden çıkar | Breaks the loop and exits the loop
            if <condition>: continue # Döngüyü kırar ve döngüye devam eder | Breaks the loop and continues the loop
'''

print("---> Break Statement | Break İfadesi <---")
print("Example 1")
# for döngüsünde break kullanımı | break usage in for loop
for i in range(5): # Koşul ve koşul değeri | Condition and condition value
    if i == 3: # Koşul ve koşul değeri | Condition and condition value
        break # For döngüsünden tamamen çıkar | Exit completely from the for loop
    print(i) # i'yi yazdır | Print i
print("Program ended | Program sonlandı\n")

print("Example 2")
# while döngüsünde break kullanımı | break usage in while loop
i = 0 # Başlangıç değeri | Start value
while i < 5: # Koşul ve koşul değeri | Condition and condition value
    if i == 3: # Koşul ve koşul değeri | Condition and condition value
        break # While döngüsünden tamamen çıkar | Exit completely from the while loop
    print(i) # i'yi yazdır | Print i
    i += 1 # i'yi 1 artır | Increase i by 1
print("Program ended | Program sonlandı\n")

print("Example 3")
i = 4
while i < 1000: # Koşul ve koşul değeri | Condition and condition value
    if i == 10: # Koşul ve koşul değeri | Condition and condition value
        break # while dongusunden tamamen cik, `print "bitti"` satirina atla
    ara_deger = i // 2 # ara_deger = i'nin 2'ye bolumunden kalan
    ara_deger = ara_deger + 3 # ara_deger = ara_deger + 3
    print (ara_deger) # ara_deger'i yazdir
    i = i + 1 # i'yi 1 artır | Increase i by 1

print("bitti") # yukaridaki break deyimi calistirildiginda yurutme buraya sicrar
print("Program ended | Program sonlandı\n")
