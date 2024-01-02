'''
    Bir dosyayı açmak için open() fonksiyonu kullanılır.
    open() fonksiyonu iki parametre alır. Bunlar dosya adı ve dosya modudur.
    Dosya modları:
        - r: Sadece okuma
        - w: Sadece yazma
        - a: Ekleme (var olan içeriğin sonuna ekleme)
        - r+: Okuma ve yazma
        - w+: Hem okuma hem yazma (dosya içeriğini siler)
        - a+: Hem okuma hem yazma (dosya içeriğinin sonuna ekleme yapar)
'''
# file = open("newfile.txt", "w") # Dosyayı yazma modunda açar.
print("--> Dosya açma işlemi <--")
filePath = "/Users/esalkan/Desktop/roadMaps/ODTU/SEM/BTSP/Python-Core-OOP-RoadMap/Core/08 - File Operations/openAFile.txt" # Dosya yolu
print("\nDosyayı okuma")
file = open(filePath, "r") # Dosyayı okuma modunda açar.

print("\nfile, Dosyanın bilgilerini verir.")
print(file) # Dosyanın bilgilerini verir.

print("\ntype(file), Dosyanın tipini verir.")
print(type(file)) # Dosyanın tipini verir.

print("\nfile.read(), Dosyanın tamamını okur.")
print(file.read()) # Dosyanın tamamını okur.

print("\nfile.readline(), Dosyanın sadece bir satırını okur.")
file.seek(0) # Dosyanın başına gider.

print("\nfile.readlines(), Dosyanın tamamını okur ve her bir satırı bir liste elemanı olarak döndürür.")
print(file.readline()) # Dosyanın sadece bir satırını okur.

print("\nfile.readlines(), Dosyanın tamamını okur ve her bir satırı bir liste elemanı olarak döndürür.")
print(file.readlines()) # Dosyanın tamamını okur ve her bir satırı bir liste elemanı olarak döndürür.

print("\nfor döngüsü, Dosyayı satır satır okur.")
for line in file: # Dosyayı satır satır okur.
    print(line, end="") # Her bir satırı ekrana yazdırır.

print("\nseek(0) ve tell(), Dosyanın başka bir konumuna gider ve hangi konumda olduğunu söyler.")
file.seek(0) # Dosyanın başına gider.

print("\nfile.tell(), Dosyanın hangi konumda olduğunu söyler.")
print(file.read(20)) # Dosyanın ilk 5 karakterini okur.

file.close() # Dosyayı kapatmak için close() fonksiyonu kullanılır.

with open(filePath, "r", encoding="utf-8") as file: # Dosyayı otomatik olarak kapatır.
    print("\nwith, Dosyayı otomatik olarak kapatır.")
    print(file.read())
