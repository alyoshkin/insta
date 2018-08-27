from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
import time   
import datetime
import pandas as pd
import time
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import pyperclip
import collections
import datetime
time_wait = 1.5


import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
display(HTML("<style>.container { width:100% !important; }</style>"))
import random
def smaller(x, than=0):
    if not x or min(x) < than:
        return True
    return False
def larger(x, than=0):
    if not x or min(x) > than:
        return True
    return False

def rolldown(dr,circles, tm):
    for i in range(1,circles):
        dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
        dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
        dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
        time.sleep(tm)

def pop_col(im,x1,y1):
    cnt=0
    rnd=10
    samplesize=500
    import math
    for x in range(0, min(samplesize, x1-1) ):
        for y in range(0, min(samplesize, y1-1) ): 
            [r, g, b] = im[random.randint(1,x1-1), random.randint(1,y1-1)]
            #if smaller([r, g, b], than=255) and larger([r, g, b], than=0) and min(r,g,b)<110 and max(r,g,b)>120:
            if smaller([r, g, b], than=255) and larger([r, g, b], than=0) and min(r,g,b)<100 and max(r,g,b)>170:
                #print(str(r)+' ')
                r=rnd*math.ceil(float(r)/rnd)
                g=rnd*math.ceil(float(g)/rnd)
                b=rnd*math.ceil(float(b)/rnd)
                if cnt==0:
                    comb = [str(r)+'_'+str(g)+'_'+str(b)]
                else:
                    comb = comb + [str(r) + '_' + str(g) + '_' + str(b)]
                cnt=cnt+1
    try:
        counter=collections.Counter(comb)
        res=counter.most_common(1)
    except:
        res=[('0_0_0', 0)]
    return res

def get_ln(sr,pr):
    fr=9
    t=21
    for i in range(0, len(pr)-1):
        if i==0:
            ln = [scr[(pr[i]+fr):(pr[i]+t)]]
        else:
            ln = ln + [scr[(pr[i]+fr):(pr[i]+t)]]
    return ln
#a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
#counter=collections.Counter(a)
#print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
#print(counter.values())
# [4, 4, 2, 1, 2]
#print(counter.keys())
# [1, 2, 3, 4, 5]
#print(counter.most_common(1))

#url = "https://www.instagram.com/" # accounts/login/
#driver.get(url)
#driver.current_url
#main_window = driver.current_window_handle
#time.sleep(time_wait)

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches
        
#top = topic0[0]
#main_link = 'https://www.instagram.com/explore/tags/' + top + '/'
#driver.switch_to.window(main_window)
#driver.get(main_link)

def get_inst_by_tag(dr, top, cyc):
	main_lnk = 'https://www.instagram.com/explore/tags/' + top + '/'
	dr.switch_to.window(main_window)
	dr.get(main_lnk)
	for i in range(1,cyc):
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		time.sleep(time_wait/2)
		scr=dr.page_source
		places=list(find_all(scr, '/p/'))
		for j in range(0,len(places)-1):
			lnks = lnks + [scr[(places[j]+3):(places[j]+14)]]
			if i % 50 == 0:
				print(i)
	return list(sorted(set(lnks)))


def find_emoji(hashtxt, emj):
    t=''
    emojilst = list(emj.items())
    for kk in hashtxt:
        if len(kk)>3:
            if kk[-1:] == 's':
                str2 = kk[:-1]
            else:
                str2 = kk
            for ll in range(0, len(emojilst) - 1):
                #print(kk)
                if emojilst[ll][0].find(kk)>=0 or emojilst[ll][0].find(str2)>=0:
                    t = t + emojilst[ll][1] + ' '
    return t



def get_emoji(col):
	if col<=0.1 or col>0.9:
		e=emoji['red heart']
	if col>0.1 and col<=0.3:
		e=emoji['yellow heart']
	if col>0.3 and col<=0.45:
		e=emoji['green heart']
	if col>0.44 and col<0.8:
		e=emoji['blue heart']
	if col>=0.8 and col<=0.8:
		e=emoji['purple heart']
	return e 
	
topic0 = ['summer','purple','sunset','morning','night','nature','mountains','saintpetersburg','sea','weekend','food','color']

		
poptags=['sunset','sky','clouds','sea','sunrise','evening','flowers','ocean','dog','colors','hair','horizon','city','lake','river','canon']

def get_rgb(scr):
	pic1=list(find_all(scr, 'srcset="https://scontent-arn2-1'))
	pic2=list(find_all(scr, '.jpg'))
	response = requests.get(scr[(pic1[0]+8):(4+[i for i in pic2 if i > pic1[0]][0])])
	img_file = Image.open(BytesIO(response.content))
	img = img_file.load()
	[xs, ys] = img_file.size
	return pop_col(img,xs,ys)

	
def get_user_lnks(dr, usr, cyc):
	#user = 'prof_denglish'#'olga_buravtseva'#'mona_lisza' #'liebe_gabel'
	dr.switch_to.window(dr.window_handles[0])
	dr.get('https://www.instagram.com/' + usr)
	main_window = dr.current_window_handle

	dr.switch_to.window(main_window)
	dr.execute_script("window.open('https://www.instagram.com/" + usr + "');")
	dr.switch_to.window(dr.window_handles[1])
	time.sleep(time_wait)
	dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
	dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
	dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)

	time.sleep(time_wait)
	scr=dr.page_source

	places=list(find_all(scr, '/p/')) 
	lnks = [scr[(places[0]+3):(places[0]+14)]]

	for j in range(1,len(places)-1):
		lnks = lnks + [scr[(places[j]+3):(places[j]+14)]]
		lnks = lnks + [scr[(places[j]+3):(places[j]+43)]]

	for i in range(1,cyc):
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		time.sleep(time_wait)
		scr=dr.page_source
		places=list(find_all(scr, '/p/'))
		for j in range(0,len(places)-1):
			lnks = lnks + [scr[(places[j]+3):(places[j]+42)]]
		if i % 50 == 0:
			print(i)
	return list(sorted(set(lnks)))

