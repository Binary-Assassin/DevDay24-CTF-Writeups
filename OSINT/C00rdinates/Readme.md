# C00rdinates


# Author
Abubakr Wamiq


# Description
The secret lies in the coordinates
When you find the image check for Addeddate field in the image description


When you look at the image the first thing that comes to mind is the reverse image lookup using google, so we will do that.


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/db93ecb5-6f5b-4d9d-b44b-d32d6d4d5c4c)


Although we did not find the image source but we can see that it is suggesting similiar pictures from internet archieve aka the way back machine.
So lets give it a try, go to https://archive.org/ and in the top bar you can see an image icon. When you click on the icon you can see a drop down and in the drop down list the last item you can see is USGS Maps


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/b2c1d047-2ce1-4ad7-bce3-bfcb3cb1a73a)


Click on the the link and now you have access to archieves images of the United States Geological Survey maps, but ther are tons of images here.
To filter down our options we will analyze the image closely to find any keywords that may be of use.
First we notice is that this is a map of the California region, so we will check if that narrow downs our options. It works but there are still a lot of options. If you remember correctly the challenge descritption says that the secret lies in the coordinates. When you look at the map there are two consistent coordinates that are 32 and 115. Now lets try again with 'california 32 115'. And BINGO we found our image


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/3253014f-f5a3-4637-87f7-b2a5f20ff43d)


Now click on the image and look for the Addedate field and put it in the flag.


![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/121969132/c87f7050-6a26-4dd0-a309-61ce9f989ba2)


# Flag
 _**DD24{2006-10-09 22:52:19}**_
