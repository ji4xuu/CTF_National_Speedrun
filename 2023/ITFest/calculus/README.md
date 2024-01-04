#Chall : diberikan chall.py dan output.txt.

#Proof of Concept : 
fungsi encrypt mengambil sebuah string kemudian dikonversi menjadi long number disimpan dalam variabel val, menginisiasi dua bilangan prima acak (a, b) kedalam list Set, dan 1 bilangan prima lainnya sebagai p dan menuliskan variabel n=23+24, x=a+b, z=ab+pow(p, 2, n), y=a2+b2. Kemudian hasil enkripsi diperoleh dengan operasi xor terhadap a3+b3 kemudian dikalikan dengan (x+y) diakhiri dengan mengubahnya dalam format hex. Diakhir fungsi encrypt mengembalikan [x, z, enc]. Maka kita punyai informasi nilai x, z, enc.

Step-by-Step
pertama ubah enc dari basis 16 menjadi basisa 10. Kemudian perhatikan bahwa z=ab+pow(p, 2, n), dimana nilai n adalah 24 perhatikan bahwa untuk sembarang bilangan bulat p pasti memenuhi p^2= 0, 1 mod 3, p^2= 0, 1, 4 mod 8
tinjau bahwa bilangan prima lebih dari 3 dipastikan p^2 = 1 mod 3, p^2= 1 mod 8 dengan konsep keterbagian p^2 = 1 mod 24. sehingga nilai pow(p, 2, n)=1.
dengan demikian bisa diperoleh nilai (a, b) mengikuti pendekatan berikut : 
x=a+b, z-1=ab 
x^2-4(z-1)=(a+b)^2-4ab=a^2-2ab+b2=(a-b)^2
sqrt(x^2 -4(z-1))=a-b
sqrt(x^2 -4(z-1))+x=(a-b)+(a+b)=2a 
[sqrt(x^2 -4(z-1))+x]/2=a, b=(z-1)/a
diperoleh juga val=(encx+y)⊕(a3+b3).  Terakhir tinggal mengubah dari long number menjadi string.

