---
stylesheet: https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/2.10.0/github-markdown.min.css
body_class: markdown-body
css: |-
  .page-break { page-break-after: always; }
  .markdown-body { font-size: 14px; }
  .markdown-body pre > code { white-space: pre-wrap; }
pdf_options:
  margins : 25mm
  printBackground: true
---
# Cryptograhphy Hands-On submission 5 | PKI

## Details : 

- SRN : PES2UG20CS237
- Name : P K Navin Shrinivas 
- Section : D

## TASK 1 : Becoming a CA

### Screenshots : 
![image](./1.png)
![image](./1_2.png)
![image](./1_3.png)

### Observation : 

- Above using openssl, we generate a certificate and a key. On seeing certificate details, we see its a SHA256RSA encrypted certificate. 
- This certificate also hold the modulus and public key parts of this system.
- To see details of private key, one needs the password with which this system was created with. This hold all the private and public parts of the key.


## TASK 2 : Creating priv/pub for requesting certificate.

### Screenshots : 

![image](./2.png)
![image](./2_2.png)

### Observation : 
- Above we create a csr, that is a certificate request with things that we want the server to enc their private material.
- We also have the priv/pub stuff stored in the .key file.

## TASK 3 : Creating cerificate for our server [From which we will be requesting using previous csr]

### Screenshots : 
![image](./3.png)

### Observation : 

- Above we are creating a certificate acting as www.Bank32.com using the csr that we generated in the previous step, along with serial.

## TASK 4 : Setting up server and setting up for certificate exchange 

### Screenshots and Observations : 
![image](./4_1.png)
- Above we copy over the certicated for Bank32.com and CA certificates over to the docker file in the apace installtion.
![image](./4_2.png)
![image](./4_2_2.png)
- Above we simply build the docker image and start it.
![image](./4_3.png)
- Above we are modifying the hosts file for bank32.com such that when queried from dns, we will get a local ip address and resolved address.
![image](./4_4.png)
- Above we see that firefox gives a warning that the CA is not a trusted one and may be self signed.
![image](./4_5.png)
- Above we see no such warning as the modelCA.crt certificate was added to the trusted list of certs in firefox.

### Question : 
![image](./4_6.png)

- Above firefox shows an error code of bad cert domain, why?
- This is bacuse if we see the command that we did to create bank32.com's certificate we used 3 domains, one main domain and 2 alias domains. None of them were the ip address of the server. Firefox verifies if the cerficated are fit by comparing hosts, which in this case is not.
- The three domain this certificate is fit for is : "www.bank32.com","www.bank32A.com","www.bank32B.com"

## TASK 5 : MITM attack 

### Screenshots and Observations : 

![image](./5_1.png)
- Above we are acting as a CA and creating certificates for www.example.com using csr and crt
![image](./5_2.png)
- Above we rebuild the docker image with new ssl conf and certificates, one that can serve www.example.com

![image](./5_3.png)

- Above we are creating fake entries in the hosts dns record file. Usually for MITM attack, this change has to be done programmatically and this rightfully need elevated permissions.
![image](./5_4.png)
- Above we visit www.example.com in the host machine, as we have added ourselves as trusted CA in the firefox list, we see no warnings come up. The unaware hosts never knows that is isn't the original site. Hence our MITM attack has been executed successfully.

