#Proof of Concept : 
Pada fungsi encrypt setiap character dari flag menjalani operasi xor dengan S[(S[i] + S[j]) % 256]  kemudian hasilnya digunakan untuk membaca elemen dari list sbox pada nilai hasil tersebut dan di simpan pada list out. Terakhir fungsi mengembalikan string gabungan elemen dari list out.

Step-by-Step

Dengan menjalankan nc 178.128.113.198 31337 kemudian memasukkan input 1, diperoleh nilai dari encrypt(flag, key).encode('latin1').hex() adalah string dengan panjang 278, yang berarti  encrypt(flag, key) adalah string sepanjang 139. kemudian setiap charnya dipisahkan menjadi elemen dari list out1.
Sekarang kita peroleh bahwa setiap elemen dari list out1 adalah chr(sbox[ord(char) ^ S[(S[i] + S[j]) % 256]]).  Dengan mengkonversi setiap elemennya menjadi bilangan desimal kita peroleh nilai dari setiap elemen list out1 adalah sbox[ord(char) ^ S[(S[i] + S[j]) % 256]]. Selanjutnya untuk memperoleh nilai dari ord(char) ^ S[(S[i] + S[j]) % 256] dibuat sebuah dictionary yang dinamai kamus yang memetakan setiap sbox[i] ke i.

Perhatikan bahwa untuk setiap char dari flag akan dixor dengan nilai S[(S[i] + S[j]) % 256], dengan nilai S[(S[i] + S[j]) % 256] untuk setiap charnya berbeda-beda sehingga diperlukan semua nilai  S[(S[i] + S[j]) % 256] yang digunakan untuk melakukan operasi xor dengan masing-masing char untuk mendecrypt flagnya, selanjutnya nilai  S[(S[i] + S[j]) % 256] untuk setiap charnya akan disebut sebagai key.

dengan menjalankan nc 178.128.113.198 31337 kemudian memasukkan input 2, kita bisa memasukkan input yang akan dienkripsi dengan fungsi encrypt yang sama yg digunakan untuk mengenkripsi flag, maka yang perlu kita lakukan adalah memberikan input string sepanjang 139. dengan langkah yang sama dengan langkah 2, bisa diperoleh ord(char) ^ S[(S[i] + S[j]) % 256] 
Mengingat
char ⊕ key ⊕ char=key
diperoleh nilai key untuk setiap charnya
Terakhir kita tinggal melakukan operasi xor kepada hasil dari Langkah 2, kemudian menggabungkan listnya menjadi string, maka diperoleh flagnya.
