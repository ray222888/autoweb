#!/usr/bin/python
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import ReadExcel

def from_contain(object,stringValue):
    print('validation contain text')
    sleep(5)
    browser = object
    stringContain = stringValue.upper()
    try:
     browser.find_elements_by_xpath("//*[contains(text(), '"+ stringValue+"')]")
     print('find text ' + stringContain)
     return 'true'
    except:
     print('find text error ' + stringContain)
     browser.get_screenshot_as_file(str(stringContain)+'.png')
     #ReadExcel.excelUpdate(filestr,"Fail,"+"value missing:"+' '.join(listinput)+","+str(caseid)+'.png',caseid)
     return 'find text error'

def from_value(object,list,filestr,caseid,optionbutton):
    print('validation form')
    browser = object    
    listinput = list    
   
    
    labels= browser.find_elements_by_tag_name("span")
    print (len(labels))
    print (listinput)  
    for arg in labels[0:]:
      try:
       if arg.text.lower() in listinput:          
            listinput.remove(arg.text.lower())
            print('remove')
      except:
        print('not remove')
    
    stronglabels= browser.find_elements_by_tag_name("strong")
    print (len(stronglabels))
    for arg in stronglabels[0:]:
        try:
            print(str(arg.text))
            replacestr = arg.text.replace("[","")
            replacestr = replacestr.replace("]","")        
            if replacestr in listinput:
                listinput.remove(replacestr)
                print('remove')
        except:
            print('not remove')

    textareas= browser.find_elements_by_tag_name("textarea")
    for arg in textareas[0:]:
        try:
         if arg.get_attribute('value').lower() in listinput:
            listinput.remove(arg.get_attribute('value').lower())
            print('remove')
        except:
            print('not remove')     
            
    if len(listinput)  == 0:
       ReadExcel.excelUpdate(filestr,"Pass",caseid)
       return 'true'
    else:
       print(listinput)
       #browser.get_screenshot_as_file(str(caseid)+'.png')
       #ReadExcel.excelUpdate(filestr,"Fail,"+"value missing:"+' '.join(listinput)+","+str(caseid)+'.png',caseid)
       return 'false,error,errorurl'

