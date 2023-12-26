print("\n---> Özyinelemeli Fonksiyonlar | Recursive Functions <---")
# Özyinelemeli fonksiyonlar, kendini çağıran fonksiyonlardır.
# Özyinelemeli fonksiyonlar, fonksiyon içinde kendini çağıran bir ifadeye sahip olmalıdır.
# Özyinelemeli fonksiyonlar, bir döngü ile de yazılabilir.

print("Example 1 --> Factorial")
def faktoriyel(sayi):
    if sayi == 1:
        return 1
    else:
        return sayi * faktoriyel(sayi - 1)

print(faktoriyel(5))
print("Program ended | Program sonlandı\n")

print("Example 2 --> Factorial")
def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

print(faktoriyel(5))
print("Program ended | Program sonlandı\n")

print("Example 3 --> Fibonacci Series")
def fibonacci(sayi):
    if sayi == 0:
        return 0
    elif sayi == 1:
        return 1
    else:
        return fibonacci(sayi - 1) + fibonacci(sayi - 2)

print(fibonacci(10))
print("Program ended | Program sonlandı\n")

print("Example 4 --> Fibonacci Series")
def fibonacci(sayi):
    a, b = 0, 1
    for i in range(sayi):
        a, b = b, a + b
    return a

print(fibonacci(10))
print("Program ended | Program sonlandı\n")

print("Example 5 --> Perfect Number")
def perfect_number(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

print(perfect_number(28))
print("Program ended | Program sonlandı\n")

print("Example 6 --> Bir liste üzerinden özyinelemesiz toplama | Non-recursive sum over a list")
def toplam(list):
    toplam = 0
    for i in range(0, len(list)): # add every number in the list to the variable toplam
        toplam = toplam + list[i] # sum every number in the list and assign it to the variable toplam
    return toplam # return the sum of the numbers in the list

print(toplam([5,7,3,8,10])) # Test edelim | Let's test

print("Example 7 --> Bir liste üzerinden özyinelemeli toplama | Recursive sum over a list")
def toplam(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + toplam(list[1:])
print(toplam([5,7,3,8,10]))

