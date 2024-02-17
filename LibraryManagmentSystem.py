class Library:

    def __init__(self):
        #Library sınıfının constructor metodu, burada books.txt dosyası a+ modunda açılıyor.
        self.file = open("books.txt", "a+")
    
    def __del__(self):
        #destructor metodu işimiz bitince dosyanın kapanmasını sağlıyor.
        self.file.close()    
    
    def listBooks(self):
        #kitapların listelenme işleminin gerçekleştirildiği kısım.
        #seek metodu kulanarak mevcut dosyanın başına dçnme işlemi yapılıyor.
        #(birden fazla kez yapılacak olan listeleme işlemi için gerekli)
        self.file.seek(0)
        content = self.file.read() #dosyadan bütün içerik alınıyor.
        books = content.splitlines()#içerik satırlara (yani kitaplara) bölünüyor. 
        print("Kitap Adı\tYazar")
        for book in books:
            bookInfos = book.split(",")#her satır , işaretine göre ayrıştırılıyor buda kitap bilgilerinin ayrıştırılması demek oluyor.
            print(f"{bookInfos[0]}\t{bookInfos[1]}")# sıradaki kitabın adı ve yazar bilgisi yazdırılıyor.

    def addBook(self):
        #kitap ekleme işlemlerinin yapıldığı metot.
        #kitap özellikleri alınıyor.
        name = input("Kitap adı: ")
        author = input("Yazar: ")
        releaseDate = input("Basım Yılı: ")
        page = input("Sayfa Sayısı: ")
        
        newLine = name+","+author+","+releaseDate+","+page+"\n"#kitap bilgileri dosyaya yazılacak hale getiriliyor.

        self.file.write(newLine)#kitabın dosyaya yazdırıldığı kısım.
        print("kitap başarıyla eklendi...")

    def removeBook(self):
        #kitap silme işleminin gerçekleştirildiği metot.
        delName = input("Silinecek kitabın adı:")#silinecek kitabın adı.

        self.file.seek(0)#dosyanın başına dönüş yapılıyor.
        content = self.file.read()#içerik okunuyor.
        lines = content.splitlines()#içerik satırlara bölünüyor.
        books = []#her bir kitabın özelliklerinin liste olarak ekleneceği liste.
        for line in lines:
            book = line.split(",")#satır , ile ayrıştırılarak kitap özelliklerini tutan liste oluşturuldu.
            books.append(book)#kitap özelliklerini tutan liste books listesine eklendi.

        index = 0 #burada silinecek olan kitabın index değeri bulundu.
        for i in range(len(books)):
            if(delName == books[i][0]):
                index = i

        if(index == 0):
            #index değerini default olarak 0 atandığından dolayı silinecek kitap bulunmadığında
            #yani index değeri 0 kaldığında ilk kitabın silinme işlemi gerçekleşir. bu durumun önüne geçmek için
            #index değeri sıfıra eşit ise sıfırıncı indexteki kitap adıyla delName kıyaslanır.
            if(books[index][0] == delName):
                books.pop(index)
        else:#indexin 0 olmadığı durum.
            books.pop(index)
    
        self.file.truncate(0)#algoritma tasarımından dolayı books.txt dosyasının temizlenmesi gerekiyor. işlem burada gerçekleşiyor.

        for book in books:
            #books listesi güncellendikten sonra kitapların yazdırılma işleminin yapıldığı kısım.
            newLine = book[0]+","+book[1]+","+book[2]+","+book[3]+"\n"
            self.file.write(newLine)
        print("Kitap kütüphandeden kaldırıldı....")    
    
    #library classının bittiği kısım.            


lib = Library() #lib nesnesi oluşturuldu.

while(True):
    print("\n*** MENU***\n" 
        "1) List Books\n" 
        "2) Add Book\n" 
        "3) Remove Book\n")
    
    choice = input("Seçiminiz(çıkış için q):")
    if(choice == "1"):
        lib.listBooks()
    elif(choice == "2"):
        lib.addBook()
    elif(choice == "3"):
        lib.removeBook()
    elif(choice == "q"):
        break
    else:
        print("hatalı giriş tekrar deneyiniz....")

lib.__del__()#lib nesnesinin destructor metodunun kullanıldığı kısım.  
