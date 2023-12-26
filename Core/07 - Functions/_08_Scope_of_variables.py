print("\n---> Değişkenlerin kapsamı | Scope of variables <---")
# Değişkenlerin kapsamı, değişkenlerin hangi kod bloklarında kullanılabileceğini belirler.
# Local scope: Değişkenler, tanımlandıkları kod bloklarında kullanılabilir.
# Enclosing scope: Değişkenler, tanımlandıkları kod bloklarının alt kod bloklarında kullanılabilir.
# Global scope: Değişkenler, tanımlandıkları kod bloklarının üst kod bloklarında kullanılamaz.
# Built-in scope: Değişkenler, tanımlı olan gömülü fonksiyonlarda kullanılamaz.

print("Example 1 --> Değişkenlerin kapsamı | Scope of variables\n Local scope: Değişkenler, tanımlandıkları kod bloklarında kullanılabilir.\n Local scope: Variables can be used in the code blocks where they are defined.")
def function():
    number = 10
    print(number)

function()
# print(number) # NameError: name 'number' is not defined
print("Program ended | Program sonlandı\n")

print("Example 2 --> Değişkenlerin kapsamı | Scope of variables\n Enclosing scope: Değişkenler, tanımlandıkları kod bloklarının alt kod bloklarında kullanılabilir.\n Enclosing scope: Variables can be used in the sub code blocks of the code blocks where they are defined.")
def function():
    number = 10

    def function2():
        print(number)

    function2()

function()
# print(number) # NameError: name 'number' is not defined
print("Program ended | Program sonlandı\n")

print("Example 3 --> Değişkenlerin kapsamı | Scope of variables\n Global scope: Değişkenler, tanımlandıkları kod bloklarının üst kod bloklarında kullanılamaz.\n Global scope: Variables cannot be used in the upper code blocks of the code blocks where they are defined.")
def function():
    number = 10

    def function2():
        print(number)

    function2()

function()
# print(number) # NameError: name 'number' is not defined
print("Program ended | Program sonlandı\n")

print("Example 4 --> Değişkenlerin kapsamı | Scope of variables\n Built-in scope: Değişkenler, tanımlı olan gömülü fonksiyonlarda kullanılamaz.\n Built-in scope: Variables cannot be used in the built-in functions where they are defined.")
def function():
    number = 10

    def function2():
        print(number)

    function2()

function()
# print(number) # NameError: name 'number' is not defined
print("Program ended | Program sonlandı\n")

