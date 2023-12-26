"""
    # python modülleri aşağıdaki gibidir
# python modules are as follows
# https://docs.python.org/3/py-modindex.html
# 1. Built-in Functions
    # 1.1. abs()
        # abs() fonksiyonu girilen sayının mutlak değerini döndürür | abs() function returns the absolute value of the entered number
    # 1.2. all()
        # all() fonksiyonu girilen nesnenin elemanlarının hepsi True ise True, en az biri False ise False döndürür | all() function returns True if all elements of the entered object are True, False if at least one is False
    # 1.3. any()
        # any() fonksiyonu girilen nesnenin elemanlarından en az biri True ise True, hepsi False ise False döndürür | any() function returns True if at least one of the elements of the entered object is True, False if all are False
    # 1.4. ascii()
        # ascii() fonksiyonu girilen nesnenin ascii karşılığını döndürür | ascii() function returns the ascii equivalent of the entered object
    # 1.5. bin()
        # bin() fonksiyonu girilen sayının ikilik tabandaki karşılığını döndürür | bin() function returns the binary equivalent of the entered number
    # 1.6. bool()
        # bool() fonksiyonu girilen değerin boolean karşılığını döndürür | bool() function returns the boolean equivalent of the entered value
    # 1.7. breakpoint()
        # breakpoint() fonksiyonu hata ayıklama için kullanılır | breakpoint() function is used for debugging
    # 1.8. bytearray()
        # bytearray() fonksiyonu girilen nesnenin byte dizisi karşılığını döndürür | bytearray() function returns the byte array equivalent of the entered object
    # 1.9. bytes()
        # bytes() fonksiyonu girilen nesnenin byte karşılığını döndürür | bytes() function returns the byte equivalent of the entered object
    # 1.10. callable()
        # callable() fonksiyonu girilen değerin çağrılabilir olup olmadığını döndürür | callable() function returns whether the entered value is callable
    # 1.11. chr()
        # chr() fonksiyonu girilen sayının karakter karşılığını döndürür | chr() function returns the character equivalent of the entered number
    # 1.12. classmethod()
        # classmethod() fonksiyonu girilen fonksiyonu sınıf metoduna dönüştürür | classmethod() function converts the entered function to a class method
    # 1.13. compile()
        # compile() fonksiyonu girilen kodu derler | compile() function compiles the entered code
    # 1.14. complex()
        # complex() fonksiyonu girilen sayının karmaşık sayı karşılığını döndürür | complex() function returns the complex number equivalent of the entered number
    # 1.15. delattr()
        # delattr() fonksiyonu girilen nesnenin girilen niteliğini siler | delattr() function deletes the entered attribute of the entered object
    # 1.16. dict()
        # dict() fonksiyonu girilen nesnenin sözlük karşılığını döndürür | dict() function returns the dictionary equivalent of the entered object
    # 1.17. dir()
        # dir() fonksiyonu girilen nesnenin niteliklerini döndürür | dir() function returns the attributes of the entered object
    # 1.18. divmod()
        # divmod() fonksiyonu girilen sayıların bölümünü ve kalanını döndürür | divmod() function returns the division and remainder of the entered numbers
    # 1.19. enumerate()
        # enumerate() fonksiyonu girilen nesnenin elemanlarını numaralandırır | enumerate() function enumerates the elements of the entered object
    # 1.20. eval()
        # eval() fonksiyonu girilen kodu çalıştırır | eval() function runs the entered code
    # 1.21. exec()
        # exec() fonksiyonu girilen kodu çalıştırır | exec() function runs the entered code
    # 1.22. filter()
        # filter() fonksiyonu girilen fonksiyonu girilen nesnenin elemanlarına uygular | filter() function applies the entered function to the elements of the entered object
    # 1.23. float()
        # float() fonksiyonu girilen değerin ondalıklı sayı karşılığını döndürür | float() function returns the decimal equivalent of the entered value
    # 1.24. format()
        # format() fonksiyonu girilen değerin girilen formata göre karşılığını döndürür | format() function returns the equivalent of the entered value according to the entered format
    # 1.25. frozenset()
        # frozenset() fonksiyonu girilen nesnenin donmuş küme karşılığını döndürür | frozenset() function returns the frozen set equivalent of the entered object
    # 1.26. getattr()
        # getattr() fonksiyonu girilen nesnenin girilen niteliğini döndürür | getattr() function returns the entered attribute of the entered object
    # 1.27. globals()
        # globals() fonksiyonu global değişkenleri döndürür | globals() function returns global variables
    # 1.28. hasattr()
        # hasattr() fonksiyonu girilen nesnenin girilen niteliğinin olup olmadığını döndürür | hasattr() function returns whether the entered object has the entered attribute
    # 1.29. hash()
        # hash() fonksiyonu girilen nesnenin hash karşılığını döndürür | hash() function returns the hash equivalent of the entered object
    # 1.30. help()
        # help() fonksiyonu girilen nesnenin yardım belgesini döndürür | help() function returns the help document of the entered object
    # 1.31. hex()
        # hex() fonksiyonu girilen sayının onaltılık tabandaki karşılığını döndürür | hex() function returns the hexadecimal equivalent of the entered number
    # 1.32. id()
        # id() fonksiyonu girilen nesnenin bellekteki kimliğini döndürür | id() function returns the identity of the entered object in memory
    # 1.33. input()
        # input() fonksiyonu kullanıcıdan veri alır | input() function gets data from the user
    # 1.34. int()
        # int() fonksiyonu girilen değerin tam sayı karşılığını döndürür | int() function returns the integer equivalent of the entered value
    # 1.35. isinstance()
        # isinstance() fonksiyonu girilen nesnenin girilen türden olup olmadığını döndürür | isinstance() function returns whether the entered object is of the entered type
    # 1.36. issubclass()
        # issubclass() fonksiyonu girilen sınıfın girilen sınıfın alt sınıfı olup olmadığını döndürür | issubclass() function returns whether the entered class is a subclass of the entered class
    # 1.37. iter()
        # iter() fonksiyonu girilen nesnenin yinelenebilir karşılığını döndürür | iter() function returns the iterable equivalent of the entered object
    # 1.38. len()
        # len() fonksiyonu girilen nesnenin uzunluğunu döndürür | len() function returns the length of the entered object
    # 1.39. list()
        # list() fonksiyonu girilen nesnenin liste karşılığını döndürür | list() function returns the list equivalent of the entered object
    # 1.40. locals()
        # locals() fonksiyonu yerel değişkenleri döndürür | locals() function returns local variables
    # 1.41. map()
        # map() fonksiyonu girilen fonksiyonu girilen nesnenin elemanlarına uygular | map() function applies the entered function to the elements of the entered object
    # 1.42. max()
        # max() fonksiyonu girilen nesnenin en büyük elemanını döndürür | max() function returns the largest element of the entered object
    # 1.43. memoryview()
        # memoryview() fonksiyonu girilen nesnenin bellek görünümü karşılığını döndürür | memoryview() function returns the memory view equivalent of the entered object
    # 1.44. min()
        # min() fonksiyonu girilen nesnenin en küçük elemanını döndürür | min() function returns the smallest element of the entered object
    # 1.45. next()
        # next() fonksiyonu girilen nesnenin bir sonraki elemanını döndürür | next() function returns the next element of the entered object
    # 1.46. object()
        # object() fonksiyonu boş bir nesne döndürür | object() function returns an empty object
    # 1.47. oct()
        # oct() fonksiyonu girilen sayının sekizlik tabandaki karşılığını döndürür | oct() function returns the octal equivalent of the entered number
    # 1.48. open()
        # open() fonksiyonu girilen dosyayı açar | open() function opens the entered file
    # 1.49. ord()
        # ord() fonksiyonu girilen karakterin sayı karşılığını döndürür | ord() function returns the number equivalent of the entered character
    # 1.50. pow()
        # pow() fonksiyonu girilen sayının girilen üssünü döndürür | pow() function returns the entered power of the entered number
    # 1.51. print()
        # print() fonksiyonu girilen değeri ekrana yazdırır | print() function prints the entered value to the screen
    # 1.52. property()
        # property() fonksiyonu girilen fonksiyonu özellik haline getirir | property() function makes the entered function a property
    # 1.53. range()
        # range() fonksiyonu girilen sayıya kadar olan sayıları döndürür | range() function returns the numbers up to the entered number
    # 1.54. repr()
        # repr() fonksiyonu girilen değerin gösterimini döndürür | repr() function returns the representation of the entered value
    # 1.55. reversed()
        # reversed() fonksiyonu girilen nesnenin tersini döndürür | reversed() function returns the reverse of the entered object
    # 1.56. round()
        # round() fonksiyonu girilen sayıyı girilen basamağa göre yuvarlar | round() function rounds the entered number to the entered digit
    # 1.57. set()
        # set() fonksiyonu girilen nesnenin küme karşılığını döndürür | set() function returns the set equivalent of the entered object
    # 1.58. setattr()
        # setattr() fonksiyonu girilen nesnenin girilen niteliğini girilen değere eşitler | setattr() function sets the entered attribute of the entered object to the entered value
    # 1.59. slice()
        # slice() fonksiyonu girilen nesnenin girilen dilimini döndürür | slice() function returns the entered slice of the entered object
    # 1.60. sorted()
        # sorted() fonksiyonu girilen nesnenin sıralanmış halini döndürür | sorted() function returns the sorted version of the entered object
    # 1.61. staticmethod()
        # staticmethod() fonksiyonu girilen fonksiyonu statik metod haline getirir | staticmethod() function makes the entered function a static method
    # 1.62. str()
        # str() fonksiyonu girilen değerin karakter dizisi karşılığını döndürür | str() function returns the string equivalent of the entered value
    # 1.63. sum()
        # sum() fonksiyonu girilen nesnenin elemanlarının toplamını döndürür | sum() function returns the sum of the elements of the entered object
    # 1.64. super()
        # super() fonksiyonu girilen sınıfın üst sınıfını döndürür | super() function returns the superclass of the entered class
    # 1.65. tuple()
        # tuple() fonksiyonu girilen nesnenin demet karşılığını döndürür | tuple() function returns the tuple equivalent of the entered object
    # 1.66. type()
        # type() fonksiyonu girilen nesnenin türünü döndürür | type() function returns the type of the entered object
    # 1.67. vars()
        # vars() fonksiyonu girilen nesnenin sözlük karşılığını döndürür | vars() function returns the dictionary equivalent of the entered object
    # 1.68. zip()
        # zip() fonksiyonu girilen nesnelerin elemanlarını birleştirir | zip() function merges the elements of the entered objects
"""

