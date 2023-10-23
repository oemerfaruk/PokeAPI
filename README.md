# Case Study - PokeAPI
<img src='https://pokeapi.co/static/pokeapi_256.3fa72200.png' width=200>

A restful api for Pokemon Data

## Introduction

### Case Study
https://pokeapi.co URL'i üzerindeki Rest API kullanılarak, ismini kullanıcının gireceği bir Pokemonun yeteneklerini ve yine API üzerinden ingilizce olarak alınacak yetenek özelliklerini html halinde tablo olarak oluşturulması bekleniyor. Dosya formatı PDF'e dönüştürülerek sorgulamayı yapan kullanıcıya mail olarak atılması gerekmektedir. Pokemon ismi ve gönderilecek mail adresi input ile alınacak ve fonksiyon yapısı kullanılarak modüler olarak işlem yapması beklenmektedir. (Python kullanılacaktır)

<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmk1Y3Zuem9hZ3d6dWcxbDJycjVweHpzejJ2c3pwdjNuZTN4ZG5pZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DB2Xn2W6Ea5k10r0ro/giphy.gif' width=550>

----
### Installation
#### Weasyprint
**htmltopdf**.*py* programının kullanımı için ***weasyprint*** dahil edilmeli bundan dolayı;

``` Bash
pip3 install weasyprint
```


#### Pokebase
**mainPokeBase**.*py* programının kullanımı için ***pokebase*** dahil edilmeli bundan dolayı;

``` Bash
pip3 install pokebase
```

---

### Modules
#### sendmail.py

``` Python
from userInfo import * # sender_email ve password bilgilerini içerir
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
```
#### mainRest.py
``` Python
from createhtml import *
from htmltopdf import *
from sendmail import *

import requests
```
#### mainPokeBase.py
``` Python
from pokebase import *
from createhtml import *
from htmltopdf import *
from sendmail import *
```
#### createhtml.py
``` Python
from weasyprint import HTML
```
