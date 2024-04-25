# RabbitHole

## Description
head over to the acm cys instagram page and see if you can find out something interesting

### Author 
Abubakr Wamiq


When you head over to the instagram page of acm cys you can see a strange comment made by AbubakrWamiq under the devday CTF post, Pufd3b1W2k6wkYGWmxuzFhBuKMyq948HWMtSHLVpZQGRyqrUfVKPaCPN.
It looks like some base64 string, so we put it in cyberchef to find out.


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/ed4366a2-33e0-4bd3-9d98-222e7b22d0cb)


Turns out it is a base58 string and it decodes to a link to a github repository, so lets see what the repository holds.


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/ceff7987-48a0-47db-9aeb-1c7fa90e52bb)


Turns out it has three folders and a file with two subfolders and all of them have random data and text that seems irrelevant.
When going through the May be this one? file there are two strings that can be found at the end of lines 3 and 5


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/79709b0e-d612-42af-a8c9-ba453d6f63bf)


Lets put them both in cyberchef


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/40e271bc-9305-4d7d-a38c-cc113f639006)
![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/5ebb026d-a7b9-4637-a791-125b6b4d0e92)


One looks like a fake flag but the second one is a URL which leads to the famous rick and roll meme template
The same two strings that we decoded can be found in the Or this one ? file


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/629db2db-96be-4977-982b-d2b9f3ac5348)


This means that the flag lies in these strings. One is a fake flag and the other one is a link. 
When you look at the comments under the rick roll meme video and sort them by the newest first you can see a string posted by Work Aura and if you have done the first challenge this should ring a bell


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/0b7703d6-3eca-4580-a7e4-d876777c6084)


lets put this string in cyberchef and see if it works and BINGO we found the flag


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/7f24c291-8601-4322-a7a6-198716c83342)


# Flag
_**DD24{th1s_is_th3_r33l_fl4g}**_
