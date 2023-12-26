print("\n---> Gömülü Fonksiyonlar | Built-in Functions <---")
# Gömülü fonksiyonlar, Python ile birlikte gelen fonksiyonlardır.
print("Example 1 --> Gömülü Fonksiyonlar | Built-in Functions\n abs() Sayının mutlak değerini döndürür\n Returns the absolute value of the number")
print(abs(-4.5))
print(abs(4.5))
print("Program ended | Program sonlandı\n")

print("Example 2 --> Gömülü Fonksiyonlar | Built-in Functions\n all() Tüm elemanlar True ise True, aksi halde False döndürür\n Returns True if all elements are True, otherwise False")
print(all([True, True, True]))
print(all([True, False, True]))
print("Program ended | Program sonlandı\n")

print("Example 3 --> Gömülü Fonksiyonlar | Built-in Functions\n any() Herhangi bir eleman True ise True, aksi halde False döndürür\n Returns True if any element is True, otherwise False")
print(any([True, True, True]))
print(any([True, False, True]))
print("Program ended | Program sonlandı\n")

print("Example 4 --> Gömülü Fonksiyonlar | Built-in Functions\n ascii() Girilen karakterin ascii karşılığını döndürür\n Returns the ascii equivalent of the entered character")
print(ascii('a'))
print(ascii('ş'))
print("Program ended | Program sonlandı\n")

print("Example 5 --> Gömülü Fonksiyonlar | Built-in Functions\n bin() Girilen sayının ikilik tabandaki karşılığını döndürür\n Returns the binary equivalent of the entered number")
print(bin(10))
print(bin(100))
print("Program ended | Program sonlandı\n")

print("Example 6 --> Gömülü Fonksiyonlar | Built-in Functions\n bool() Girilen değerin boolean karşılığını döndürür\n Returns the boolean equivalent of the entered value")
print(bool(0))
print(bool(1))
print(bool(2))
print(bool(-1))
print(bool(''))
print(bool('a'))
print("Program ended | Program sonlandı\n")

print("Example 7 --> Gömülü Fonksiyonlar | Built-in Functions\n bytearray() Girilen değerin byte dizisi karşılığını döndürür\n Returns the byte array equivalent of the entered value")
print(bytearray('a', 'utf-8'))
print(bytearray('ş', 'utf-8'))
print("Program ended | Program sonlandı\n")

print("Example 8 --> Gömülü Fonksiyonlar | Built-in Functions\n bytes() Girilen değerin byte dizisi karşılığını döndürür\n Returns the byte array equivalent of the entered value")
print(bytes('a', 'utf-8'))
print(bytes('ş', 'utf-8'))
print("Program ended | Program sonlandı\n")

print("Example 9 --> Gömülü Fonksiyonlar | Built-in Functions\n callable() Girilen değerin çağrılabilir olup olmadığını döndürür\n Returns whether the entered value is callable")
print(callable(1))
print(callable(print))
print(callable('a'))
print(callable('ş'))
print("Program ended | Program sonlandı\n")

print("Example 10 --> Gömülü Fonksiyonlar | Built-in Functions\n chr() Girilen sayının ascii karşılığını döndürür\n Returns the ascii equivalent of the entered number")
print(chr(97))
print(chr(351))
print("Program ended | Program sonlandı\n")

print("Example 11 --> Gömülü Fonksiyonlar | Built-in Functions\n classmethod() Girilen fonksiyonu sınıf metodu olarak döndürür\n Returns the entered function as a class method")
class Person:
    age = 25

    @classmethod
    def printAge(cls):
        print('The age is:', cls.age)

Person.printAge()
print("Program ended | Program sonlandı\n")

print("Example 12 --> Gömülü Fonksiyonlar | Built-in Functions\n compile() Girilen kodu derler\n Compiles the entered code")
code = 'print("Hello World")'
result = compile(code, 'example', 'exec')
exec(result)
print("Program ended | Program sonlandı\n")

print("Example 13 --> Gömülü Fonksiyonlar | Built-in Functions\n complex() Girilen sayının karmaşık sayı karşılığını döndürür\n Returns the complex number equivalent of the entered number")
print(complex(1))
print(complex(1, 2))
print(complex('1+2j'))
print("Program ended | Program sonlandı\n")

print("Example 14 --> Gömülü Fonksiyonlar | Built-in Functions\n delattr() Girilen nesnenin girilen niteliğini siler\n Deletes the entered attribute of the entered object")
class Person:
    name = 'Adam'

