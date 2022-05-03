short = 'xxxxxx'
appid = "xxxxxxxxxxxxxxxxxxxxxxx"
appkey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
publickey =  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

import time
import requests
import hashlib
import datetime
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5

from base64 import b64decode,b64encode
successUrl = 'https://us-central1-airtime-payment.cloudfunctions.net/payment/telebirr/paymentsuccess/1'

timestamp =  str(time.time()*1000)
timestamp = timestamp[:len(timestamp)-5]

nonce = "f514260e911746b0"+timestamp
outTradeNo = '20210907'+timestamp

signobj1 = {
    'appId':appid,
    'nonce':'f514260e911746b0164102880854',
    'notifyUrl':'url',
    'outTradeNo':'2021090716410288085',
    'receiveName': 'kuku player',
    'returnUrl': 'url',
    'shortCode': short,
    'subject': 'kolo',
    'timeoutExpress':'30',
    'timestamp': '164102880857',
    'totalAmount':'89',
}

signobj = {
    'appId':appid,
    'appKey':appkey,
    'nonce':'f514260e911746b0164102880854',
    'notifyUrl':'url',
    'outTradeNo':'2021090716410288085',
    'receiveName': 'kuku player',
    'returnUrl': 'url',
    'shortCode': short,
    'subject': 'kolo',
    'timeoutExpress':'30',
    'timestamp': '164102880857',
    'totalAmount':'89',
}

stringA = json.dumps(signobj1)
ussdjson = ''

for x in signobj:
    ussdjson += x+'='+str(signobj[x])+'&'
    
ussdjson = ussdjson[:len(ussdjson)-1]

stringB = hashlib.sha256(ussdjson.encode('UTF-8')).hexdigest()
sign = stringB

keyDER = b64decode(publickey)
keyPub = RSA.import_key(keyDER)
cipher = Cipher_PKCS1_v1_5.new(keyPub)

maxencrptblock = 117
offset = 0
inputlen = len(stringA)
data = ''.encode('UTF-8')
i = 0

while(inputlen - offset >0):
    if inputlen - offset > maxencrptblock:
        datam = cipher.encrypt(stringA[offset:offset+maxencrptblock].encode())
        data += datam
    else:
        datam = cipher.encrypt(stringA[offset:inputlen].encode())
        data += datam
    i+= 1
    offset = i*maxencrptblock

requestbody = {
    'appid':appid,
    'sign':sign,
    'ussd': b64encode(data).decode('UTF-8'),
}

x = requests.post('http://196.188.120.3:11443/service-openup/toTradeWebPay',json=requestbody)

print(x.text)
