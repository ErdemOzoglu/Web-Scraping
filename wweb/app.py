#Emirhan Ekşi 180202079
#Erdem Özoğlu 180202094
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from flask import Flask,render_template,request,redirect,url_for
import cgi

app = Flask(__name__)
@app.route("/")
def index():
      return render_template("index.html")

@app.route("/toplam", methods = ["GET","POST"])
def toplam():
    if request.method =="POST":
          url1 = request.form.get("url1")  
          url2 = request.form.get("url2")
          r2 = requests.get(url2)
          source2 = BeautifulSoup(r2.content,"html.parser")
          metin2 = source2.find("body").text
          for char in '1234567890!^%&(?é<|>#$[_])}{/*+=-,.\n':
              metin2 = metin2.replace(char, ' ')
          metin2 = metin2.lower()
          array2 = metin2.split()
          count2 = {}
          for word2 in array2:
              count2[word2] = count2.get(word2, 0)+1
          sort2=sorted(count2.items(), key=lambda x: x[1], reverse=True)
          arr2 = pd.Series(sort2)
          sorted_values2 = sorted(count2.values()) # Sort the values
          sorted_dict2 = {}
          for i in sorted_values2:
              for k in count2.keys():
                  if count2[k] == i:
                      sorted_dict2[k] = count2[k]
                      break            
          df2 = pd.DataFrame(sorted_dict2.items(),columns = ['kelime','sayac'])
          kw2 = df2.loc[::-1].reset_index(drop = True)
          allkw2=kw2
          kw2 = kw2.head(5)
          r = requests.get(url1)
          source = BeautifulSoup(r.content,"html.parser")
          metin = source.find("body").text
          for char in '1234567890!^%&(?é<|>#$[_])}{/*+=-,.\n':
              metin = metin.replace(char, ' ')
          metin = metin.lower()
          array = metin.split()
          count = {}
          for word in array:
              count[word] = count.get(word, 0)+1
          sort=sorted(count.items(), key=lambda x: x[1], reverse=True)
          arr = pd.Series(sort)
          sorted_values = sorted(count.values()) # Sort the values
          sorted_dict = {} 
          for i in sorted_values:
              for k in count.keys():
                  if count[k] == i:
                      sorted_dict[k] = count[k]
                      break  
          df = pd.DataFrame(sorted_dict.items(),columns = ['kelime','sayac'])
          kw1 = df.loc[::-1].reset_index(drop = True)
          allkw1=kw1
          kw1 = kw1.head(5)
          kw1.plot(x ='kelime', y='sayac', kind = 'bar')
          #plt.show()
          list = kw1["kelime"]
          list[0]
          r2 = requests.get(url2)
          source2 = BeautifulSoup(r2.content,"html.parser")
          metin2 = source2.find("body").text
          for char in '1234567890!^%&(?é<|>#$[_])}{/*+=-,.\n':
              metin2 = metin2.replace(char, ' ')
          metin2 = metin2.lower()
          array2 = metin2.split()
          sayac = 0
          len(array2)
          for x in array2:
              if (list[0]==x) | (list[1]==x) | (list[2]==x) | (list[3]==x) | (list[4]==x) :
                  sayac = sayac+1 
          print(sayac)
          oran= (sayac/len(array2))*100
          sayac = 0
          print("Benzerlik oranı : %",oran)
            
              
          return render_template("sonuc.html",total =oran  ,kv1=kw1 , kv2=kw2 , allkv2=count2 , allkv1=count) 
    else:
          return render_template("sonuc.html")
      
if __name__ == "__main__":
    app.run(debug = True)