person = Person()
print('Before delete:', person.name)
delattr(Person, 'name')
# print('After delete:', person.name) # AttributeError: 'Person' object has no attribute 'name'
print("Program ended | Program sonlandı\n")

print("Example 15 --> Gömülü Fonksiyonlar | Built-in Functions\n dict() Girilen değerin sözlük karşılığını döndürür\n Returns the dictionary equivalent of the entered value")
print(dict())
print(dict(a='a', b='b', c='c'))
print(dict([('a', 'a'), ('b', 'b'), ('c', 'c')]))
print("Program ended | Program sonlandı\n")

print("Example 16 --> Gömülü Fonksiyonlar | Built-in Functions\n dir() Girilen nesnenin niteliklerini döndürür\n Returns the attributes of the entered object")
class Person:
    name = 'Adam'

person = Person()
print(dir(person))
print("Program ended | Program sonlandı\n")

print("Example 17 --> Gömülü Fonksiyonlar | Built-in Functions\n divmod() Girilen sayıların bölümünü ve kalanını döndürür\n Returns the division and remainder of the entered numbers")
print(divmod(10, 3))
print("Program ended | Program sonlandı\n")

print("Example 18 --> Gömülü Fonksiyonlar | Built-in Functions\n enumerate() Girilen nesnenin numaralandırılmış halini döndürür\n Returns the enumerated version of the entered object")
numbers = ['a', 'b', 'c', 'd']
print(list(enumerate(numbers)))
print(list(enumerate(numbers, start=1)))
print("Program ended | Program sonlandı\n")

print("Example 19 --> Gömülü Fonksiyonlar | Built-in Functions\n eval() Girilen ifadeyi değerlendirir\n Evaluates the entered expression")
x = 1
print(eval('x + 1'))
print("Program ended | Program sonlandı\n")

print("Example 20 --> Gömülü Fonksiyonlar | Built-in Functions\n exec() Girilen ifadeyi çalıştırır\n Runs the entered expression")
x = 1
exec('x = x + 1')
print(x)
print("Program ended | Program sonlandı\n")

print("Example 21 --> Gömülü Fonksiyonlar | Built-in Functions\n filter() Girilen fonksiyonu girilen nesne üzerinde uygular\n Applies the entered function to the entered object")
numbers = [1, 2, 3, 4, 5, 6]
def even(x):
    return x % 2 == 0

print(list(filter(even, numbers)))
print("Program ended | Program sonlandı\n")

print("Example 22 --> Gömülü Fonksiyonlar | Built-in Functions\n float() Girilen değerin ondalıklı sayı karşılığını döndürür\n Returns the decimal number equivalent of the entered value")
print(float(10))
print(float(11.22))
print(float('11.22'))
print("Program ended | Program sonlandı\n")

print("Example 23 --> Gömülü Fonksiyonlar | Built-in Functions\n format() Girilen değeri girilen formata göre biçimlendirir\n Formats the entered value according to the entered format")
print(format(0.5, '%'))
print(format(0.5, '.2%'))
print(format(5, 'b'))
print(format(5, 'c'))
print(format(5, 'd'))
print(format(5, 'o'))
print(format(5, 'x'))
print(format(5, 'n'))
print(format(5, 'e'))
print(format(5, 'f'))
print(format(5, 'g'))
print(format(5, 'E'))
print(format(5, 'F'))
print("Program ended | Program sonlandı\n")

print("Example 24 --> Gömülü Fonksiyonlar | Built-in Functions\n frozenset() Girilen değerin donmuş küme karşılığını döndürür\n Returns the frozen set equivalent of the entered value")
print(frozenset())
print(frozenset([1, 2, 3, 4, 5]))
print("Program ended | Program sonlandı\n")

print("Example 25 --> Gömülü Fonksiyonlar | Built-in Functions\n getattr() Girilen nesnenin girilen niteliğini döndürür\n Returns the entered attribute of the entered object")
class Person:
    name = 'Adam'

person = Person()
print(getattr(person, 'name'))
print("Program ended | Program sonlandı\n")

print("Example 26 --> Gömülü Fonksiyonlar | Built-in Functions\n globals() Küresel değişkenleri döndürür\n Returns global variables")
print(globals())
print("Program ended | Program sonlandı\n")

