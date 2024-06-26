# Jihaadi

## Description
What are you looking at?

### Author
Osama Irfan

## Solution
This challenge includes a .jpg image file. The flag is divided into two parts. One part of the flag can be extracted using the steghide tool in Kali Linux with the following command:       

Commnad: `steghide extract -sf jihaadi.jpg`

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/88867050-7cee-4042-a6f6-9b26f2545463)

You can simply press enter when prompted for a password as it has no password. This will create a secret.txt file where the first part of the flag can be found.

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/098c6aad-ae51-4064-a1a8-5f7315e00814)

If we view the contents of this secret.txt. First part of the flag will be found.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/a982f878-5b00-48b4-83ba-a48cb89c53ca)

To find the second part of the flag we can just check for the meta data of the image using exiftool or any other online tool.
![tempsnip](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/17d2bf4b-62cd-43b6-820e-169fd69cb8ba)

## Flag for this challenge is: 
> **DD24{Th1$_1$_C@LL3D_CYB3R_J1H@@D}**


To learn more about steganography, you can visit the following link:
https://www.freecodecamp.org/news/what-is-steganography-hide-data-inside-data/
