from selenium import webdriver as web
from selenium.webdriver.chrome.options import Options
import os
import time as t
import pyautogui as auto
from PIL import Image
print(os.getcwd())
options= Options()
options.add_argument('--load-extension={}'.format(os.getcwd()+r"\full-page-capture-chrome-extension-master"))
driver = web.Chrome('chromedriver.exe',options=options)
conn=driver.get("https://www.doc-solus.fr/bin/users/connexion.html")

driver.find_element_by_name("login").send_keys("ilyasswadjinny@gmail.com")
driver.find_element_by_name("passwd").send_keys("qfKh6w3pMrsWKNi")
driver.find_element_by_name("save").click()


for ans in range(18):
    for num in [1,2]:
        ansS=str(ans) if ans>=10 else '0'+str(ans)
        annale="MP_PHYSIQUE_CENTRALE_"+str(num)+"_20"+ansS
        url="https://www.doc-solus.fr/prepa/sci/adc/bin/view.corrige.html?q="+annale

        driver.get(url)

        links_el=driver.find_element_by_tag_name("section").find_elements_by_tag_name("a")

        links=[i.get_attribute("href") for i in links_el]

        for e in range(len(links)):
            driver.get(links[e])
            if e==len(links)-1: driver.refresh()
            driver.execute_script("""
        $("a img,table:first,div:last").remove()
        $("div:first").removeClass("one_column")
        $("body:first").css("background","white")
            $("h1").remove()
            """)
            auto.hotkey('alt','shift','p')
            while(len(driver.window_handles)==1):
                t.sleep(2)
            auto.hotkey('ctrl','s')
            while(len(driver.window_handles)==2):
                t.sleep(2)
                auto.hotkey('enter')
                t.sleep(2)
                auto.hotkey('ctrl','w')
            t.sleep(2)
        docs=r'C:/Users/'+os.getlogin()+r'/Downloads'
        files=os.listdir(docs)
        imgs=[]
        for f in files:
            if 'doc-solus' in f:
                imgs.append(f)

        imgss=[Image.open(docs+i).convert('RGB') for i in imgs ]

        imgss[0].save(annale+'.pdf',save_all=True, append_images=imgss[1:])

        for i in imgs:
            os.remove(docs+i)