print("\n---> Modüller | Modules <---")
# Modüller, Python kodlarını içeren dosyalardır.
# Modüller, import anahtar kelimesi ile kullanılır.
# Modüller, aynı dizindeki .py uzantılı dosyalardır.

print("Example 1 --> Modüller | Modules\ import math modülü mateamatiksel işlemler için kullanılır\n import math module is used for mathematical operations")
import math
print(math.factorial(5))
print(math.sqrt(25))
print(math.log10(100))
print(math.pi)
print(math.e)
print("Program ended | Program sonlandı\n")

print("Example 2 --> Modüller | Modules\ import math modülü mateamatiksel işlemler için kullanılır\n import math module is used for mathematical operations")
import math as matematik
print(matematik.factorial(5))
print(matematik.sqrt(25))
print(matematik.log10(100))
print(matematik.pi)
print(matematik.e)
print("Program ended | Program sonlandı\n")

print("Example 3 --> Modüller | Modules\ from math import * modülü mateamatiksel işlemler için kullanılır\n from math import * module is used for mathematical operations")
from math import *
print(factorial(5))
print(sqrt(25))
print(log10(100))
print(pi)
print(e)
print("Program ended | Program sonlandı\n")

print("Example 4 --> Modüller | Modules\ from math import factorial, sqrt, log10, pi, e modülü mateamatiksel işlemler için kullanılır\n from math import factorial, sqrt, log10, pi, e module is used for mathematical operations")
from math import factorial, sqrt, log10, pi, e
print(factorial(5))
print(sqrt(25))
print(log10(100))
print(pi)
print(e)
print("Program ended | Program sonlandı\n")