print("Example 27 --> Gömülü Fonksiyonlar | Built-in Functions\n hasattr() Girilen nesnenin girilen niteliğine sahip olup olmadığını döndürür\n Returns whether the entered object has the entered attribute")
class Person:
    name = 'Adam'

person = Person()
print(hasattr(person, 'name'))
print(hasattr(person, 'age'))
print("Program ended | Program sonlandı\n")

print("Example 28 --> Gömülü Fonksiyonlar | Built-in Functions\n hash() Girilen değerin karma değerini döndürür\n Returns the hash value of the entered value")
print(hash('a'))
print(hash('ş'))
print("Program ended | Program sonlandı\n")

print("Example 29 --> Gömülü Fonksiyonlar | Built-in Functions\n help() Girilen nesnenin yardım belgesini döndürür\n Returns the help document of the entered object")
print(help(list))
print("Program ended | Program sonlandı\n")

print("Example 30 --> Gömülü Fonksiyonlar | Built-in Functions\n hex() Girilen sayının onaltılık tabandaki karşılığını döndürür\n Returns the hexadecimal equivalent of the entered number")
print(hex(10))
print(hex(100))
print("Program ended | Program sonlandı\n")

print("Example 31 --> Gömülü Fonksiyonlar | Built-in Functions\n id() Girilen nesnenin kimliğini döndürür\n Returns the identity of the entered object")
print(id('a'))
print(id('ş'))
print("Program ended | Program sonlandı\n")

print("Example 32 --> Gömülü Fonksiyonlar | Built-in Functions\n input() Kullanıcıdan girdi alır\n Gets input from the user")
print(input('Enter a value: '))
print("Program ended | Program sonlandı\n")

print("Example 33 --> Gömülü Fonksiyonlar | Built-in Functions\n int() Girilen değerin tam sayı karşılığını döndürür\n Returns the integer equivalent of the entered value")
print(int(10))
print(int(11.22))
print(int('11'))
print("Program ended | Program sonlandı\n")

print("Example 34 --> Gömülü Fonksiyonlar | Built-in Functions\n isinstance() Girilen nesnenin girilen sınıfın örneği olup olmadığını döndürür\n Returns whether the entered object is an instance of the entered class")
class Person:
    name = 'Adam'

person = Person()
print(isinstance(person, Person))
print(isinstance(person, str))
print("Program ended | Program sonlandı\n")

print("Example 35 --> Gömülü Fonksiyonlar | Built-in Functions\n issubclass() Girilen sınıfın girilen sınıfın alt sınıfı olup olmadığını döndürür\n Returns whether the entered class is a subclass of the entered class")
class Person:
    name = 'Adam'

class Student(Person):
    pass

print(issubclass(Student, Person))
print(issubclass(Person, Student))
print("Program ended | Program sonlandı\n")

print("Example 36 --> Gömülü Fonksiyonlar | Built-in Functions\n iter() Girilen nesnenin yineleyicisini döndürür\n Returns the iterator of the entered object")
numbers = [1, 2, 3, 4, 5]
print(iter(numbers))
print("Program ended | Program sonlandı\n")

print("Example 37 --> Gömülü Fonksiyonlar | Built-in Functions\n len() Girilen nesnenin uzunluğunu döndürür\n Returns the length of the entered object")
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
print("Program ended | Program sonlandı\n")

print("Example 38 --> Gömülü Fonksiyonlar | Built-in Functions\n list() Girilen nesnenin listeye dönüştürülmüş halini döndürür\n Returns the list version of the entered object")
print(list())
print(list('abc'))
print(list((1, 2, 3)))
print("Program ended | Program sonlandı\n")

print("Example 39 --> Gömülü Fonksiyonlar | Built-in Functions\n locals() Yerel değişkenleri döndürür\n Returns local variables")
print(locals())
print("Program ended | Program sonlandı\n")

print("Example 40 --> Gömülü Fonksiyonlar | Built-in Functions\n map() Girilen fonksiyonu girilen nesne üzerinde uygular\n Applies the entered function to the entered object")
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2

print(list(map(square, numbers)))
print("Program ended | Program sonlandı\n")

print("Example 41 --> Gömülü Fonksiyonlar | Built-in Functions\n max() Girilen nesnenin en büyük elemanını döndürür\n Returns the largest element of the entered object")
numbers = [1, 2, 3, 4, 5]
print(max(numbers))
print("Program ended | Program sonlandı\n")

