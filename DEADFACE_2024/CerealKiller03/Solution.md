# CEREALKILLER03: 500 Points

For this challnge I used the same methodology aswell.
Starting off with opening the binary in ghidra and analyzing it:

![image](https://github.com/user-attachments/assets/aebfbb46-b110-4688-bfab-725f823ec83f)

1) Same as before, set breakpoint at cmp statement: ```breakrva 0x1506``` in gdb 
2) Enter a random password and see what happens:

![image](https://github.com/user-attachments/assets/d2d40660-da1a-4e00-98f5-1fa735bcd6f7)

3) Again, we see two values being compared but we dont know which one of these we should change.
   So  we run it again with different password:

   ![image](https://github.com/user-attachments/assets/f60b4e11-b9ce-4ddb-bb7f-fe7d5439ea05)

4) "0xa8bc8ec" Stayed the same so we should change "0x223550f5", again I will do this by changing the pointer: ```set {int} 0xffffcda0 = 0xffffce78```
5) Press continue and see the flag appear:

![image](https://github.com/user-attachments/assets/1f29ddc0-34c9-4d01-b0a6-b90a584d9118)

Or not lol, wth is this

6) Back to ghidra to see what I did wrong:
```c
  local_468 = 0xa8bc8ec;
  local_464 = 0x535302f9;
  local_460 = 0x970670e8;
  local_45c = 0xdc3f2f4b;
```
 ```c
     iVar1 = memcmp(local_478,&local_468,0x10);
  if (iVar1 == 0) {
    puts("\n");
    puts("TOP SEEKWET ACCESS GRANTED, MR. PRESIDENT!!!");
    printf("Here is your NUKULAR CODE! (Note: It only works ONCE!) Have a nice breakfast, sir! ");
    puts("\n\n*********** KABOOM!!! ***********\n");
    RC4((RC4_KEY *)local_458,0x21,local_478,(uchar *)0x10);
    local_415 = 0;
    printf("%s",local_436);
    puts("\n\n*********** KABOOM!!! ***********\n");
  }
   ```
  We can see the cmp statement comparing between a predetermined value and local478, it doesnt take a genius to figure out local478 will be related to our input.
  
  The problem lies within how our flag is decrypted, it uses this local478 (which is still some random stuff we gave it) so it it will be completely wrong.

  To fix this, I found out where lcoal478 and local468 (the right answer) are saved:
  
  ![image](https://github.com/user-attachments/assets/40307d1a-b827-4e0b-b71a-c0f906ebee5a)

  Next I patched this the local478 to be local468 in the decryption step
  
  FROM THIS:
  ![image](https://github.com/user-attachments/assets/6e6f3368-be75-4745-8bfb-f0ab1a3afa8c)

  TO THIS:
  ![image](https://github.com/user-attachments/assets/e5605ccc-944d-4fda-a4b7-e423fedf8d83)


7) Now just export the binary: file>export program>orginal file, change name to something like ck_patched
8) Okay, hopefully problem is fixed now, just reapeat the same steps as before on this file and get:
   
![image](https://github.com/user-attachments/assets/479da222-f622-4739-81de-c50c52309a4b)

9) Note: I had to patch because I change the pointer, if you change the bytes of local478 directly you probably get the right answer first try

   