print("Example 5 --> Modüller | Modules\ from math import factorial as faktoriyel, sqrt as karekok, log10 as logaritma, pi as piSayisi, e as eulerSayisi modülü mateamatiksel işlemler için kullanılır\n from math import factorial as faktoriyel, sqrt as karekok, log10 as logaritma, pi as piSayisi, e as eulerSayisi module is used for mathematical operations")
from math import factorial as faktoriyel, sqrt as karekok, log10 as logaritma, pi as piSayisi, e as eulerSayisi
print(faktoriyel(5))
print(karekok(25))
print(logaritma(100))
print(piSayisi)
print(eulerSayisi)
print("Program ended | Program sonlandı\n")

print("Example 6 --> Modüller | Modules\ import random modülü rastgele sayı üretmek için kullanılır\n import random module is used to generate random numbers")
import random
print(random.random())
print(random.randint(1, 100))
print(random.randrange(1, 100))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choice('abcçdefgğhıijklmnoöprsştuüvyz'))
print(random.choice(['a', 'b', 'c', 'd', 'e']))
print(random.choice(['a', 'b', 'c', 'd', 'e']))
print(random.choice(['a', 'b', 'c', 'd', 'e']))
print(random.choice(['a', 'b', 'c', 'd', 'e']))
print(random.choice(['a', 'b', 'c', 'd', 'e']))
print("Program ended | Program sonlandı\n")

