#!/usr/bin/python2
# (C) Copyrigth 2006 Authentic Exploit
# Make you real a Programer
# Don't change Author Please

        # My link >> https://www.facebook.com/ReaperXD277
        # Thanks for used my script
        # Coded by Reaper Official ( Reza Alfauzan )
        # Module
import os,sys,random,time,getpass
### WARNA RANDOM ###

t = "0ahUKEwin2M64oKr2AhULSmwGHVNjDOcQ4dUDCA0tX4si3a6408j50XMpT0yWM"

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
G = '\33[33;7m'  # KUNING TEPAK
V = '\x1b[1;90m' # HITAM
my_color = [
 P, M, H, K, B, U, O, N, G, V]

# Start

### LOGO LOGIN ###
hensem = """
[+]=============[----------]=============[+]
[+] Anda harus masuk menggunakan token   [+]
[+] Download tokennya dahulu ges ya      [+]
[__________________________________________]
(===============[||||||||||]===============)

                        [ Website ]
                        [ https://www.mediafire.com/file/n51z27ftdef5s3t/Initokennya.txt.txt/file ]
"""
def auto(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.05)

def login():
        os.system("clear")
        os.system("toilet -f small -F gay TOKEN | lolcat -a -d 5")
        print hensem
        time.sleep(2)
        token = getpass.getpass("Masukkan Token : \x1b[2;90m")
        if token ==t:
                auto("Token Benar!!")
                time.sleep(1.5)
        else:
                auto("Token salah!!!, Download token dulu slurr")
                time.sleep(1.5)
                login()
if __name__ == "__main__":
        login()


def nanya():
        bertanya = raw_input("Apakah anda ingin kembali? [Y/n] : ")
        if bertanya =="Y" or bertanya =='y':
                time.sleep(2)
                main()
        if bertanya =="N" or bertanya =='n':
                titik()
                time.sleep(1.5)
                auto("\nGoodbye My Friend :)")
                exit()
        if bertanya =="" or bertanya =='':
                auto("Tolol Jangan kosong belegu!!")
                raw_input("Kembali [ ENTER ]")
                os.system("")
                nanya()
        else:
                print "Anak tolol anjing sia belegu"%()
                nanya();time.sleep(2)

def titik():
        babi = [".","..","...",".","..","..."]
        for x in babi:
                print "\rMohon menunggu %s"%(x),
                sys.stdout.flush()
                time.sleep(1.5)


def main():
        os.system("clear")
        time.sleep(3)
        os.system("toilet -f small -F gay M I N I ToolS")
        print "%s______________%s______________"%(O,V)
        print "%s[%s+%s] %sAuthor %s: %sReaper XD   %s[%s+%s]"%(V,O,V,O,N,M,V,O,V)
        print "%s[%s+%s] %sGithub %s: %sReaper-XD   %s[%s+%s]"%(V,O,V,O,N,M,V,O,V)
        print "%s[%s+%s] %sThis Script Nice!!   %s[%s+%s]"%(V,O,V,O,V,O,V)
        print "%s______________%s______________"%(V,O)
        print "";time.sleep(4)
        print "%s(%s01%s). %sPerk%salian"%(N,O,N,U,K);time.sleep(0.03)
        print "%s(%s02%s). %sPert%sambahan"%(N,O,N,U,K);time.sleep(0.03)
        print "%s(%s03%s). %sPemb%sagian"%(N,O,N,U,K);time.sleep(0.03)
        print "%s(%s04%s). %sPeng%surangan"%(N,O,N,U,K);time.sleep(0.03)
        print "%s(%s00%s). %sKelu%sar%s"%(N,O,N,U,K,N);time.sleep(0.03)
        kali = raw_input("\nPilih mana gan : ")
        if kali =="1" or kali =='01':
                angka1 =int(input("Angka Pertama : "))
                angka2 =int(input("Angka Kedua : "))
                print(angka1 * angka2)
                nanya()
        elif kali =="2" or kali =='02':
                angka1 =int(input("Angka Pertama : "))
                angka2 =int(input("Angka Kedua : "))
                print(angka1 + angka2)
                nanya()
        elif kali =="3" or kali =='03':
                angka1 =int(input("Angka Pertama : "))
                angka2 =int(input("Angka Kedua : "))
                print(angka1 / angka2)
                nanya()
        elif kali =="4" or kali =='04':
                angka1 =int(input("Angka Pertama : "))
                angka2 =int(input("Angka Kedua : "))
                print(angka1 - angka2)
                nanya()
        elif kali =="0" or kali =='00':
                auto("Goodbye my friend :)")
                time.sleep(2)
                exit()
        else:
                auto("Salah!, masukkan Input dengan benar!")
                raw_input("Kembali [ ENTER ] ");main()
main()
