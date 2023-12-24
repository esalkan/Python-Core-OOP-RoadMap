'''

    Programlama dilinde en önemli şeylerden biri karar verme yeteneğidir.
        - One of the most important things in programming is the ability to make decisions.

    Python'da karar vermek için if ifadesini kullanırız.
        - In Python, we use the if statement to make decisions.

    Bazen, bir programda, bir karşılaştırma sonucuna göre karar vermek isteyebiliriz.
    Bir ifadenin değerinin "Doğru (True)" veya "Yanlış (False)" olabileceğini biliyoruz ve programımızı bu değerlere
    göre şekillendirebiliriz. Örneğin, elimizde x ve y isimli iki değişken olduğunu varsayalım. x, y'den daha büyükse,
    “x, y'den daha büyüktür” yazdırmak istiyoruz. Eğer y, x'den büyükse, “y, x'den daha büyük” yazdırmak istiyoruz.
    İşte bu tür karar verme durumlarında if ifadelerini kullanıyoruz.

        - Sometimes, in a program, we may want to make a decision based on the result of a comparison.
        We know that the value of an expression can be either "True" or "False" and we can shape our program according to
        these values. For example, suppose we have two variables x and y. If x is greater than y, we want to print
        "x is greater than y". If y is greater than x, we want to print "y is greater than x".
        We use if statements in such decision making situations.

    elif ve else ifadeleri de if ifadesiyle birlikte kullanılır. elif ifadesi, if ifadesinin koşulu sağlamadığı
    durumlarda kullanılır. else ifadesi ise hiçbir koşul sağlanmadığında çalışır. else ifadesi, if ifadesinin
    koşulu sağlamadığı ve elif ifadesinin koşulu sağlamadığı durumlarda çalışır.

        - elif and else statements are also used with the if statement. The elif statement is used when the condition of
        the if statement is not met. The else statement works when no condition is met. The else statement works when
        neither the condition of the if statement nor the condition of the elif statement is met.

    if ifadesi, koşul sağlandığında çalışır. Koşul sağlanmazsa, if ifadesi çalışmaz. elif ifadesi, if ifadesinin
    koşulu sağlanmadığında çalışır. else ifadesi ise hiçbir koşul sağlanmadığında çalışır.

        - The if statement works when the condition is met. If the condition is not met, the if statement does not work.
        The elif statement works when the condition of the if statement is not met. The else statement works when no
        condition is met.
'''

print("If Statement")
print("Example 1")
('if ifacesi, belirli bir koşulun sağlanıp sağlanmadığını kontrol eder. Koşul sağlanıyorsa, if ifadesi çalışır. '
 'Koşul değeri "True" ise if ifadesi çalışır. Koşul değeri "False" ise if ifadesi çalışmaz.')
('The if statement checks whether a certain condition is met. If the condition is met, the if statement executes. '
 'If the condition value is "True", the if statement works. If the condition value is "False", the if statement does not run.')
condition = True
if condition:
    # Koşul doğruysa bu blok çalışır
    # If the condition is true, this block works
    print("Condition is ", condition)
    pass

print()

number = 5
if number > 3:
    print("Number is bigger than 3")
print("Program ended")

print("\n--------------------------------------------------")

print("\nIf - else Statement")
print("Example 1")
('if ifadesi, koşul sağlanıyorsa çalışır. Koşul sağlanmıyorsa çalışmaz. else ifadesi ise hiçbir koşul sağlanmadığında '
 'çalışır.')
('The if statement works if the condition is met. If the condition is not met, it does not work. The else statement '
 'works when no condition is met.')

sayi = -5 # Sayıyı değiştirerek programı çalıştırın # Change the number and run the program

if sayi > 0: # Sayı pozitifse # If the number is positive
    print("Sayı pozitif.") # Bu blok çalışır # This block works
else: # Sayı pozitif değilse # If the number is not positive
    print("Sayı negatif veya sıfır.") # Bu blok çalışır # This block works