print("Example 7 --> Modüller | Modules\ import random modülü rastgele sayı üretmek için kullanılır\n import random module is used to generate random numbers")
import random as rastgele
print(rastgele.random())
print(rastgele.randint(1, 100))
print(rastgele.randrange(1, 100))
print(rastgele.choice([1, 2, 3, 4, 5]))
print(rastgele.choice('abcçdefgğhıijklmnoöprsştuüvyz'))
print(rastgele.choice(['a', 'b', 'c', 'd', 'e']))
print("Program ended | Program sonlandı\n")

print("Example 8 --> Modüller | Modules\ from random import * modülü rastgele sayı üretmek için kullanılır\n from random import * module is used to generate random numbers")
from random import *
print(random())
print(randint(1, 100))
print(randrange(1, 100))
print(choice([1, 2, 3, 4, 5]))
print(choice('abcçdefgğhıijklmnoöprsştuüvyz'))
print(choice(['a', 'b', 'c', 'd', 'e']))
print("Program ended | Program sonlandı\n")

print("Example 9 --> Modüller | Modules\ from random import random, randint, randrange, choice modülü rastgele sayı üretmek için kullanılır\n from random import random, randint, randrange, choice module is used to generate random numbers")
from random import random, randint, randrange, choice
print(random())
print(randint(1, 100))
print(randrange(1, 100))
print(choice([1, 2, 3, 4, 5]))
print(choice('abcçdefgğhıijklmnoöprsştuüvyz'))
print(choice(['a', 'b', 'c', 'd', 'e']))
print("Program ended | Program sonlandı\n")

print("Example 10 --> Modüller | Modules\ from random import random as rastgele, randint as rastgeleTamSayi, randrange as rastgeleAralik, choice as sec modülü rastgele sayı üretmek için kullanılır\n from random import random as rastgele, randint as rastgeleTamSayi, randrange as rastgeleAralik, choice as sec module is used to generate random numbers")
from random import random as rastgele, randint as rastgeleTamSayi, randrange as rastgeleAralik, choice as sec
print(rastgele())
print(rastgeleTamSayi(1, 100))
print(rastgeleAralik(1, 100))
print(sec([1, 2, 3, 4, 5]))
print(sec('abcçdefgğhıijklmnoöprsştuüvyz'))
print(sec(['a', 'b', 'c', 'd', 'e']))
print("Program ended | Program sonlandı\n")