def insta_logged(dr):
	time.sleep(0.5)
	main_url = "https://www.instagram.com/accounts/emailsignup/"
	dr.get(main_url)
	time.sleep(0.5)
	dr.find_elements_by_css_selector('.yZn4P')[0].click() 
	time.sleep(0.1)
	dr.find_elements_by_css_selector('#email')[0].send_keys("s_alyoshkin@yahoo.com")
	time.sleep(0.1)
	dr.find_elements_by_css_selector('#pass')[0].send_keys("LEEanor457047")
	time.sleep(0.1)
	dr.find_elements_by_css_selector('#pass')[0].send_keys(Keys.ENTER)
	
def get_insta_stats(dr, foll):
	stat = pd.DataFrame(columns=['names','posts','followers','following'])
	dr.switch_to.window(dr.window_handles[0])
	dr.get("https://www.instagram.com/")
	time.sleep(0.5)
	dr.switch_to.window(dr.window_handles[0])
	main_window = dr.current_window_handle
	for i in range(0, len(foll)-1):
	#for i in range(0, 3):
        #driver.switch_to.window(main_window)
		try:
			dr.execute_script("window.open('https://www.instagram.com/" + foll[i] + "');")
			dr.switch_to.window(dr.window_handles[1])
			time.sleep(0.1)
			try:
				stat.loc[i,'names']=foll[i]
			except:
				nms_fail=i
			try:
				stat.loc[i,'posts']=dr.find_elements_by_class_name("g47SY")[0].text
			except:
				posts_fail=i
			try:
				stat.loc[i,'followers']=dr.find_elements_by_class_name("g47SY")[1].text
			except:
				foll_fail=i
			try:
				stat.loc[i,'following']=dr.find_elements_by_class_name("g47SY")[2].text
			except:
				following_fail=i
			dr.close()
		except:
			fail=i
		dr.switch_to.window(main_window)
		if i % 10 == 0:
			print(str(round(100*i/len(foll))) + '%')
	return stat

def unsubscribe_insta(dr, un):
	dr.switch_to.window(dr.window_handles[0])
	#dr.get("https://www.instagram.com/")
	#time.sleep(0.5)
	dr.switch_to.window(dr.window_handles[0])
	main_window = dr.current_window_handle
	for i in range(0, len(un)):
	#for i in range(0, 3):
        #driver.switch_to.window(main_window)
		try:
			dr.execute_script("window.open('https://www.instagram.com/" + un[i] + "');")
			dr.switch_to.window(dr.window_handles[1])
			time.sleep(time_wait)
			try:
				dr.find_element_by_css_selector('.yZn4P').click()
				time.sleep(0.2)
				dr.find_element_by_class_name('aOOlW').click()
				time.sleep(0.8)
			except:
				unsubscr_fail=i
			dr.close()
		except:
			fail=i
		dr.switch_to.window(main_window)
		if i % 10 == 0:
			print(str(round(100*i/len(un))) + '%')


def get_lnks_by_url(dr,num_iter,link):
	#main_link = 'https://www.instagram.com/' + user + '/'
	#driver.get(main_link)
	#driver.switch_to.window(main_window)
	dr.switch_to.window(dr.window_handles[0])
	#driver.get('https://www.instagram.com/' + user)
	dr.get(link)
	main_window = dr.current_window_handle

	dr.switch_to.window(main_window)
	time.sleep(time_wait)
	dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
	dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
	dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)

	time.sleep(time_wait)
	scr=dr.page_source

	places=list(find_all(scr, '/p/'))
	ln = [scr[(places[0]+3):(places[0]+14)]]

	for j in range(1,len(places)-1):
		ln = ln + [scr[(places[j]+3):(places[j]+14)]]
		#lnks = lnks + [scr[(places[j]+3):(places[j]+43)]]

	for i in range(1,num_iter):
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		dr.find_element_by_tag_name("body").send_keys(Keys.SPACE)
		time.sleep(time_wait)
		scr=dr.page_source
		places=list(find_all(scr, '/p/'))
		for j in range(0,len(places)-1):
			ln = ln + [scr[(places[j]+3):(places[j]+14)]]
			#ln = ln + [scr[(places[j]+3):(places[j]+42)]]
		if i % 50 == 0:
			time.sleep(time_wait)
			dr.find_element_by_tag_name("body").send_keys(Keys.PAGE_UP)
			dr.find_element_by_tag_name("body").send_keys(Keys.PAGE_UP)
			dr.find_element_by_tag_name("body").send_keys(Keys.PAGE_UP)
			dr.find_element_by_tag_name("body").send_keys(Keys.PAGE_UP)
			time.sleep(time_wait)
			print(i)
	ln = list(sorted(set(ln)))
	#for j in range(1,len(places)-1):
	#    lnks = lnks + [scr[(places[j]+3):(places[j]+14)]]
	return ln
