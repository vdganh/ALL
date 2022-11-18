username = 'Vdganh'

password = 'ketapang123'

userInput = input("Masukkan Username?\n")

if userInput == username:
    a=input("Masukkan Password?\n")   
    if a == password:
        print("Selamat Datang!")
        print("SILAHKAN PILIH MENU DIBAWH INI")
        print("[1.] ENSKRIPSI")
        print("[2.] IP-HOST")
        print("[3.] CHAT-BOT")
        print("[4.] Kirim-Pesan-Whatsapp")
        b = input('PILIH ANGKA DIATAS : ')
        if b == '1' :
            abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

            key = int(input('MASUKKAN ANGKA 1 SAMPAI 9 (MISAL 9) : '))

            def encode(kalimat,cipher_key):
                kalimat = kalimat.lower()
                hasil_encode = ''
                for karakter in kalimat:
                    if karakter in abjad:
                        index_lama = abjad.index(karakter)
                        index_baru = (index_lama + cipher_key ) % len(abjad)
                        abjad_baru = abjad[index_baru]
                        hasil_encode = hasil_encode + abjad_baru 
                    else:
                        hasil_encode = hasil_encode + ' ' 
                return hasil_encode

            kalimat = input('MASUKKAN KALIMAT YANG INGIN DI ENSKRIPSI : ')
            # ENKRIPSI
            kalimat_hasil = encode(kalimat,key)
            print('KALIMAT YANG DIMASUKKAN TAMBAHKAN (-) JIKA INGIN MENERJEMAHKAN = : ',kalimat)
            print('HASIL ENSKRIPSI " ',key, ' " ADALAH :', kalimat_hasil)
            # DEKRIPSI (dengan enkripsi ulang menggunakan nilai minus key)
            kalimat_awal = encode(kalimat_hasil,-key)
            print('JIKA HASIL DI ENSKRIPSI ULANG MENGGUNAKAN NILAI NEGATIF DARI SEBELUMNYA MAKA KALIMAT HASILNYA ADALAH',-key, 'ADALAH', kalimat_awal)
        elif b == '2' : #informasi tentang komputer
            print("Ini Informasi Tentang Komputermu!")
            import socket
            hostname=socket.gethostname()
            IPAddr=socket.gethostbyname(hostname)
            print("NAMA KOMPUTER:"+hostname)
            print("IP KOMPUTER:"+IPAddr)
        elif b == '3' :
                import json
                x = open('data.json')
                data = json.load(x)

                print('''
                1. Melatih Bot
                2. Berbicara dengan Bot
                ''')


                while True:
                    input_pertama = input("Masukkan Kode: ")
                    if input_pertama == "1":
                        while True:
                            a = input("User\t: ")
                            if a == "Keluar":
                                break
                            else:
                                b = input("Bot\t: ")
                                data[a] = b
                                b = open('D:\VSC\CODINGAN\PYTHON\BOT WA\data.json', "w")
                                json.dump(data,b)
                                b.close()


                    elif input_pertama == "2":
                        while True:
                            a = input("User\t: ")
                            if a == 'Keluar':
                                break
                            if a in data:
                                print(f'Bot\t: {data[a]}')
                            else:
                                print('Bot\t: Itu kata baru')

                    else:
                        pass
                    #Pesan Whatsapp
        elif b == "4":
            import pywhatkit
            nomer = input('MASUKKAN NOMER : ' )    
            waktu = input('MASUKKAN WAKTU : ')
            print('''CATATATAN PENULISAN WAKTU :( 22,12)
                     PENJELASN : 22 ADALAH JAM DAN 12 ADALAH MENIT''') 
            try:
                # pywhatkit.sendwhatmsg("no hp yang ingin kamu kirim pesannya", "pesannya apa", JAM, Menit)
                # mengirimkan pesan ke no +628xxxxxxx, pesannya adalah hello, jam 19 : 05
                pywhatkit.sendwhatmsg(nomer, "hello", waktu)
                print("success")
            except:
                print("gagal")

        else :
            print('PILIH INPUT YANG BENAR')
else:
    print("USERNAME & PASSWORD SALAH!")
