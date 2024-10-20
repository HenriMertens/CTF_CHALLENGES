
# CEREALKILLER01: 25 Points

For this challenge we get a zip file containing a binary, if we run it with random input it returns: `ACCESS DENIED!!!`

To solve this I first opened the file in ghidra to see what was going on (I also tried renaming some of the functions):

![ck1 0](https://github.com/user-attachments/assets/eb76067e-f74b-4ba7-a7f4-845a83eb27e9)

After trying to reverse the binary from scratch I realized the flag is returned to us as cleartext output (probably), this means that we hopefully just need to bypass the "if statement".

If you try do this by changing ```if (iVar3 == 0)``` to ```if (iVar3 == 1)```, this will not work since the decryption of the flag is still based of our output.

However we can try to change the strcmp function:
![image](https://github.com/user-attachments/assets/fe16e913-b44b-44e5-8951-ae2e54440c28)

If we set local4b7 = "obboreel", the if statement will be true and "obboreel" will be used for the decryption.

To to do this you can patch the binary or use gdb, I used gdb.

1) Open up the prograam and press `start`
2) Set breakpoint at cmp statement: `breakrva 0x17b0` and press continue
3) It will ask for the password, just enter random stuff.
4) You will hit the breakpoint and see (if you dont have pwngdb you will not see this and will have to inspect registers and stuff):
![image](https://github.com/user-attachments/assets/47f05de9-feda-4cad-a88c-13b4c31eba68)

5) Now we just need to change "vbrmnlrm" to "obboreel": ```set {char[9]} 0xffffce59 = "obboreel"``` and press continue
 ![ck1 1](https://github.com/user-attachments/assets/4a495b66-a5a2-4bf3-b1bb-ecdc7b80ae32)
