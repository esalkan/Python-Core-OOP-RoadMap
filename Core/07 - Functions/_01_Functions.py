'''
    Fonksiyonlar | Functions

    Kullanıcının tanımını yaptığı fonksiyonlar | Functions defined by the user
    Gömülü fonksiyonlar | Built-in functions
    Lambda fonksiyonları | Lambda functions
    Özyinelemeli fonksiyonlar | Recursive functions (Recursive functions)

    Fonksiyon Tanımlama Örneği | Function Definition Example

        def fonksiyon_adi(parametre1, parametre2, ...):
            # Fonksiyon gövdesi
            # Function body
            return deger

        def : Fonksiyon tanımlamak için kullanılan anahtar kelime
        fonksiyon_adi : Fonksiyonun adı
        parametre1, parametre2, ... : Fonksiyonun parametreleri
        return : Fonksiyonun sonucunu döndürmek için kullanılan anahtar kelime
        deger : Fonksiyonun sonucu

    Fonksiyon Tanımlama Kuralları | Function Definition Rules
        - Fonksiyon isimleri büyük harfler (A-Z), küçük harfler (a-z) veya alt çizgi (_) ile başlayabilir.
        - Fonksiyonun isminin geri kalanı büyük harfler (A-Z), küçük harfler (a-z), rakamlar(0-9) veya alt çizgi (_)'den oluşabilir.
        - Daha önceden rezerve edilmiş anahtar kelimeler fonksiyon ismi olarak kullanılamazlar.

    Python'da fonksiyonlar belirli bir görevi yerine getiren ve başka bir kod bloğu içinden çağrılabilen
    adlandırılmış kod bloklarıdır.

    - Fonksiyonlar, kodunuzu modüler hale getirmenize ve tekrar kullanılabilirliği artırmanıza yardımcı olur.
    - Fonksiyon tanımlamak için def anahtar kelimesini kullanırız.
    - Fonksiyon çağırmak için fonksiyonun adını ve ardından parantez içinde parametreleri kullanırız.

    - Fonksiyonlar, parametre alabilir veya almayabilir.
        - merhaba_dunya()

    - Fonksiyonlar, parametre alıyorsa, parametreler parantez içinde belirtilir.
        - def selamla(isim):

    - Fonksiyonlar, argüman alıyorsa, argümanlar parantez içinde belirtilir.
        - selamla("Dünya")

    - Fonksiyonlarda, return anahtar kelimesi ile fonksiyonun sonucu döndürülür.
        - def kare_al(sayi):
            return sayi**2

    - Fonksiyonlarda, varsayılan parametre değerleri belirtilebilir.
        - def selamla(isim="Dünya"):

    - Fonksiyonlarda, birden fazla parametre belirtilebilir.
        - def selamla(isim, soyisim, yas):

    - Fonksiyonlarda, esnek sayıda argümanlar.
        - def selamla(*args):
            return sum(args)

    - Fonksiyonlarda, esnek sayıda anahtar kelimeli argümanlar.
        - def selamla(**kwargs):
            if "isim" in kwargs:
                print("Merhaba", kwargs["isim"])
            else:
                print("Merhaba Dünya")

    Argüman tipleri | Argument types
        - Required arguments (Zorunlu/Positional argümanlar)
        - Keyword arguments (Anahtar kelime argümanları)
        - Default arguments (Varsayılan argümanlar)
        - Variable-length arguments (Esnek uzunluklu argümanlar)


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

'''
selamla = 'deneme'
print("---> Functions <---")
print("Example 1 --> Fonksiyonlar | Functions")
def selamla(): # Fonksiyon tanımlama | Function definition
    'Bu ilk selamlama fonksiyonudur [Fonksiyon açıklaması için kullanılır]' # Fonksiyonun açıklaması | Function description
    'This is the first greeting function [Used for function description]'
    print("Merhaba Dunya") # Fonksiyonun gövdesi | Function body

selamla() # Fonksiyonu çağır | Call the function
print(selamla.__doc__) # Fonksiyonun açıklamasını yazdır | Print the function description
print("Program ended | Program sonlandı\n")

print("Example 2 --> Fonksiyonlar | Functions")
def sesliSessiz(cumle): # Fonksiyon tanımlama | Function definition
    sesli = 0 # Sesli harf sayısı | Number of vowels
    sessiz = 0 # Sessiz harf sayısı | Number of consonants
    # girilen cumlenin uzunlugunu bul
    for i in range(len(cumle)): # Fonksiyonun gövdesi | Function body
        if cumle[i] in ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']: # Sesli harf kontrolü | Vowel check
            sesli = sesli + 1 # Sesli harf sayısını arttır | Increase the number of vowels
        else: # Sessiz harf kontrolü | Consonant check
            sessiz = sessiz + 1 # Sessiz harf sayısını arttır | Increase the number of consonants
    print(cumle, " 'deki sesli harf sayisi =", sesli) # Sonucu yazdır | Print the result
    print(cumle, " 'deki sessiz harf sayisi =", sessiz) # Sonucu yazdır | Print the result


x = input("Bir cümle giriniz ") # Kullanıcıdan cümle al | Get sentence from user
sesliSessiz(x) # Fonksiyonu çağır | Call the function
print("Program ended | Program sonlandı\n")