print("Example 11 --> Modüller | Modules\ import datetime modülü tarih ve saat işlemleri için kullanılır\n import datetime module is used for date and time operations")
import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)
print(datetime.datetime.now().date())
print(datetime.datetime.now().time())
print("Program ended | Program sonlandı\n")

print("Example 12 --> Modüller | Modules\ import datetime modülü tarih ve saat işlemleri için kullanılır\n import datetime module is used for date and time operations")
import datetime as tarihSaat
print(tarihSaat.datetime.now())
print(tarihSaat.datetime.now().year)
print(tarihSaat.datetime.now().month)
print(tarihSaat.datetime.now().day)
print(tarihSaat.datetime.now().hour)
print(tarihSaat.datetime.now().minute)
print(tarihSaat.datetime.now().second)
print(tarihSaat.datetime.now().microsecond)
print(tarihSaat.datetime.now().date())
print(tarihSaat.datetime.now().time())
print("Program ended | Program sonlandı\n")

print("Example 13 --> Modüller | Modules\ from datetime import * modülü tarih ve saat işlemleri için kullanılır\n from datetime import * module is used for date and time operations")
from datetime import *
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().microsecond)
print(datetime.now().date())
print(datetime.now().time())
print("Program ended | Program sonlandı\n")

print("Example 14 --> Modüller | Modules\ from datetime import datetime, date, time modülü tarih ve saat işlemleri için kullanılır\n from datetime import datetime, date, time module is used for date and time operations")
from datetime import datetime, date, time
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().microsecond)
print(datetime.now().date())
print(datetime.now().time())
print("Program ended | Program sonlandı\n")

print("Example 15 --> Modüller | Modules\ from datetime import datetime as tarihSaat, date as tarih, time as saat modülü tarih ve saat işlemleri için kullanılır\n from datetime import datetime as tarihSaat, date as tarih, time as saat module is used for date and time operations")
from datetime import datetime as tarihSaat, date as tarih, time as saat
print(tarihSaat.now()) # Yıl, ay, gün, saat, dakika, saniye ve mikrosaniye bilgilerini verir | gives us year, month, day, hour, minute, second and microsecond information
print(tarihSaat.now().year) # Yıl bilgisini verir | gives us only year information
print(tarihSaat.now().month) # Yıl ve ay bilgilerini verir | gives us only year and month information
print(tarihSaat.now().day) # Yıl, ay ve gün bilgilerini verir | gives us only year, month and day information
print(tarihSaat.now().hour) # Saat bilgisini verir | gives us hour information
print(tarihSaat.now().minute) # Dakika bilgisini verir | gives us minute information
print(tarihSaat.now().second) # Saniye bilgisini verir | gives us second information
print(tarihSaat.now().microsecond) # Mikrosaniye bilgisini verir | gives us microsecond information
print(tarihSaat.now().date())  # Yıl, ay ve gün bilgilerini verir | gives us only year, month and day information
print(tarihSaat.now().time()) # Saat, dakika, saniye ve mikrosaniye bilgilerini verir | gives us only hour, minute, second and microsecond information
print("Program ended | Program sonlandı\n")