print("Example 42 --> Gömülü Fonksiyonlar | Built-in Functions\n memoryview() Girilen nesnenin bellek görünümünü döndürür\n Returns the memory view of the entered object")
print(memoryview(b'abc'))
print("Program ended | Program sonlandı\n")

print("Example 43 --> Gömülü Fonksiyonlar | Built-in Functions\n min() Girilen nesnenin en küçük elemanını döndürür\n Returns the smallest element of the entered object")
numbers = [1, 2, 3, 4, 5]
print(min(numbers))
print("Program ended | Program sonlandı\n")

print("Example 44 --> Gömülü Fonksiyonlar | Built-in Functions\n next() Girilen nesnenin bir sonraki elemanını döndürür\n Returns the next element of the entered object")
numbers = [1, 2, 3, 4, 5]
numberIterator = iter(numbers)
print(next(numberIterator))
print(next(numberIterator))
print(next(numberIterator))
print(next(numberIterator))
print(next(numberIterator))
# print(next(numberIterator)) # StopIteration
print("Program ended | Program sonlandı\n")

print("Example 45 --> Gömülü Fonksiyonlar | Built-in Functions\n object() Girilen nesnenin boş bir nesne oluşturulmuş halini döndürür\n Returns the empty object version of the entered object")
print(object())
print("Program ended | Program sonlandı\n")

print("Example 46 --> Gömülü Fonksiyonlar | Built-in Functions\n oct() Girilen sayının sekizlik tabandaki karşılığını döndürür\n Returns the octal equivalent of the entered number")
print(oct(10))
print(oct(100))
print("Program ended | Program sonlandı\n")

print("Example 47 --> Gömülü Fonksiyonlar | Built-in Functions\n open() Girilen dosyayı açar\n Opens the entered file")
# file = open('example.txt', 'r')
# print(file.read())
# file.close()
print("Program ended | Program sonlandı\n")

print("Example 48 --> Gömülü Fonksiyonlar | Built-in Functions\n ord() Girilen karakterin ascii karşılığını döndürür\n Returns the ascii equivalent of the entered character")
print(ord('a'))
print(ord('ş'))
print("Program ended | Program sonlandı\n")

print("Example 49 --> Gömülü Fonksiyonlar | Built-in Functions\n pow() Girilen sayının girilen üssünü döndürür\n Returns the entered number to the entered power")
print(pow(2, 3))
print(pow(2, 3, 3))
print("Program ended | Program sonlandı\n")

print("Example 50 --> Gömülü Fonksiyonlar | Built-in Functions\n print() Girilen değeri yazdırır\n Prints the entered value")
print('Hello World')
print("Program ended | Program sonlandı\n")

print("Example 51 --> Gömülü Fonksiyonlar | Built-in Functions\n property() Girilen fonksiyonu özellik olarak döndürür\n Returns the entered function as a property")
class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('Getting name')
        return self._name

    def setName(self, value):
        print('Setting name to ' + value)
        self._name = value

    def delName(self):
        print('Deleting name')
        del self._name

    name = property(getName, setName, delName, 'Name property.') # property(fget, fset, fdel, doc)

person = Person('Adam') # Person.__init__(person, 'Adam')
print(person.name) # person.getName()
person.name = 'John' # setattr(person, 'name', 'John')
del person.name # delattr(person, 'name')
print("Program ended | Program sonlandı\n")

print("Example 52 --> Gömülü Fonksiyonlar | Built-in Functions\n range() Girilen sayıya kadar olan sayıları döndürür\n Returns the numbers up to the entered number")
print(list(range(5))) # 5'e kadar
print(list(range(1, 5))) # 1'den 5'e kadar
print(list(range(1, 5, 2))) # 1'den 5'e kadar 2'şer artarak
print("Program ended | Program sonlandı\n")

print("Example 53 --> Gömülü Fonksiyonlar | Built-in Functions\n repr() Girilen değerin temsilini döndürür\n Returns the representation of the entered value")
print(repr('a')) # 'a'
print(repr('ş')) # '\u015f'
print("Program ended | Program sonlandı\n")

print("Example 54 --> Gömülü Fonksiyonlar | Built-in Functions\n reversed() Girilen nesnenin tersini döndürür\n Returns the reverse of the entered object")
numbers = [1, 2, 3, 4, 5]
print(list(reversed(numbers))) # [5, 4, 3, 2, 1]
print("Program ended | Program sonlandı\n")

