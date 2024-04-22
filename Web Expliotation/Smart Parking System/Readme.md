# Smart Parking System

## Description
Smart Parking System is under maintenance!

## Solution

Vist "/robots.txt".

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/84d488d0-4d68-41db-b195-8a4025568daa)

Vist "/contactIT".

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/55d05157-08e2-4b38-9d83-c723e375f4ed)

Intercept the request in BurpSuite, send it to Repeater, and change "GET" to "POST".

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/639a472f-9d2d-4a67-ac83-1a7cf1ecbd05)

Add "Content-Type: application/json" to the HTTP header.

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/54d5106f-00bc-4f70-b2f1-fffc0e5bf648)

Send add any random JSON data.

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/515cb56d-7785-42d1-b56e-2843074bff28)

Forward the same request from the proxy.

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/d0ede3af-2aa7-4824-9148-a5e19a08cefe)

As you can see, debug mode is on and it is leaking a bit of source code from the server. We will adjust the request accordingly.

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/54a61849-fec0-4541-851c-43cdb7bb0b67)

WHOA EMAIL SENT
After checking our email, we get the flag.

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/d4b6115d-f7f4-4547-988f-3ec5b9af6018)

**Flag:** 
> DD24{N3v3r_L3ft_D3bug_M0de_0n}



