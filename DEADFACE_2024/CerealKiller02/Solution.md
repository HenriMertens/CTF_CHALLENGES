
# CEREALKILLER02: 250 Points

For this challenge we also get a zip file containing a binary, unzipping and running it gives: ```ACCESS DENIED!!!```

To solve this I will use same methodology as Cearealkiller01, opening it up in ghidra gives:

![image](https://github.com/user-attachments/assets/ec152548-a3ce-411f-9834-8f9575584b3c)

We can see lots of stuff being initialized, lots of decrypting, however we dont care.

As I said I tried the same stuff a cereal01 first:

1) Open it up in gdb, start the binary and set breakpoint at cmp statement: ```breakrva 0x177f```

![image](https://github.com/user-attachments/assets/1e191381-0b6b-4043-8b5a-49ee277c1564)

2) We see 2 values being compared, however we dont knwo which one we should change:
   
 ![image](https://github.com/user-attachments/assets/fb1f8eec-1e83-4861-ae30-ac63641e190a)
 
   To figure this out, we just run it again with a different random password:
   
![image](https://github.com/user-attachments/assets/e6bbcbc8-e093-422f-87e7-1ef5185455ec)

3) We can see the "0xda866e97" stays the same so we should change "0xb3dd8bde"
4) To do this, this time we cant just `set {char}.... ` (I tried), because "0xda866e97" isnt the only part of the password, it continues further:
   
![image](https://github.com/user-attachments/assets/a77a6b43-e5f0-4ecf-bc3b-07ef0280faf2)

5) To circumvent this you can change the all the 16 bytes to the right password or change the pointer, I went with pointer.
   
   ![image](https://github.com/user-attachments/assets/75e7a2d5-52ca-47e7-a6e1-733626dc8a7f)

6) we want to make 0xffffcd50 point to 0xffffce34: ```set {int} 0xffffcd50 = 0xffffce34 ```
7) Press continue and voila:

![image](https://github.com/user-attachments/assets/b937ef34-c103-487b-9e31-c1b2b86ff4b2)



