# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:14:09 2020

@author: Viswanath
"""

from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
# urllib.request is a Python module for fetching URLs (Uniform Resource Locators).
import urllib.parse
from urllib.request import urlretrieve

class ScrapperImage:
    
    def createImageurl(searchterm):
        searchterm = searchterm.split()
        searchterm="+".join(searchterm)
        web_url = "https://www.google.com/search?q="+ searchterm + "&source=lnms&tbm=isch"
        return web_url
    
    def scrap_html_data(url,header):
        request =urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(request)
        #urlopen function. This is capable of fetching URLs using a variety of different protocols. 
        #It also offers a slightly more complex interface for handling common situations - 
        #like basic authentication, cookies, proxies and so on
        responsedata=response.read()
        #Calling urlopen with this Request object returns a response object for the URL requested. This response is a file-like object, 
        #which means you can for example call .read() on the response:
        html=bs(responsedata,"html.parser")
        return html # passing this url to nect function to get the images
        
    def getimageUrlList(rawhtml):
        imageUrlList=[]
        for a in rawhtml.find_all("div",{"class":"rg_meta"}):
            link,imageExt =json.loads(a.text)["ou"],json.loads(a.text)['ity']
            imageUrlList.append((link,imageExt))
        print("There are total number of",len(imageUrlList),"images")
        return imageUrlList # u got link and extension of each image to send it to next download function
    
    def downloadImagesFromURLExt(imageUrlList,image_name,header):
        masterListOfImages=[]
        count=0
        imagesFiles=[]
        imagesTypes=[]
        
        image_count=0
        for i,(img,Type) in enumerate(imageUrlList):
            try:
                if(count>10):
                    break
                else:
                    count=count+1
                req=urllib.request.Request(img,headers=header)
                try:
                    urllib.request.urlretrieve(img,"C:/Users/Viswanath/shalini_DSPractice/Scrapping_images/static"+image_name+str(image_count)+".jpg")
                    image_count=image_count+1
                except Exception as e :
                    print("Storing and naming image failed:",e)
                    image_count=image_count+1
                respdata=urllib.request.urlopen(req)
                raw_img =respdata.read()
                imagesFiles.append(raw_img)
                imagesTypes.append(Type)
                
            except Exception as e:
                print("could not load"+img)
                print(e)
                count=count+1
        masterListOfImages.append(imagesFiles)
        masterListOfImages.append(imagesTypes)
        return masterListOfImages
  
    def delete_downloaded_images(self,list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("C:/Users/Viswanath/shalini_DSPractice/Scrapping_images/static"+self.image)
            except Exception as e:
                print("error in deleting the images",e)
                
        return 0        
                
    
        