print("\n--------------------------------------------------")

print("\nelif Statement")
print("Example 1")
('if ifadesi, koşul sağlanıyorsa çalışır. Koşul sağlanmıyorsa çalışmaz. elif ifadesi, if ifadesinin koşulu sağlanmıyorsa '
 'çalışır.')
('The if statement works if the condition is met. If the condition is not met, it does not work. The elif statement '
 'works if the condition of the if statement is not met.')

sayi = 0 # Sayıyı değiştirerek programı çalıştırın # Change the number and run the program
if sayi > 0: # Sayı pozitifse # If the number is positive
    print("Sayı pozitif.") # Bu blok çalışır # This block works
elif sayi < 0:
    print("Sayı negatif.") # Bu blok çalışır # This block works
else:
    print("Sayı sıfır.")
print("Program sonlandı.")

print("\nExample 2")
('elif ifadesi, if ifadesinin koşulu sağlanmıyorsa çalışır.')
('The elif statement works if the condition of the if statement is not met.')
if "Ali" == "Veli" :
    print("Bir")
elif 16 >= 17:
    print("Iki")
elif 7 == len("merhaba"):
    print("Uc")
else:
    print("Dort")

print("\nExample 3")
('elif ifadesi, if ifadesinin koşulu sağlanmıyorsa çalışır.')
('The elif statement works if the condition of the if statement is not met.')

('if-else deyimindeki koşullar içinde karşılaştırma yapabilmek için kıyaslama (>, <, <=, >=, ==, !=) ve mantıksal (and, or, not)'
 ' operatörlerini kullanabiliriz. Ayrıca, in ve not operatörlerini de kullanabiliriz. in operatörü, a in b şeklinde yazıldığında, '
 'a\'nın b verisi içinde olup olmadığını kontrol eder.')
('To be able to compare in the conditions in the if-else statement, we can use the comparison (>, <, <=, >=, ==, !=) and '
    'logical (and, or, not) operators. We can also use the in and not operators. The in operator, when written as a in b, '
    'checks whether a is in the b data.')

x = "portakal" # x = "kivi" # x = "elma"
y = "portakal suyu" # y = "kivi suyu" # y = "elma suyu"

if 8 == "8": # Koşul sağlanmaz # Condition is not met
    print("Sekiz") # Bu blok çalışmaz # This block does not work
elif "kiraz" > "elma" and "armut" > "kivi": # Koşul sağlanmaz # Condition is not met
    print("kiraz")  # Bu blok çalışmaz # This block does not work
elif x in y: # Koşul sağlanır # Condition is met
    print("portakal suyu") # Bu blok çalışır # This block works
else: # Koşul sağlanmaz # Condition is not met
    print("kivi") # Bu blok çalışmaz # This block does not work
print("program sonu") # Bu blok çalışır # This block works

print("\nExample 4")
('elif ifadesi, if ifadesinin koşulu sağlanmıyorsa çalışır.')
('The elif statement works if the condition of the if statement is not met.')

if (6 > 3 or "Elma" == "Armut") and ("ali" != "ADA" or 3 == len("idea")): # Koşul sağlanır # Condition is met
    print("sartlar saglandi") # Bu blok çalışır # This block works
else: # Koşul sağlanmaz # Condition is not met
    print("sartlar saglanmadi")    # Bu blok çalışmaz # This block does not work

print("\n--------------------------------------------------")

print("\nNested if Statement | iç içe if ifadeleri")
('Birden fazla if ifadesini iç içe kullanabiliriz. Bu durumda, içteki if ifadesi, dıştaki if ifadesinin koşulu sağlandığında '
 'çalışır. İçteki if ifadesinin koşulu da sağlanıyorsa, içteki if ifadesi çalışır. İçteki if ifadesinin koşulu sağlanmıyorsa, '
 'içteki if ifadesi çalışmaz.')
