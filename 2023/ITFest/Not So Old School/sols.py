from pwn import *


sbox = [98, 56, 7, 192, 121, 149, 107, 246, 120, 132, 191, 152, 229, 238, 94, 106, 176, 170, 161, 253, 145, 181, 237, 211, 219, 250, 131, 190, 158, 24, 126, 32, 79, 212, 244, 53, 60, 183, 83, 128, 162, 137, 15, 148, 50, 51, 166, 92, 171, 88, 44, 242, 69, 91, 101, 103, 175, 3, 82, 40, 245, 110, 34, 143, 248, 35, 109, 115, 227, 47, 140, 122, 193, 59, 39, 243, 208, 55, 165, 213, 224, 231, 96, 185, 151, 100, 105, 12, 66, 42, 160, 214, 205, 189, 130, 5, 147, 20, 236, 85, 142, 194, 2, 228, 124, 215, 14, 26, 240, 223, 154, 203, 54, 25, 141, 200, 8, 111, 177, 0, 75, 73, 204, 80, 230, 58, 112, 10, 52, 157, 116, 41, 4, 217, 18, 9, 174, 27, 226, 163, 36, 13, 167, 72, 241, 21, 186, 30, 87, 221, 168, 89, 239, 29, 178, 179, 249, 45, 195, 57, 95, 22, 180, 153, 129, 108, 201, 202, 63, 68, 64, 135, 207, 156, 133, 220, 11, 71, 6, 233, 232, 119, 173, 90, 102, 117, 136, 86, 247, 76, 234, 164, 172, 184, 78, 225, 125, 199, 46, 210, 216, 123, 31, 235, 182, 251, 38, 206, 139, 197, 159, 127, 150, 61, 16, 19, 28, 198, 93, 77, 49, 169, 1, 114, 134, 187, 188, 67, 113, 74, 218, 104, 254, 65, 196, 155, 144, 209, 37, 81, 70, 48, 43, 84, 138, 62, 17, 23, 222, 118, 146, 33, 99, 252, 97]
kamus={}
for i in range(len(sbox)):
    kamus.update({sbox[i] : i})


target = remote("178.128.113.198", 31337)
target.sendline(b'1')
enc_flag=target.recvline_startswith(b'>').decode()[2:] #menyimpan output hasil enkripsi flag
target.sendline(b'2')


input1=['a']*30
input2=['b']*30
input3=['c']*19
input=input1+input2+input1+input2+input3
key_key_join=''.join(input) #input flag pengganti yang akan digunakan


for i in range(len(input)):
    input[i]=ord(input[i]) #mengubah elemen dari string menjadi ascii number


target.sendline(key_key_join.encode())
input_key_flag=target.recvline_startswith(b'>').decode()[27:] #menyimpan output flag pengganti


#pembuatan key nya
input_key_flag=bytes.fromhex(input_key_flag).decode('latin1')
input_list_key_flag=list(input_key_flag)
for i in range(len(input_list_key_flag)):
    input_list_key_flag[i]=kamus[ord(input_list_key_flag[i])]


final_key=[0]*139
for i in range(len(final_key)):
    final_key[i]=input_list_key_flag[i]^input[i]


#decrypt flagnya
enc_flag=bytes.fromhex(enc_flag).decode('latin1')
enc_list_flag=list(enc_flag)
for i in range(len(enc_list_flag)):
    enc_list_flag[i]=kamus[ord(enc_list_flag[i])]
   
flag_list=[0]*139


for i in range(len(enc_list_flag)):
    flag_list[i]=chr(enc_list_flag[i]^final_key[i])
   
flag=''.join(flag_list)
print(flag)
