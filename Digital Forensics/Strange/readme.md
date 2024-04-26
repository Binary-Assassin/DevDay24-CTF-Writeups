# Strange

## Description:       
I travel through wires, invisible to sight,    
Carrying secrets, hidden from light.    
Messages I carry, data I bear,     
Discover the keys, open the gate.   

### Author
Osama Irfan

## Solution
This challenge includes a .pcapng file which can be analysed by Wireshark tool. 
Find more about Wireshark here: https://www.upguard.com/blog/what-is-wireshark

Upon opening this file in Wireshark tool. We can see all the captured traffic by the author.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/e40f7ed2-939d-4aaa-b138-78623e444fcf)

We can check for the specific traffic by filtering it. For e.g. Here I filtered for `http` 
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/b1ea8f86-5023-4386-8baf-39240f042345)

Now right click on the on any packet. Go to Follow->Tcp Stream 
![Screenshot (2)](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/87258f1f-efd2-4a6f-846b-4935ee4b2508)
In TCP stream, you can view packet details.

Here you can see a specific email conversation is being done. You can analyse other streams also by simply increasing the number of streams.
![tempsnip](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/a72ce2d6-282f-4694-90b3-49ac0953a739)

In the streams we can observer that some pdf files are being shared.
![tempsnip](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/44bfeab4-79c5-4f25-a7f1-48a312970f7f)

We can download these pdf files from the File->Export Objects->http 
![Screenshot (3)](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/0d917bd5-9d6e-497d-a7c2-c6046c97aa4b)

Click on the pdf and save it. There are total 8 pdf files.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/5d9e6fea-c885-4af2-87ac-d88637254e13)

Upon extracting the files it asks for the password.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/8fa24d6a-1437-44ba-84c2-3101bce585ee)

Now we have to find the password in the streams. Try to find any unusual strings from the stream.   
Here in the part_1.pdf stream we found some usual base64 encrypted string so we can test it using cyberchef.
![tempsnip](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/796d6a32-2162-47c2-820a-77ea3fd7961c)

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/6aabba17-7cf0-4ea3-9fae-ab8d0c1658b2)

We can test this string for the first part_1.zip file.   
The password was correct and we got the pdf.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/5030728a-41af-4e86-b62c-145783803bf2)

But we found nothing special from here.
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/3d30d6ab-faaf-4e6e-a99f-6d7c35cb5846)

So we have to keep trying for all the other 7 parts of the pdf.
1. Get the encryped string:
   ![tempsnip](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/d952819a-4ab3-4569-943e-c0b129c0a0c3)

3. Decrypt it using cyberchef:
   ![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/4afbc6d9-34ac-4559-a8d5-92e1a9ce3551)

4. Extract the pdf:
   ![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/501a06a7-5b55-4fba-881b-fe729f2d8b2b)

5. Check for any usual information:
   Here in part 2 we found a part of the flag. But its still incomplete so we have to try other parts too.
   ![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/19e41282-791f-49de-9af5-1e55215d9b6e)

6. Repeat the same steps for all.

By doing so we will find all the parts. The flag was divided into 3 parts. Part 1 was placed in **part_2.pdf**, Part 2 was placed in **part_4.pdf** and part 3 was placed in part_8.pdf.    

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/767dac82-7c7f-42d6-9ac8-12cd251dc406)

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/128910142/5d0d8986-1074-4a2d-a573-3f4e84e49205)

## Flag for this challenge:
> **DD24{Y0U_H@V3_TH3_P0T3NT1@L}**