('We can use multiple if statements nested. In this case, the inner if statement works when the condition of the outer if '
    'statement is met. If the condition of the inner if statement is also met, the inner if statement works. If the '
    'condition of the inner if statement is not met, the inner if statement does not work.')

print("Example 1")
x=5
y=8
if x==5:
    if y==8:
        print("x = 5 ve y=8 dir")
        print("program sonu")

print("\nExample 2")
x = 10

if x > 0:
    print("x pozitif.")
    if x % 2 == 0:
        print("x çift sayı.")
    else:
        print("x tek sayı.")
else:
    print("x negatif veya sıfır.")
print("program sonu")



print("\nExample 3")
marketFiyatlari = {"kahvaltilik": {"peynir" : 35 , "zeytin": 40, "yumurta": 30 },
                   "temelGida" : {"makarna" : 5.35 , "pirinc": 20, "bulgur": 12.5},
                   "temizlik" : {"deterjan": 20 , "cif": 23 , "camasirSuyu": 20},
                   "icecek" : {"su5litre": 6.65 , "kola": 6 , "soda": 6.5}
                  }
tutar = 0
if "kisiselBakim" in marketFiyatlari.keys():
    if len(marketFiyatlari["kisiselBakim"]) > 0:
        tutar = sum(marketFiyatlari["kisiselBakim"].values())
        print(tutar)

elif "cay" in marketFiyatlari["icecek"].keys():
    tutar = sum(marketFiyatlari["icecek"].values()) / len(marketFiyatlari["icecek"])
    print(tutar)

elif "temizlik" in marketFiyatlari:
    if "sunger" in marketFiyatlari["temizlik"].keys():
        tutar = 4 * marketFiyatlari["temizlik"]["sunger"]
        print(tutar)

    elif "cif" in marketFiyatlari["temizlik"]:
        tutar = 3 * marketFiyatlari["temizlik"]["cif"]
        if tutar > 50:
            # %10 indirim uygula
            tutar -= tutar* 0.1
        print(tutar)
else:
    print("aranan sartlar saglanamadi...")
print("program sonu")

print("\nExample 4")
sicaklik = 23
ruzgar = 3.2 #km/h
basinc = 67 # mmHg

if sicaklik > 21:
    if ruzgar > 3.2:
        if basinc > 66:
            yagmur = True
            print("yağmurlu")
        else:
            yagmur = False
            print("yağmursuz")
    else:
        yagmur = False
        print("yağmursuz")
else:
    if ruzgar > 7.2:
        yagmur = True
        print("yağmurlu")
    else:
        if basinc > 79:
            yagmur = True
            print("yağmurlu")
        else:
            yagmur = False
            print("yağmursuz")
print("program sonu")

print("\n--------------------------------------------------")

print("\nSingle Statement Conditions | Tek Satırlık Koşullar")
'Python\'da tek satırlık koşullar yazabiliriz. Bu durumda, if ifadesinden sonra koşul yazılır, iki nokta üst üste (:) '
'koyulur ve tek satırda if ifadesi yazılır.'
'We can write single-line conditions in Python. In this case, the condition is written after the if statement, '
'two dots (:) are put and the if statement is written in a single line.'

print("Example 1")
x = 5
if x > 0: print("x pozitif.") # Bu blok çalışır # This block works
print("program sonu") # Bu blok çalışır # This block works

print("\nExample 2")
x = 5
if x > 0: print("x pozitif.") # Bu blok çalışır # This block works
else: print("x negatif veya sıfır.")
print("program sonu") # Bu blok çalışır # This block works

print("\nExample 3")
x = 5
yazdir = "x büyük" if x > 0 else "x küçük veya sıfır"
print(yazdir)
print("program sonu")

print("\nExample 4")
x=5
if x>2: print("Büyüktür")
if x>2: print("Merhaba"); print("Dünya")

print("\nExample 5")
if x>2:
    print("Merhaba")
    print("Dünya")

print("\n--------------------------------------------------")

print("\n--------------------------------------------------")

print("\n--------------------------------------------------")





