print("\n---> Return İfadesi | Return Statement <---")
print("Example 1 --> Return İfadesi | Return Statement")
def kare_al(sayi): # Fonksiyon tanımlama | Function definition
    'Bu fonksiyon, girilen sayinin karesini hesaplar' # Fonksiyonun açıklaması | Function description
    'This function calculates the square of the entered number'
    return sayi**2 # Fonksiyonun sonucunu döndürür | Returns the result of the function
print("3 Sayısının Karesi :", kare_al(3)) # Fonksiyonu çağır ve sonucu yazdır | Call the function and print the result
print("Program ended | Program sonlandı\n")

print("Example 2 --> Return İfadesi | Return Statement")
def daireAlanı(r, pi=3.14): # Fonksiyon tanımlama | Function definition
    'Bu fonksiyon, girilen yarıçap değerine göre dairenin alanını hesaplar' # Fonksiyonun açıklaması | Function description
    'This function calculates the area of the circle according to the entered radius value'
    return pi * r**2 # Fonksiyonun sonucunu döndürür | Returns the result of the function
print("Yarıçapı 5 olan dairenin alanı :", daireAlanı(5)) # Fonksiyonu çağır ve sonucu yazdır | Call the function and print the result
print("Program ended | Program sonlandı\n")

print("Example 3 --> Return İfadesi | Return Statement")
def hesaplama(sayi1, sayi2): # Fonksiyon tanımlama | Function definition
    toplama = sayi1 + sayi2 # Toplama işlemi | Addition operation
    carpma = sayi1 * sayi2 # Çarpma  işlemi | Multiplication operation
    bolme = sayi1 / sayi2 # Bölme işlemi | Division operation
    cikarma = sayi1 - sayi2 # Çıkarma işlemi | Subtraction operation
    # birden cok deger dondurmek icin virgul kullan
    return toplama, carpma, bolme, cikarma # Fonksiyonun sonucunu döndürür | Returns the result of the function

# sonucları tuple formatinda dondur
hepsi = hesaplama(50, 30) # Fonksiyonu çağır ve sonucu yazdır | Call the function and print the result
print("Dört işlem sonuçları :", hepsi) # Sonucu yazdır | Print the result

# sonucları tek tek dondur
toplama, carpma, bolme, cikarma = hesaplama(50, 30)
print("Toplama :", toplama) # Sonucu yazdır | Print the result
print("Çarpma :", carpma) # Sonuc u yazdır | Print the result
print("Bölme :", bolme) # Sonucu yazdır | Print the result
print("Çıkarma :", cikarma) # Sonucu yazdır | Print the result
print("Program ended | Program sonlandı\n")
