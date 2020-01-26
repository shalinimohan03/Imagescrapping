# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:11:22 2020

@author: Viswanath
"""
## FIRST scrapper_image is folder name ,second one is python file ,third is class name

from scrapper_image.ScrapperImage import ScrapperImage

class BusinessLayer:
    keyword=""
    header=""
    
    
    def downloadImages(keyword,header):
        imgscrapper=ScrapperImage
        url= imgscrapper.createImageUrl(Keyword)## This will ive you weburl to webscrap to next function
        rawhtml=imgscrapper.scrap_html_data(url,header)
        
        imageURLlist=imgscrapper.getimageUrlList(rawhtml)
        masterListOfImages=imgscrapper.downloadImagesFromURLExt(imageURLlist,keyword,header)
        
        return masterListOfImages