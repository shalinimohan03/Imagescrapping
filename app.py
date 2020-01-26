# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:44:31 2020

@author: Viswanath
"""

from flask_cors import CORS,cross_origin
from flask import Flask,render_template,request
import os
from scrapper_image.ScrapperImage import ScrapperImage
from businesslayer.BusinesslayerUtility import BusinessLayer


### import request
app=Flask(__name__)

# redirecting to the home page
@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def displayimages():
    listimages=os.listdir("C:/Users/Viswanath/shalini_DSPractice/Scrapping_images/static")
    print(listimages)
    
    try:
        if(len(listimages)>0):
            return render_template("showImage.html",user_images=listimages)### This user_images should get and match from yhe show.html code
        else:
            return "Images are not present"
        
    except Exception as e:
        print("no images found",e)
        return "Please type right keyword"
    
@app.route('/searchImages',methods=['Get','POST']) ## searchImages u can find in index.html
def searchImage(): # This basically uses the index.html to get the keyword entered there by clicking submit at index page , 
    #request straightly coming here so u can receive here by using .form method 
    if request.method=='POST':
        search_term =request.form['keyword']
    else:
        print("please enter the keyword")
        
    imagescrapperutil = BusinessLayer
    imagescrapper = ScrapperImage()
    listimages=os.listdir("C:/Users/Viswanath/shalini_DSPractice/Scrapping_images/static")
    imagescrapper.delete_download_images(listimages)### Deletes the existing images before trying to scrap the new image
        
    image_name=search_term.split()
    image_name="+".join(image_name)
    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            
            }
    lst_images=imagescrapperutil.downloadImages(search_term,header)
    ## DownloadImages - called from  business layer
    
    return displayimages() # redirect the control to the show images method to display the images to the screen
    
        
if __name__=="__main__":
    app.run(host='127.0.0.1',port=8080)
     