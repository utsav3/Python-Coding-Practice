# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 13:18:42 2018

@author: utsav
"""

from __future__ import print_function
import requests, re, sys

url_link = "http://cs.siu.edu/faculty-staff/continuing_faculty.php"   
keywords = {"Education:": "Education", "test1": "test1"}

def urlScraping(url_link):
    main_page= requests.get(url_link)
    search_term = "Email:"
    
    if search_term in keywords:
        print("JERE")
        return get_data_by_keyword(main_page, search_term)
    else:
        div_term = "Email:"
        end_tag = "</div>"
        
        #print(main_page.text)
        links = re.findall(r'<div class="people-wrapper">(.+?)</div>' , main_page.text, re.S)
        homepage_links =  re.findall(r'<div class="summary">(.+?)</div>' , main_page.text, re.S)
    
        #(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\.[a-zA-Z0-9-.]+$)
        for link,homepage_link in zip(links,homepage_links):
            
            #print(link)
            name = re.search(r'<h3>(.+?)</h3>',link,re.S)
            email_str = re.search(r'Email:(.+?)</',link,re.S)
            #email = re.search(r'.*edu',email_str.group(0),re.S)
            #email = re.search(r'',email.group(0))
            office = re.search(r'Office:(.+?)<',link,re.S) 
            position = re.search(r'<h4 class="department">(.+?)</h4>',link,re.S)
            phone = re.search(r'Phone:(.+?)<',link,re.S)
            print("*************************************************************")
            print("Name: "+ name.group(1))
            print("Position:" + position.group(1))
            print("Phone:"+ phone.group(1))
            print("Office:" +office.group(1))
            
            email = re.search(r':.*?edu',email_str.group(1))
            if email is not None:
                print("Email"+ email.group(0))
            else:
                email1 = re.search(r'>(.+)<',email_str.group(0))
                print("Email " + email1.group(0)[1:-1])
            homepage = re.search(r'<a href="(.+?)\"',homepage_link,re.S)
            if homepage is not None:    
                print("Homepage: "+homepage.group(1))
            else:
                print("Homepage Not Applicable")
            #print(faculty.text)
            #return get_faculty_name(faculty)
           # print("FOUND " , link.group(1) )
           
            
            
            

    
if __name__ == "__main__":
   urlScraping(url_link)