from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

####################### Database

##import psycopg2
##
##conn = psycopg2.connect(database="testdb", user="postgres", password="12345", host="127.0.0.1", port="5432")
##
##print ("Opened database successfully")
##
##cur = conn.cursor()

##
##     #### CREATE TABLE  ####
##    
##cur.execute('''CREATE TABLE CAR_DATA
##       (ID SERIAL PRIMARY KEY  ,
##       TITLE           TEXT    ,
##       HOUR            TEXT    ,
##       UBICATION       TEXT    ,
##       PRICE           TEXT    ,
##       ANNO            INTEGER     ,
##       USAGE           TEXT    ,
##       KM              BIGINT     ,
##       GAS             TEXT    ,
##       TRANS           TEXT    ,
##       MODEL           TEXT    ,
##       COLOR           TEXT    ,
##       DESCRIPTION     TEXT    ,
##       SELLER          TEXT    ,
##       PHONE           TEXT    ,
##       IMAGE           TEXT    
##       );''')
##
##print ("Table created successfully")
##
##conn.commit()

#######################################


option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome()
browser.get("https://www.olx.co.cr/autos-cat-378")



conta2 = 1

while(conta2<400):
   elements = browser.find_elements_by_xpath("//*[@class='item featuredad  highlighted']")
   elements2 = browser.find_elements_by_xpath("//*[@class='item  highlighted']")
   elements3 = browser.find_elements_by_xpath("//*[@class='item ']")
   e = [x.text for x in elements]
   e2 = [x.text for x in elements2]
   e3 = [x.text for x in elements3]
   tam = len(e)+len(e2)+len(e3)
   conta = 1
   while(conta<tam):

       browser.find_element_by_xpath("//*[@id='items-list-view']/ul/li[" + str(conta) +"]/a").click()


       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/header/div[1]/h1")) == 0):
           title = "No data"
       else:
           title = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/header/div[1]/h1")
           title = title.text


       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/header/div[2]/p[1]/time")) == 0):
           hour = "No data"
       else:
           hour = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/header/div[2]/p[1]/time")
           hour = hour.text


       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/header/div[2]/p[1]/span")) == 0):
           ubication = "No data"
       else:
           ubication = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/header/div[2]/p[1]/span")
           ubication = ubication.text

       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/header/div[2]/p[2]/strong")) == 0):
           price = "No data"
       else:
           price = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/header/div[2]/p[2]/strong")
           price = price.text

       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[1]/span")) == 0):
           anno = 0
           usage = "No data"
       else:
           annoCondicion = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[1]/span")
           anno = annoCondicion.text[:4]
           usage = annoCondicion.text[4:]

       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[3]/span")) == 0):
           km = 0
       else:
           km = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[3]/span")
           km = km.text

       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[5]/span")) == 0):
           gas = "No data"
       else:
           gas = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[5]/span")
           gas = gas.text
       
       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[2]/span")) == 0):
           trans = "No data"
       else:
           trans = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[2]/span")
           trans = trans.text
       
       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[4]/span")) == 0):
           model = "No data"
       else:
           model = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[4]/span")
           model = model.text

       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[6]/span")) == 0):
           color = "No data"
       else:
           color = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/ul/li[6]/span")
           color = color.text

       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/div/section[1]/p")) == 0):
           description = "No data"
       else:
           description = browser.find_element_by_xpath("//*[@id='item_index_view']/article/div/section[1]/p")
           description = description.text

       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/aside/div[1]/div[2]/p[1]")) == 0):
           seller = "No data"
       else:
           seller = browser.find_element_by_xpath("//*[@id='item_index_view']/article/aside/div[1]/div[2]/p[1]")
           seller = seller.text
       
       if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/article/aside/div[1]/div[3]/a")) == 0):
           phone = "No data"
       else:
           browser.find_element_by_xpath("//*[@id='item_index_view']/article/aside/div[1]/div[3]/a").click()
           phone = browser.find_element_by_xpath("//*[@id='item_index_view']/article/aside/div[1]/div[3]/strong")
           phone = phone.text

       if (len(browser.find_elements_by_xpath('//*[@id="item_index_view"]/article/div/section[1]/section/figure/a/img')) == 0):
           imageSrc = "No data"  
       else:                     
           image = browser.find_element_by_xpath('//*[@id="item_index_view"]/article/div/section[1]/section/figure/a/img')
           ##imageSrc = image.text
           imageSrc = image.get_attribute("src")

       print("------Informacion------\n")
       print("Título: " + title)
       print("Hora Publicacion: " + hour)
       print("Ubicacion: " + ubication)
       print("Price: " + price)
       print("Anno: " + str(anno))
       print("Uso: " + usage)
       print("Kilometraje: " + str(km))
       print("Combustible: " + gas)
       print("Transmisión: "+ trans)
       print("Modelo: " + model)
       print("Color: " + color)
       print("Descripcion: " + description)
       print("Vendedor: " + seller)
       print("Teléfono: " + phone)
       print("Imagen: " + str(imageSrc))
       print("\n")
   
      
##       try:
##          cur.execute("INSERT INTO CAR_DATA (TITLE,HOUR,UBICATION,PRICE,ANNO,USAGE,KM,GAS,TRANS,MODEL,COLOR,DESCRIPTION,SELLER,PHONE,IMAGE) VALUES ('" + title + "','" + hour + "','" + ubication + "','" +  price + "','" + anno + "','" + usage+ "','" + km + "','" + gas + "','" + trans + "','" + model + "','" + color + "','" + description + "','" + seller + "','" + phone + "','" + imageSrc + "')");
##          conn.commit()
##       except:
##          pass
       
       conta+=1  
       browser.back()

   if (len(browser.find_elements_by_xpath("//*[@id='item_index_view']/nav/p[1]/a")) > 0):
      browser.find_element_by_xpath("//*[@id='item_index_view']/nav/p[1]/a").click()

   
   element = browser.find_element_by_xpath("//*[@id='listing-breadcrumb']/div[2]/a[2]")
   browser.execute_script("arguments[0].click();", element)
   conta2+=1
