print("\n---> Lambda Fonksiyonları | Lambda Functions <---")
# Lambda fonksiyonları, tek satırlık fonksiyonlardır.
# Lambda fonksiyonları, fonksiyon tanımında lambda anahtar kelimesi ile belirtilir.
# Lambda fonksiyonları, fonksiyon içinde return anahtar kelimesi kullanılmaz.

print("Example 1 | Lambda Fonksiyonu ile Filtreleme | Filtering with Lambda Function")
kare_al = lambda sayi: sayi**2
print(kare_al(3))
print("Program ended | Program sonlandı\n")

print("Example 2 --> Lambda Fonksiyonu ile Filtreleme | Filtering with Lambda Function")
def kare_al(sayi): return sayi**2
print(kare_al(3))
print("Program ended | Program sonlandı\n")

print("Example 3 --> Lambda Fonksiyonu ile Filtreleme | Filtering with Lambda Function")
topla = lambda x, y: x + y
print(topla(3, 5))
print("Program ended | Program sonlandı\n")

print("Example 4 --> Lambda Fonksiyonu ile Filtreleme | Filtering with Lambda Function")
def topla(x, y): return x + y
print(topla(3, 5))
print("Program ended | Program sonlandı\n")

print("Example 5 --> Lambda Fonksiyonu ile Filtreleme | Filtering with Lambda Function")
def kare_al(x): return x**2
print(kare_al(3))
print("Program ended | Program sonlandı\n")