# Keul

## Description
Doc... Doc... Who is it?

### Author
Osama Irfan

## Solution
This challenge contains a file keul which is unaccessible due to a broken file extension.

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/a61a09a6-e63c-488a-998c-37e4eb657450)

Upon getting a hint from the challenge description "Doc... Doc..." we found that it is a **.docx** (Ms Word) file. So we applied the extension.    

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/9ef3aef5-2893-431b-9ad0-6346da95a93d)

The word file contains a base64 string.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/acef9887-a8f3-4505-8740-d969afae9415)

Upon decrypting it using CyberChef we can find a github link which has some image file in it containing a flag. But Sadly thats a fake flag.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/120d6e70-59e3-49ab-ac5e-02f735f95d8a)

Have you ever seen this meme? This is the original image of the meme.
![6lgcf5](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/f35c2839-a862-4633-bd06-242b9b663065)

What can we do now? We see that the meme image is incomplete or is resized. To get the original image you can follow the following steps:

Use CyberChef to upload your image and convert it to Hex by selecting the "To Hex" recipe. The output gives you the hexadecimal values for the image.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/fd083454-5513-49f9-8530-ad34f26f87bc)

Next, copy the output and click the trash icons to clear the Input and Recipe panels and paste the copied values in the input panel. 
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/5cc55168-df14-4834-ad2d-321afa714256)

In the Operations panel, enter "From Hex" and click or drag the it over to the Recipes panel.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/c0016952-c5a0-419f-aa75-66a2c4c02dca)

Now hold ctrl+F in the output field and search for ff c0. Note the following values starting at ff c0:
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/418d07fa-2a54-4d86-818a-324377260e79)

I've highlighted the relevant bytes and what they mean in the image below:
![hex](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/c432dcb6-63f9-48f4-87ab-49c6aba0f528)

Now again in the Operations panel, enter "Render Image" and click or drag it over to the Recipes panel so you can see the result rendered result of the image also.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/9f8ebddc-0c31-4096-9344-f8975bb80816)

Now modify the height values of this image to something else as below, By doing so the image height will be increased and you will find the flag:
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/1e19c68c-f7dd-40b3-8a45-d856972599f1)

Save the modified image get the flag.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/c7dc2bb6-07d4-4e9b-951c-9daed3cae3f0)

## Flag for this challenge:
> **DD24{Y3$_Y0U_D1D_1T}**

