#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
url="http://desktop-pakdbu0:8080/CalculatorWS/CalculatorWS?wsdl"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="UTF-8"?>
         <S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/" 
            xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
            <SOAP-ENV:Header/>
                <S:Body xmlns:ns2="http://calculator.me.org/">
                    <ns2:add>
                        <i>1</i>
                        <j>1</j>
                    </ns2:add>
                </S:Body>
         </S:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print(response.content)


# In[ ]:




