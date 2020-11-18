 # dosya açma operarörü 
file = open("newfile.txt","a",encoding='utf-8')
file.write("abcnd\n") # açılan dosyada yazma operatörü 
file.close() # dosyayı kapatma 

with open("Nextfile.txt","r",encoding='utf-8') as file:
 content= file.read()
 print(content)
 file.seek(10) #10 uncu metoda kadar sil
 print(file.tell())
 content2=file.read()
 print(content2)