print("Example 55 --> Gömülü Fonksiyonlar | Built-in Functions\n round() Girilen sayıyı girilen basamak sayısına göre yuvarlar\n Rounds the entered number to the entered number of digits")
print(round(10.2)) # 10
print(round(10.5)) # 10
print(round(10.6)) # 11
print(round(10.2, 1)) # 10.2
print(round(10.5, 1)) # 10.5
print(round(10.6, 1)) # 10.6
print(round(10.2, 0)) # 10.0
print(round(10.5, 0)) # 10.0
print(round(10.6, 0)) # 11.0
print("Program ended | Program sonlandı\n")

print("Example 56 --> Gömülü Fonksiyonlar | Built-in Functions\n set() Girilen nesnenin küme karşılığını döndürür\n Returns the set equivalent of the entered object")
print(set())
print(set('abc'))
print(set([1, 2, 3, 4, 5]))
print("Program ended | Program sonlandı\n")

print("Example 57 --> Gömülü Fonksiyonlar | Built-in Functions\n setattr() Girilen nesnenin girilen niteliğini girilen değere eşitler\n Sets the entered attribute of the entered object to the entered value")
class Person:
    name = 'Adam'

person = Person()
print(person.name)
setattr(person, 'name', 'John')
print(person.name)
print("Program ended | Program sonlandı\n")

print("Example 58 --> Gömülü Fonksiyonlar | Built-in Functions\n slice() Girilen nesnenin girilen dilimini döndürür\n Returns the entered slice of the entered object")
numbers = [1, 2, 3, 4, 5]
print(numbers[slice(2)])
print(numbers[slice(1, 3)])
print(numbers[slice(1, 5, 2)])
print("Program ended | Program sonlandı\n")

print("Example 59 --> Gömülü Fonksiyonlar | Built-in Functions\n sorted() Girilen nesnenin sıralanmış halini döndürür\n Returns the sorted version of the entered object")
numbers = [4, 2, 3, 1, 5]
print(sorted(numbers))
print("Program ended | Program sonlandı\n")

print("Example 60 --> Gömülü Fonksiyonlar | Built-in Functions\n staticmethod() Girilen fonksiyonu statik metod olarak döndürür\n Returns the entered function as a static method")
class Person:
    age = 25

    @staticmethod
    def printAge():
        print('The age is:', Person.age)

Person.printAge()
print("Program ended | Program sonlandı\n")

print("Example 61 --> Gömülü Fonksiyonlar | Built-in Functions\n str() Girilen değerin karakter dizisi karşılığını döndürür\n Returns the string equivalent of the entered value")
print(str(10))
print(str(11.22))
print(str('11'))
print("Program ended | Program sonlandı\n")

print("Example 62 --> Gömülü Fonksiyonlar | Built-in Functions\n sum() Girilen nesnenin elemanlarının toplamını döndürür\n Returns the sum of the elements of the entered object")
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print("Program ended | Program sonlandı\n")

print("Example 63 --> Gömülü Fonksiyonlar | Built-in Functions\n super() Girilen sınıfın üst sınıfını döndürür\n Returns the superclass of the entered class")
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number

student = Student('Adam', 1)
print(student.name)
print(student.number)
print("Program ended | Program sonlandı\n")

print("Example 64 --> Gömülü Fonksiyonlar | Built-in Functions\n tuple() Girilen nesnenin demet karşılığını döndürür\n Returns the tuple equivalent of the entered object")
print(tuple())
print(tuple('abc'))
print(tuple([1, 2, 3, 4, 5]))
print("Program ended | Program sonlandı\n")

print("Example 65 --> Gömülü Fonksiyonlar | Built-in Functions\n type() Girilen nesnenin türünü döndürür\n Returns the type of the entered object")
print(type(10))
print(type(11.22))
print(type('11'))
print(type([1, 2, 3, 4, 5]))
print("Program ended | Program sonlandı\n")

print("Example 66 --> Gömülü Fonksiyonlar | Built-in Functions\n vars() Girilen nesnenin sözlük karşılığını döndürür\n Returns the dictionary equivalent of the entered object")
class Person:
    name = 'Adam'

person = Person()
print(vars(person))
print("Program ended | Program sonlandı\n")

print("Example 67 --> Gömülü Fonksiyonlar | Built-in Functions\n zip() Girilen nesnelerin elemanlarını birleştirir\n Merges the elements of the entered objects")
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
print(list(zip(numbers, letters)))
print("Program ended | Program sonlandı\n")