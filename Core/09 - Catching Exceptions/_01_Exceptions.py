'''

    Hata çözümleme (Exception Handling) veya hata yakalama (Exception Catching) olarak da bilinir.
    Programlarımız çalışırken bazı hatalarla karşılaşabilir. Bu hatalar programımızın çökmesine neden olabilir.
    Bu hataların önüne geçmek için hata çözümleme kullanırız.

    Hata çözümleme, programımızın çökmesini engellemek için hataları yakalamamızı sağlar.

    Örneğin, bir dosyayı okumaya çalışırken dosya bulunamazsa programımız çöker.
    Bu hatayı yakalayarak programımızın çökmesini engelleyebiliriz.

    Örnek:
        try:
            # Hata çıkarabilecek kodlar
        except HataAdı:
            # Hata çıktığında çalışacak kodlar
        else:
            # Hata çıkmadığında çalışacak kodlar
        finally:
            # Hata olsun ya da olmasın çalışacak kodlar


    Built-in Exceptions (Python İçindeki Hatalar):
        - AssertionError: Bir assert ifadesi yanlış olduğunda oluşur. (AssertionError: 2 + 2 == 5)
        - AttributeError: Bir nesnenin bir özelliği olmadığında oluşur. (AttributeError: 'int' object has no attribute 'append')
        - FloatingPointError: Bir float sayı sıfıra bölündüğünde oluşur. (FloatingPointError: float division by zero)
        - MemoryError: Bir işlem için yeterli hafıza yoksa oluşur. (MemoryError)
        - IndexError: Bir dizinin dizin aralığının dışında bir dizine erişmeye çalıştığımızda oluşur. (IndexError: list index out of range)
        - NotImplementedError: Bir sınıfın metodu tanımlanmadığında oluşur. (NotImplementedError)
        - NameError: Bir değişken tanımlanmadığında oluşur. (NameError: name 'foo' is not defined)
        - KeyError: Bir sözlükte olmayan bir anahtar sözlüğe erişmeye çalıştığımızda oluşur. (KeyError: 'foo')
        - ImportError: Bir modül ya da modül içindeki bir nesne yüklenemediğinde oluşur. (ImportError: No module named 'foo')
        - ZeroDivisionError: Bir sayı sıfıra bölündüğünde oluşur. (ZeroDivisionError: division by zero)
        - GeneratorExit: Bir generator fonksiyonu kapatılmaya çalışıldığında oluşur. (GeneratorExit)
        - OverflowError: Bir sayı çok büyük olduğunda oluşur. (OverflowError: int too large to convert to float)
        - IndentationError: Girintileme hatası olduğunda oluşur. (IndentationError: unexpected indent)
        - EOFError: input() fonksiyonu dosya sonuna gelindiğinde oluşur. (EOFError: EOF when reading a line)
        - SyntaxError: Sözdizimi hatası olduğunda oluşur. (SyntaxError: invalid syntax)
        - TabError: Girintileme hatası olduğunda oluşur. (TabError: inconsistent use of tabs and spaces in indentation)
        - valueError: Bir fonksiyona geçilen argümanın veri tipi uygun değilse oluşur. (ValueError: invalid literal for int() with base 10: 'foo')
        - RuntimeError: Runtime hatası olduğunda oluşur. (RuntimeError: foo)
        - TypeError: Bir fonksiyona geçilen argümanın veri tipi uygun değilse oluşur. (TypeError: 'int' object is not iterable)
        - SystemError: Yorumlayıcı sisteminde bir hata olduğunda oluşur. (SystemError: foo)
        - KeyboardInterrupt: Kullanıcı bir tuşa bastığında oluşur. (KeyboardInterrupt)
        - OSError: İşletim sisteminde bir hata olduğunda oluşur. (OSError: [Errno 2] No such file or directory: 'foo')
        - IOError: Bir dosya açma işlemi başarısız olduğunda oluşur. (IOError: [Errno 2] No such file or directory: 'foo')

'''

# Örnek 1:
print("--> Örnek 1 Hata Mesajı | Example 1 Error Message <--")
try:
    sayi = int(input("Sayı: "))
    print("Girdiğiniz sayı:", sayi)
except:
    print("Hata!")

# Örnek 2:
print("--> Örnek 2 Hata Mesajı | Example 2 Error Message <--")
try:
    sayi = int(input("Sayı: "))
    print("Girdiğiniz sayı:", sayi)
except ValueError:
    print("Tip uyuşmazlığı!")

# Örnek 3:
print("--> Örnek 3 Hata Mesajı | Example 3 Error Message <--")
try:
    sayi = int(input("Sayı: "))
    print("Girdiğiniz sayı:", sayi)
except ValueError as ex:
    print(ex)

# Örnek 4:
print("--> Örnek 4 Finally | Example 4 Finally <--")
try:
    sayi = int(input("Sayı: "))
    print("Girdiğiniz sayı:", sayi)
except ValueError:
    print("Tip uyuşmazlığı!")
finally:
    print("İşlem tamamlandı.")

# Örnek 5:
print("--> Örnek 5 Veri Tipi Kontrolü | Example 5 Data Type Control <--")
try:
    sayi = int(input("Sayı: "))
    print("Girdiğiniz sayı:", sayi)
except ValueError:
    print("Tip uyuşmazlığı!")
else:
    print("İşlem tamamlandı.")

# Örnek 6:
print("--> Örnek 6 Değişken Tanımlama hatası | Example 6 Variable Definition Error <--")
try:
    print(x)
except NameError:
    print("Değişken tanımlı değil!")

# Örnek 7:
print("--> Örnek 7 birden fazla exeption | Example 7 more than one exeption <--")
try:
    sayi = int(input("Sayı: "))
    print("Girdiğiniz sayı:", sayi)
except ValueError:
    print("Tip uyuşmazlığı!")
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
except:
    print("Bir hata oluştu!")

# Örnek 8:
print("--> Örnek 8 birden fazla exeption | Example 8 more than one exeption <--")
def bolme(x, y):
    try:
        print(x // y)
    except ZeroDivisionError:
        print("Sıfıra bölme yapılamaz")
    except TypeError:
        print("Sayi veri tipleri haricinde baska veri tipi kullanmayiniz")

bolme(5,"nunum")


# Örnek 9:
print("test.txt isminde bir dosyamız olduğunu ve içindeki verilerin: 1, 2, 3, 4, 5 olduğunu düşünelim."
      "Bu dosyayı okumaya çalışalım. Eğer dosya bulunamazsa bir hata mesajı verelim.")
try:
    file = open("test.txt", "r")
    print(file)
except FileNotFoundError:
    print("Dosya bulunamadı!")