print("Example 16 --> Modüller | Modules\ import os modülü işletim sistemi işlemleri için kullanılır\n import os module is used for operating system operations")
import os # nt: Windows, posix: Linux
print(os.name) # nt: Windows, posix: Linux
print(os.getcwd()) # C:\Users\...: Windows, /home/...: Linux
print(os.listdir()) # C:\Users\...\Desktop\...: Windows, /home/.../Desktop/...: Linux
print(os.listdir('..')) # C:\Users\...\Desktop: Windows, /home/.../Desktop: Linux
print(os.listdir('../..')) # C:\Users\...: Windows, /home/...: Linux
print(os.listdir('../../..'))   # C:\Users: Windows, /home: Linux
print(os.listdir('c:/')) # C:\: Windows, /: Linux
print(os.listdir('c:/Users')) # C:\Users: Windows, /home: Linux
print(os.listdir('c:/Users/')) # C:\Users: Windows, /home: Linux
print(os.listdir('c:/Users/...')) # C:\Users\...\Desktop: Windows, /home/.../Desktop: Linux
print(os.listdir('c:/Users/.../Desktop/')) # C:\Users\...\Desktop\...: Windows, /home/.../Desktop/...: Linux
print(os.listdir('c:/Users/.../Desktop/...'))   # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(os.listdir('c:/Users/.../Desktop/.../')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(os.listdir('/usr/bin')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(os.listdir('/usr/bin/')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(os.listdir('/usr/bin/...')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(os.listdir('/usr/bin/.../')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print("Program ended | Program sonlandı\n")

print("Example 17 --> Modüller | Modules\ import os modülü işletim sistemi işlemleri için kullanılır\n import os module is used for operating system operations")
import os as isletimSistemi
print(isletimSistemi.name) # nt: Windows, posix: Linux
print(isletimSistemi.getcwd()) # C:\Users\...: Windows, /home/...: Linux
print(isletimSistemi.listdir()) # C:\Users\...\Desktop\...: Windows, /home/.../Desktop/...: Linux
print(isletimSistemi.listdir('..')) # C:\Users\...\Desktop: Windows, /home/.../Desktop: Linux
print(isletimSistemi.listdir('../..')) # C:\Users\...: Windows, /home/...: Linux
print(isletimSistemi.listdir('../../..')) # C:\Users: Windows, /home: Linux
print(isletimSistemi.listdir('c:/')) # C:\: Windows, /: Linux
print(isletimSistemi.listdir('c:/Users')) # C:\Users: Windows, /home: Linux
print(isletimSistemi.listdir('c:/Users/')) # C:\Users: Windows, /home: Linux
print(isletimSistemi.listdir('c:/Users/...')) # C:\Users\...\Desktop: Windows, /home/.../Desktop: Linux
print(isletimSistemi.listdir('c:/Users/.../Desktop/')) # C:\Users\...\Desktop\...: Windows, /home/.../Desktop/...: Linux
print(isletimSistemi.listdir('c:/Users/.../Desktop/...')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(isletimSistemi.listdir('c:/Users/.../Desktop/.../')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(isletimSistemi.listdir('/usr/bin')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(isletimSistemi.listdir('/usr/bin/')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(isletimSistemi.listdir('/usr/bin/...')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print(isletimSistemi.listdir('/usr/bin/.../')) # C:\Users\...\Desktop\...\...: Windows, /home/.../Desktop/.../...: Linux
print("Program ended | Program sonlandı\n")

print("Example 18 --> Modüller | Modules\ from os import * modülü işletim sistemi işlemleri için kullanılır\n from os import * module is used for operating system operations")
from os import *
print(name) # nt: Windows, posix: Linux
print(getcwd()) # C:\Users\...: Windows, /home/...: Linux
print("Program ended | Program sonlandı\n")

print("Example 19 --> Modüller | Modules\ from os import name, getcwd modülü işletim sistemi işlemleri için kullanılır\n from os import name, getcwd module is used for operating system operations")
print("Program ended | Program sonlandı\n")

print("Example 20 --> Modüller | Modules\ from os import name as isletimSistemi, getcwd as bulunduguDizin modülü işletim sistemi işlemleri için kullanılır\n from os import name as isletimSistemi, getcwd as bulunduguDizin module is used for operating system operations")
print("Program ended | Program sonlandı\n")

print("Example 21 --> Modüller | Modules\ import os modülü işletim sistemi işlemleri için kullanılır\n import os module is used for operating system operations")
