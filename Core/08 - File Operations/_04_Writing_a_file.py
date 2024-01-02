'''
    Dosya yazma işlemleri | Writing a file
        - Bir dosyaya yazma işlemi yapmak için open() fonksiyonu kullanılır.
        - open() fonksiyonu iki parametre alır. Bunlar dosya adı ve dosya modudur.
        - Dosyanın yazma modunda açılması için "w" parametresi kullanılır.
        - Dosya yoksa oluşturulur.
        - Dosya varsa içeriği silinir.
        - Dosyaya veri eklemek için write() fonksiyonu kullanılır.
        - write() fonksiyonu her defasında dosyanın sonuna ekler.
        - write() fonksiyonu sadece string parametre alır.
        - write() fonksiyonu ile dosyaya veri eklemek için dosyanın açılması gerekir.
        - Dosyayı kapatmak için close() fonksiyonu kullanılır.
        - Dosyayı otomatik olarak kapatmak için with kullanılır.
        - Dosyaya veri eklemek için a parametresi kullanılır.
        - Dosyaya veri eklemek için a+ parametresi kullanılır.

'''

filePath = "/Users/esalkan/Desktop/roadMaps/ODTU/SEM/BTSP/Python-Core-OOP-RoadMap/Core/08 - File Operations/writeAFile.txt" # Dosya yolu

print("--> Dosya yazma işlemi <--")
file = open(filePath, "w", encoding="utf-8") # Dosyayı yazma modunda açar.
file.write("Python\n") # Dosyaya veri ekler.
file.write("Java\n") # Dosyaya veri ekler.
file.write("Javascript\n") # Dosyaya veri ekler.
file.close() # Dosyayı kapatır.

with open(filePath, "a", encoding="utf-8") as file: # Dosyayı otomatik olarak kapatır.
    file.write("C#\n") # Dosyaya veri ekler.
    file.write("C++\n") # Dosyaya veri ekler.
    file.write("PHP\n") # Dosyaya veri ekler.

with open(filePath, "a+", encoding="utf-8") as file: # Dosyayı otomatik olarak kapatır. Dosyaya veri eklemek için a+ parametresi kullanılır.
    file.write("C#\n") # Dosyaya veri ekler.
    file.write("C++\n") # Dosyaya veri ekler.
    file.write("PHP\n") # Dosyaya veri ekler.
    file.seek(0) # Dosyanın başına gider.
    print(file.read()) # Dosyanın tamamını okur.


