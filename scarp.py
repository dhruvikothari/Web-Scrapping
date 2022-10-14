# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:44:31 2022

@author: Mansiba Gohil
"""

import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.adidas.co.in/outlet?sale_percentage_en_in=30%25%7C50%25%7C40%25&utm_campaign=alwayson_CPV&utm_medium=affiliate&utm_source=Dangleads&utm_term=CPV_1851")

soup = BeautifulSoup(req.content, "html.parser")


print(soup.prettify())