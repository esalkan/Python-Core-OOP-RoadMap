'''
    Değerler üzerinde çeşitli işlemleri gerçekleştirmek için kullanılan semboller veya özel kelimelerdir.
    Temel olarak, operatörler matematiksel işlemler, karşılaştırmalar, atama işlemleri ve mantıksal operasyonlar
    gibi farklı kategorilere ayrılabilir.

    Aritmetik Operatörler (Arithmetic Operators):
        Toplama: + (Addition)
        Çıkarma: - (Subtraction)
        Çarpma: * (Multiplication)
        Bölme: / (Division)
        Üs Alma: ** (Exponentiation)
        Mod (Kalan): % (Modulus)
        Taban Bölme (Floor Division): // (Floor Division)

    Karşılaştırma Operatörleri (Comparison Operators):
        Eşitse: == (Equal to)
        Eşit Değilse: != (Not equal to)
        Büyükse: > (Greater than)
        Küçükse: < (Less than)
        Büyük veya Eşitse: >= (Greater than or equal to)
        Küçük veya Eşitse: <= (Less than or equal to)

    Atama Operatörleri (Assignment Operators):
        Atama: = (Assignment)
        Topla ve Ata: += (Add and assign)
        Çıkar ve Ata: -= (Subtract and assign)
        Çarp ve Ata: *= (Multiply and assign)
        Böl ve Ata: /= (Divide and assign)
        Mod ve Ata: %= (Modulus and assign)
        Taban Bölme ve Ata: //= (Floor division and assign)
        Üs Al ve Ata: **= (Exponentiate and assign)

    Mantıksal Operatörler (Logical Operators):
        VE (AND): and
        VEYA (OR): or
        DEĞİL (NOT): not

    Kimlik Operatörleri (Identity Operators):
        Eşitse: is
        Eşit Değilse: is not

    Üyelik Operatörleri (Membership Operators):
        İçeriyorsa: in
        İçermiyorsa: not in

    Bitwise Operatörler (Bitwise Operators):
        VE (AND): &
        VEYA (OR): |
        XOR: ^
        Tekli Bit Kaydırma Sola: <<
        Tekli Bit Kaydırma Sağa: >>

'''

print("Aritmetik (Arithmetic) Operatörler:")
print("\nToplama (+)")
a = 5
b = 3
result = a + b
print("Toplama sonucu: ", result)  # Output: 8

print("\nÇıkarma (-):")
a = 5
b = 3
result = a - b
print("Çıkarma sonucu: ", result)  # Output: 2

print("\nÇarpma (*)")
a = 5
b = 3
result = a * b
print("Çarpma sonucu :", result)  # Output: 15

print("\nBölme (/)")
a = 6
b = 3
result = a / b
print("Bölme Sonucu: ", result)  # Output: 2.0

print("\nÜs Alma (**)")
a = 2
b = 3
result = a ** b
print("Üs alma sonucu: ", result)  # Output: 8

print("\nMod (%) | Kalanı Bulma")
a = 10
b = 3
result = a % b
print("Mod alma sonucu: ", result)  # Output: 1

print("\n-------------------------------------------")

print("\nİlişkisel (Comparison) Operatörler:")
print("\nEşitlik (==)")
x = 5
y = 5
result = x == y
print(result)  # Output: True

print("\nEşit Değil (!=)")
x = 5
y = 3
result = x != y
print(result)  # Output: True


print("\nBüyüktür (>)")
x = 5
y = 3
result = x > y
print(result)  # Output: True


print("\nKüçüktür (<)")
x = 5
y = 3
result = x < y
print(result)  # Output: False

print("\nBüyük Eşittir (>=)")
x = 5
y = 5
result = x >= y
print(result)  # Output: True

print("\nKüçük Eşittir (<=)")
x = 5
y = 3
result = x <= y
print(result)  # Output: False

print("\n-------------------------------------------")

print("\nAtama (Assignment) Operatörleri:")
print("\nAtama (=)")
x = 5

print("\nToplama Atama (+=)")
'x += 3 ifadesi, x in önceki değerine 3 ekler ve bunu x e atar. Bu atama ifadesi x = x + 3 atama ifadesi ile aynıdır. '
x = 5
x += 3
print(x)  # Output: 8

print("\nÇıkartma Atama (-=)")
'x -= 2 ifadesi, x\'nın önceki değerinden 2 çıkarır ve bunu x\'e atar. Bu atama ifadesi x = x - 2 atama ifadesi ile aynıdır.'
x = 5
x -= 2
print(x)  # Output: 3

print("\nÇarpma Atama (*=)")
x = 5
x *= 2
print(x)  # Output: 10

print("\nBölme Atama (/=)")
x = 10
x /= 2
print(x)  # Output: 5.0

print("\n-------------------------------------------")

print("\nMantıksal (Logical) Operatörler:")
print("\nVe (and)")
'Operatörün her iki tarafındaki koşullar doğruysa, ifade bir bütün olarak doğrudur. '
x = True
y = False
result = x and y
print(result)  # Output: False

print("\nVeya (or)")
('Operatörün her iki tarafındaki koşullardan en az biri DOĞRU (1) ise, ifade bir bütün olarak doğrudur. '
 'Eğer her iki taraftaki koşulların her ikisi de YANLIŞ (0) ise ifade bir bütün olarak YANLIŞtır. ')
x = True
y = False
result = x or y
print(result)  # Output: True

print("\nDeğil (not)")
'Not operatörü, bir ifadenin Boolean değerini tersine çevirir. Yani Doğru\'dan Yanlış\'a, Yanlış\'dan Doğru\'ya dönüştürür.'
x = True
result = not x
print(result)  # Output: False

print("\n-------------------------------------------")

print("\nÜyelik (Membership) Operatörleri:")
('Bu operatörler, bir değerin bir dizinin üyesi olup olmadığını kontrol eder. . '
 'Dizi bir liste, bir string veya bir tuple olabilir. Python\'da iki adet membership operatörü vardır:  '
 '"in" ve "not in". ')

print("\nİçeriyor (in)")
'Eğer kontrol edilen değer dizinin içinde yer alıyorsa TRUE aksi takdirde FALSE döndürür'
liste = [1, 2, 3, 4, 5]
result = 3 in liste
print(result)  # Output: True


print("\nİçermiyor (not)")
'Eğer kontrol edilen değer dizinin içinde yer almıyorsa TRUE aksi takdirde FALSE döndürür .'
liste = [1, 2, 3, 4, 5]
result = 6 not in liste
print(result)  # Output: True

print("\n-------------------------------------------")

print("\nBitsel (Bitwise) Operatörler:")
'Bitsel operatörler, bir tamsayının bitleri üzerinde bire bir ikili işlemleri yaparlar.'
'''
Elimizde iki adet tam sayımız olsun.
    x = 5 = 0101 (ikili sistemde)
    y = 7 = 0111 (ikili sistemde)
'''
print("\nVe (&)")
('x ve y nin tüm bitlerini bire bir karşılaştırır. Yani karşılıklı her bit arasında AND işlemi gerçekleştirir.  '
 'iki sayının bütün bitlerini AND işlemine tabi tutar. İki bitin AND işlemi, her iki bit de 1 ise sonuç 1, '
 'diğer durumlarda ise sonuç 0 olacaktır. '
 'Yukarıdaki x ve y sayılarını bit bit karşılaştırdığımızda sonucun ikili sistemde 0101, '
 'onluk sistemde ise 5 olacağını görebiliriz.')
x = 5
y = 7
result = x & y
print(result)  # Output: 1

print("\nVeya (|)")
('x ve x in tüm bitlerini bire bir karşılaştırır. Yani karşılıklı her bit arasında OR işlemi gerçekleştirir. '
 'Eğer karşılaştırma yapılan sayılardan herhangi biri 1 ise 1, aksi takdirde ise 0 döndürür. '
 'Yukarıdaki x ve y sayılarını bit bit karşılaştırdığımızda sonucun ikili sistemde 0111, '
 'onluk sistemde ise 7 olacağını görebiliriz.')
x = 5
y = 7
result = x | y
print(result)  # Output: 7

print("\nXOR (^) (OR)")
x = 5
y = 3
result = x ^ y
print(result)  # Output: 6

print("\nNegasyon(NOT) (~)")
('x sayısındaki tüm 0ları 1e, tüm birleri de 0a çevirir. Yani birin tümleri işlemini yapar. '
 '0101 sayısı (onluk tabanda 5 sayısına karşılık gelir) üzerinde birin tümleri işlemini uygulayarak 1010 sayısına '
 'dönüştürür. Ancak burada python yorumlayıcısı, en sağdaki bit 1 olduğu için sayının negatif olduğunu anlayıp '
 '-6 sonucunu ekrana yazar. Burada dikkat edilmesi gereken birin tümleri işleminin uygulanmasıdır. '
 'Eğer ikinin tümleri uygulanmış olsaydı sonuç olarak ekrana -5 yazılacaktı. ')
x = 5
result = ~x
print(result)  # Output: -6

print("\nSağa Kaydırma (>>)")
x = 8
result = x >> 1
print(result)  # Output: 4

print("\nSola Kaydırma (<<)")
x = 2
result = x << 2
print(result)  # Output: 8


