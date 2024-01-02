'''
    Reading a file  | Dosya okuma

    - Dosya Okuma Modları
        - with open("newfile.txt", "r", encoding="utf-8") as file: # Dosya okuma modunda açar.
        - seek(): Imleci istenilen indise götürür.
        - tell(): Imlecin hangi indiste olduğunu söyler.
'''
filePath = "/Users/esalkan/Desktop/roadMaps/ODTU/SEM/BTSP/Python-Core-OOP-RoadMap/Core/08 - File Operations/readAFile.txt" # Dosya yolu

with open(filePath, "r") as file: # Dosya okuma modunda açar
    print("\nfile.tell()", file.tell()) # Imlecin hangi indiste olduğunu söyler.
    print("\nfile.seek(20)", file.seek(20)) # Imleci istenilen indise götürür.
    print("\nfile.read(3)", file.read(50)) # Dosyanın ilk 50 karakterini okur.
    print("\nfile.readline()", file.readline()) # Dosyanın sadece bir satırını okur.
    print("\nfile.readlines()", file.readlines()) # Dosyanın tamamını okur ve her bir satırı bir liste elemanı olarak döndürür.

print("for ile dosyayı satır satır okuma | reading a file line by line with for loop")
for line in open(filePath, "r"): # Dosyayı satır satır okur.
    print(line, end="") # Her bir satırı ekrana yazdırır.



