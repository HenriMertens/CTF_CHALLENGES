CEREALKILLER05: 200 Points

For this challnege we get a .jar file, we can extract the contents by using the unzip command.
After this we find two files, a meta-inf (not interesting) and a RE08.class.
We can use jd-gui to decompile this class: `jd-gui RE08.class`

That gives:
```java
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.util.Base64;
import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class RE08 {
  private static final byte[] encryptedURL = new byte[] { 
      42, 6, 68, 64, 7, 120, 93, 31, 83, 17, 
      48, 23, 81, 92, 90, 46, 11, 68, 68, 27, 
      44, 30, 81, 82, 7, 108, 29, 66, 87, 91, 
      33, 23, 66, 85, 21, 46, 1, 31, 86, 6, 
      45, 29, 68, 82, 6, 45, 29, 68, 30, 30, 
      50, 23, 87 };
  
  private static final String encryptedFlag = "Tj/BJ+45Z45uRCFpuFOHirQI34ZC7bmtpCtJ3OE613fIxqrsZwIoLNSBXSjtPONFqZF3gC+4glh1Gyi2RBKZcuItH8s=";
  
  private static final String ivBase64 = "qHttv1t5TWZLDM4e";
  
  public static void main(String[] paramArrayOfString) {
    try {
      Scanner scanner = new Scanner(System.in);
      System.out.print("President Donald Trump has a favorite cereal.  It is great... really great...\n");
      System.out.print("The reason it is so great, is because HE likes it... that makes it reall great...\n");
      System.out.print("Of course, to maintain utmost secrecy, it is protected with a password that is\n");
      System.out.print("HIGHLY secure (and backed up securely on a piece of paper somewhere in Mar Lago...)\n");
      System.out.print("Now, you, being a highly trained hacker, should be able to BYPASS this security and\n");
      System.out.print("discover what President Trump's favorite monster cereal is.\n");
      System.out.print("\n");
      System.out.print("Enter password: ");
      String str1 = scanner.nextLine();
      byte[] arrayOfByte = decryptURL(encryptedURL, str1);
      String str2 = new String(arrayOfByte);
      if (str2.startsWith("https")) {
        System.out.println("Decrypted URL: " + str2);
        String str3 = downloadImage(str2);
        byte[] arrayOfByte1 = calculateSHA256(str3);
        String str4 = decryptFlagWithAESGCM(arrayOfByte1, "Tj/BJ+45Z45uRCFpuFOHirQI34ZC7bmtpCtJ3OE613fIxqrsZwIoLNSBXSjtPONFqZF3gC+4glh1Gyi2RBKZcuItH8s=", "qHttv1t5TWZLDM4e");
        System.out.println("Decrypted Flag: " + str4);
      } else {
        System.out.println("Sorry, that is not the correct password.");
      } 
    } catch (Exception exception) {
      exception.printStackTrace();
    } 
  }
  
  private static byte[] decryptURL(byte[] paramArrayOfbyte, String paramString) {
    byte[] arrayOfByte = new byte[paramArrayOfbyte.length];
    for (byte b = 0; b < paramArrayOfbyte.length; b++)
      arrayOfByte[b] = (byte)(paramArrayOfbyte[b] ^ paramString.charAt(b % paramString.length())); 
    return arrayOfByte;
  }
  
  private static String downloadImage(String paramString) throws IOException {
    URL uRL = new URL(paramString);
    String str = "downloaded_image.jpg";
    File file = new File(str);
    if (file.exists())
      file.delete(); 
    InputStream inputStream = uRL.openStream();
    try {
      Files.copy(inputStream, Paths.get(str, new String[0]), new java.nio.file.CopyOption[0]);
      if (inputStream != null)
        inputStream.close(); 
    } catch (Throwable throwable) {
      if (inputStream != null)
        try {
          inputStream.close();
        } catch (Throwable throwable1) {
          throwable.addSuppressed(throwable1);
        }  
      throw throwable;
    } 
    return str;
  }
  
  private static byte[] calculateSHA256(String paramString) throws Exception {
    MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
    byte[] arrayOfByte = Files.readAllBytes(Paths.get(paramString, new String[0]));
    return messageDigest.digest(arrayOfByte);
  }
  
  private static String decryptFlagWithAESGCM(byte[] paramArrayOfbyte, String paramString1, String paramString2) throws Exception {
    byte[] arrayOfByte1 = Base64.getDecoder().decode(paramString2);
    byte[] arrayOfByte2 = Base64.getDecoder().decode(paramString1);
    SecretKeySpec secretKeySpec = new SecretKeySpec(paramArrayOfbyte, "AES");
    Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
    GCMParameterSpec gCMParameterSpec = new GCMParameterSpec(128, arrayOfByte1);
    cipher.init(2, secretKeySpec, gCMParameterSpec);
    byte[] arrayOfByte3 = cipher.doFinal(arrayOfByte2);
    return new String(arrayOfByte3, "UTF-8");
  }
}
```
We can follow the execution flow by seeing what the main function does:
1) Asks for a password and stores it in str1:
   ```java
   String str1 = scanner.nextLine();```
2) Tries to decrypt the url based on your string and store it as bytearray:
   ```java
   byte[] arrayOfByte = decryptURL(encryptedURL, str1);``` 
3) Convert the array of bytes to a string (str2) and check if it start with "https":
   ```java
    if (str2.startsWith("https")) ```
   
5) After this an image get downloaded from the decrypted url and is saved as a local file, note that downloadImage(String paramString) will always return the string ```"downloaded_image.jpg"```.
   
6) This file is used in the calculateSHA256
   ```java
   private static byte[] calculateSHA256(String paramString)```
7) This is in return used by the decryptFlagWithAESGCM to decrypt the flag
    ```java
    byte[] arrayOfByte1 = calculateSHA256(str3);
    String str4 = decryptFlagWithAESGCM(arrayOfByte1, "Tj/BJ+45Z45uRCFpuFOHirQI34ZC7bmtpCtJ3OE613fIxqrsZwIoLNSBXSjtPONFqZF3gC+4glh1Gyi2RBKZcuItH8s=", "qHttv1t5TWZLDM4e");
    ```
8) Basically if you cant download the image, you cant decrypt the flag. This means that we actually need to try and get the password to make progress.

How do we do that?
1) If we take a look at the decryptURL function, we can see thats is basically just doing bitwise xor, each character of our password will be xored with each element of the array. The result will be the decrypted url.
   ```java
   private static byte[] decryptURL(byte[] paramArrayOfbyte, String paramString) {
    byte[] arrayOfByte = new byte[paramArrayOfbyte.length];
    for (byte b = 0; b < paramArrayOfbyte.length; b++)
      arrayOfByte[b] = (byte)(paramArrayOfbyte[b] ^ paramString.charAt(b % paramString.length())); 
    return arrayOfByte;
    }
  
3) The challenge maker gave us a hint with ```str2.startsWith("https")```, since the url starts with https and every url is followed by "://" we can already decipher some characters from the password.
   The basic idea is here that we can hopefully guess the password based on the firts 8 characters.
4) We  know that ```password[0] ^ encryptedURL[0] = h``` and ```password[1] ^ encryptedURL[1] = t ``` and ```password[2] ^ encryptedURL[2] = t ``` and so on. So i made a python script that does this for us.
5) After running the script we get:
   ```Br00tBr0```
6) I assumed the password was "Br00t" repeated over and over again, so I just copy pasted "Br00t" until I got to the length of the ancrypted url array (53).
7) This worked and gave me the flag:
   ```flag{Fr00t-Br00t-is-the-only-cereal-for-Prez-Trump!} ``` 
   
   
   
