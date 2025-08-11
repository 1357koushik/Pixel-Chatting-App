# -*- coding: utf-8 -*-
"""
@author: Moram Koushik
"""
from kivy.uix.effectwidget import EffectWidget, HorizontalBlurEffect, VerticalBlurEffect
from kivyauth.google_auth import initialize_google, login_google
from kivy.graphics import Color, RoundedRectangle, Rectangle
from android.runnable import run_on_ui_thread as run_thread
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.core.image import Image as CoreImage
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.textfield import MDTextField
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDIconButton
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.spinner import MDSpinner
from sqlite3 import connect as sconnect
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from webbrowser import open as uopen
from PIL import ImageOps, ImageDraw
from kivy.core.window import Window
from android import activity as act
from multiprocessing import Process
from kivymd.app import MDApp as App
from android import AndroidService
from kivy.uix.button import Button
from os import remove as removefil
from kivy.clock import mainthread
from re import search as research
from jnius import autoclass, cast
from kivy.uix.image import Image
from kivy.uix.label import Label
from datetime import datetime
from PIL import Image as img
from kivy.clock import Clock
from ast import literal_eval
from random import randint
from time import strftime
from io import BytesIO
from kivy.properties import ObjectProperty
from uuid import uuid4
from os import path
import pymysql



dark_m_switch = '''
MDSwitch:
    active: True
    icon_active: "check"
    icon_active_color: "grey"
    icon_inactive: "close"
    icon_inactive_color: "grey"
'''



class myApp(App):
    def build(self):
        try:
            global start_main
            #===============jnius=============
            change1="45"
            change2="30"
            change3=0.43
            change4=100
            change5="40"
            c1="000000"
            c2=(0,0,0,0)
            if self.theme_cls.theme_style!="Light":
                c2=(1,1,1,1)
                c1="ffffff"
            if Window.width<1200:
                change1="80"
                change2="60"
                change3=0.6
                change4=200
                change5="50"
                
            MediaStore_Images_Media_DATA = "_data"
            RESULT_LOAD_IMAGE = 1
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            io = autoclass('java.io.File')
            FileUtils=autoclass('android.os.FileUtils')
            # AndroidView=autoclass("android.view.View")
            # WebViewA = autoclass('android.webkit.WebView')
            Intent = autoclass('android.content.Intent')
            Activity = autoclass('android.app.Activity')
            # WebViewClient = autoclass('android.webkit.WebViewClient')
            # LinearLayout = autoclass('android.widget.LinearLayout')
            Context = autoclass('android.content.Context')
            Uri = autoclass('android.net.Uri')
            # ViewGroup = autoclass('android.view.ViewGroup')
            # LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
            
            
            #================jnius===============
            
            
            prolist=[]
            def cp(dp):
                newS=''
                for car in dp:
                    newS=newS+chr(ord(car)+189)
                return newS
            def cp_(dp):
                newS=''
                for car in dp:
                    newS=newS+chr(ord(car)-189)
                return newS
            def exit_app(vv):
                quit()
            def clearw(ma,war):
                ma.remove_widget(war)
                
            def opendp(pa,main,w):
                w.effects = [HorizontalBlurEffect(size=5.0),VerticalBlurEffect(size=5.0)]
                pat=str()
                for t in prolist:
                    if t[0]==pa:
                        pat=t[1]
                pima=BoxLayout(orientation="vertical",spacing="12dp",size_hint_y=None,height="300dp")
                pim=Image(source=pat,allow_stretch= True, size=(300,300))
                pima.add_widget(pim)
                bac=MDFlatButton(text="BACK", text_color=self.theme_cls.primary_color)
                def bacp(d):
                    w.effects = []
                    imop.dismiss()
                bac.bind(on_release=bacp)
                imop=MDDialog(type="custom",content_cls=pima,buttons=[bac])
                imop.open()
            
            
            
            
            
            
            
            #           =======  =========     =      ====    =========
            #           =            =        = =     =   =       =
            # ========  =====        =       =   =    ====        =     ========
            #               =        =      =======   =   =       =
            #          ======        =     =       =  =    =      =
               
            
            
            
            
            
            class ZBox(BoxLayout):
                tre=ObjectProperty(None)
                def on_kv_post(self,obj):
                    self.flip=0
                def on_touch_down(self,touch):
                    if self.collide_point(*touch.pos):
                        touch.grab(self)
                        if touch.is_double_tap:
                            if self.flip == 0:
                                self.size=2000,(self.tre.size[1]/self.tre.size[0])*2000
                                self.flip=1
                            else:
                                self.size=self.tre.size
                                self.flip=0
            b="""
#:import C kivy.utils.get_color_from_hex
#:import img PIL.Image
<MyButt>:
    size_hint: None, None
    height: self.texture_size[1] + 70
    width: self.texture_size[0] + 70
    markup: True
    size_hint_y: None
<it>:
    size_hint: None, None
    height: img.open(self.background_normal).size[1]
    width: img.open(self.background_normal).size[0]
    markup: True
    size_hint_y: None
<it1>:
    markup: True
<it2>:
    size_hint: None, None
    height: 100
    width: 100/(int(img.open(self.background_normal).size[1])/100)*(int(img.open(self.background_normal).size[0])/100)
    markup: True
    size_hint_y: None
<m2>
    size_hint: None, None
    height: self.texture_size[1] + 70
    width: self.texture_size[0] + 70
    markup: True
    size_hint_y: None
<tbtn>:
    size_hint: None, None
    height: self.texture_size[1] + 20
    width: self.texture_size[0] + 10
<ti>
    cols: 2
    rows: 1
    spacing: 50
    size_hint_y: None
    height: self.minimum_height + 20
<ct>
    padding_x:
        [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,
        0] if self.text else [self.center[0], 0]
    padding_y:
        [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
<zoompic>:
	orientation:"vertical"
	ScrollView:
		bar_width:40
		#scroll_type:["bars"]
		ZBox:
			pos_hint:{"center_x":0.5,"center_y":.5}
			id:box
			size_hint:None,None
			Widget:
				id:mdz
				canvas:
					Rectangle:
						pos:self.pos
						size:box.size
<ZBox>:
            """
            Builder.load_string(b)
            class MyButt(Button):
            	pass
            class it1(Button):
            	pass
            class ti(GridLayout):
            	pass
            class it2(Button):
            	pass
            class tbtn(Label):
            	pass
            class it(Button):
            	pass
            class m2(Button):
            	pass
            class ct(TextInput):
                pass
            def ch(filePath):
                if path.exists(filePath):
                    numb = 1
                    while True:
                        newPath = "{0}_{2}{1}".format(*path.splitext(filePath) + (numb,))
                        if path.exists(newPath):
                            numb += 1
                        else:
                            return newPath
                return filePath
            def showch(ema,usn,nam,f,mem):
                global start_main
                f.clear_widgets()
                ef=EffectWidget()
                con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                cur=con.cursor()
                cur.execute('SELECT * FROM `'+mem+'`')
                result=cur.fetchall()
                con.close()
                con=sconnect("usordlist.pix")
                cur=con.cursor()
                try:
                    cur.execute("DELETE FROM uslist WHERE na = '"+mem+"'")
                    cur.execute("DROP TABLE `"+mem+"`")
                except:
                    pass
                list=[]
                templist2=[]
                for a in cur.fetchall():
                	templist2.append(a[0])
                tempch=0
                try:
                	result[0][0]
                	tempch=1
                except:
                	pass
                totalpoints=int(open('total.pix',mode='r').read())
                if tempch==1:
                    for a in result:
                        if a[0] in templist2:
                            cur.execute('INSERT INTO `'+a[0]+'`(oi,mes,ex,exn,tm,id) VALUES (?,?,?,?,?,?)',(a[1],a[2],a[3],a[4],a[5],a[6]))
                            con.commit()
                            totalpoints=int(open('total.pix',mode='rb').read())+1
                            with open('total.pix',mode='w') as fil:
                                fil.write(str(totalpoints))
                            cur.execute("UPDATE uslist SET points = '"+str(totalpoints)+"' WHERE na ='"+str(a[0])+"'")
                            con.commit()
                        else:
                            totalpoints=int(open('total.pix',mode='rb').read())+1
                            with open('total.pix',mode='w') as fil:
                                fil.write(str(totalpoints))
                            cur.execute('INSERT INTO uslist(na,points) VALUES (?,?)',(a[0],str(totalpoints)))
                            con.commit()
                            try:
                              cur.execute('CREATE TABLE `'+a[0]+'`(oi VARCHAR(50),mes VARCHAR(225),ex LONGBLOB, exn VARCHAR(225), tm VARCHAR(50), id VARCHAR(50))')
                              con.commit()
                            except:
                                pass
                            cur.execute('INSERT INTO `'+a[0]+'`(oi,mes,ex,exn,tm,id) VALUES (?,?,?,?,?,?)',(a[1],a[2],a[3],a[4],a[5],a[6]))
                            con.commit()
                    con.close()
                    con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                    cur=con.cursor()
                    cur.execute("DROP TABLE `"+mem+"`")
                    con.commit()
                    cur.execute("CREATE TABLE `"+mem+"`(na VARCHAR(50), oi VARCHAR(50), message VARCHAR(225), ex LONGBLOB, exn VARCHAR(225), tm VARCHAR(50), id VARCHAR(50))")
                    con.commit()
                    con.close()
                Window.softinput_mode='pan'
                size = (100, 100)
                mask = img.new('L', size, 0)
                draw = ImageDraw.Draw(mask) 
                draw.ellipse((0, 0) + size, fill=255)
                im = img.open(ema+".png")
                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                output.putalpha(mask)
                im=BytesIO()
                output.save(im, format='png')
                im.seek(0)
                im = CoreImage(BytesIO(im.read()), ext='png')
                subgrid=GridLayout(rows=1, spacing=0,size_hint_y=None,pos_hint={"center_x":0.5,"center_y":0.97})
                def propen(opema):
                    f.clear_widgets()
                    con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                    cur=con.cursor()
                    cur.execute("SELECT k,s,h,i FROM sm WHERE o = '"+ema+"'")
                    cre=cur.fetchall()
                    con.close()
                    for result in cre:
                        urn=result[0]
                        usna=result[1]
                        bio=result[2]
                        with open(ema+".png","wb") as fil:
                            fil.write(result[3])
                        prof=ema+".png"
                        pimg=Image(source=prof,size_hint=(None,None),width=int(400/(int(img.open(prof).size[1])/100)*(int(img.open(prof).size[0])/100)),height=400,allow_stretch=True,pos_hint={"center_x":0.2,"center_y":0.83})
                        g=GridLayout(size_hint_y=None,cols=2,pos_hint={"center_x":0.5,"center_y":0.97})
                        def cl(b):
                            showch(ema, usn, nam, f, mem)
                        urn=Label(text='[size=50][color='+c1+']'+urn+'[/size][/color]',markup=True)
                        urn.bind(on_press=cl)
                        na=Label(text='[size=50][color='+c1+']'+usna+'[/size][/color]',markup=True,pos_hint={"center_x":0.5,"center_y":0.75})
                        biob=Label(text='[size=40][color='+c1+']'+bio+'[/size][/color]',markup=True,pos_hint={"center_x":0.5,"center_y":0.68},halign='left')
                        cb=MDIconButton(icon="keyboard-return",size_hint=(None,None),size=(163,200))
                        cb.bind(on_press=cl)
                        f.add_widget(pimg)
                        g.add_widget(urn)
                        g.add_widget(cb)
                        f.add_widget(g)
                        f.add_widget(na)
                        f.add_widget(biob)
            
            
            
                class ib(ButtonBehavior, Image):
                    def on_press(self):
                        propen(ema)
                
                profipic=ib(texture=im.texture, size_hint=(None, 100))
                if self.theme_cls.theme_style=="Light":
                    cb="000000"
                else:
                    cb="ffffff"
                name=MDLabel(text="[b][size=40][color="+cb+"]"+usn+"[/size][/b] \n [size=40]"+nam+"[/size][/color]",text_size=(850,70),markup=True)
                name.bind(on_press=propen)
                sbb=Button(background_normal="x.png",background_down="x.png",border=(0,0,0,0),pos=(1100,1750),size_hint=(None,None),size=(130,160))
                def esm(but):
                    f.clear_widgets()
                    resh.cancel()
                    start_main(f, mem)
                sbb.bind(on_press=esm)
                subgrid.add_widget(profipic)
                subgrid.add_widget(name)
                subgrid.add_widget(sbb)
                layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
                layout.bind(minimum_height=layout.setter('height'))
                con=sconnect("usordlist.pix")
                cur=con.cursor()
                cur.execute("SELECT * FROM `"+ema+"`")
                list=[]
                resultf=cur.fetchall()
                with open("temp.py","w") as fil:
                    fil.write("wed="+str(resultf))
                con.close()
                if resultf!=[]:
                    for a in resultf:
                        if a[0]=="o":
                            if a[1]=="None":
                                path=ch(a[3])
                                with open(path,mode="wb") as fil:
                                    fil.write(a[2])
                                list.append((" ","None",path,a[4]))
                            else:
                                list.append((" ",a[1],a[4]))
                        else:
                            if a[1]=="None":
                                path=ch(a[3])
                                with open(path,mode="wb") as fil:
                                    fil.write(a[2])
                                list.append(("None",path,a[4]))
                            else:
                                list.append((a[1],a[4]))
                def sh(but):
                    class zoompic(BoxLayout):
                        tre=ObjectProperty(None)
                        def on_kv_post(self,obj):
                            self.flip=0
                            self.tre=CoreImage(str(but.background_normal)).texture
                            self.ids.box.tre=self.tre
                            self.ids.box.size=self.tre.size
                            self.ids.mdz.canvas.children[1].texture=self.tre
                    ef.effects = [HorizontalBlurEffect(size=5.0),VerticalBlurEffect(size=5.0)]
                    pima=BoxLayout(orientation="vertical",spacing="12dp",size_hint=(None,None),size=(Window.width, Window.height-300))
                    pim=zoompic()
                    pima.add_widget(pim)
                    bac=MDFlatButton(text="BACK", text_color=self.theme_cls.primary_color)
                    def bacp(d):
                        ef.effects = []
                        imop.dismiss()
                    bac.bind(on_release=bacp)
                    imop=MDDialog(type="custom",content_cls=pima,buttons=[bac],size_hint=(None,None),size=(Window.width, Window.height-300))
                    imop.open()
                for ifu in list:
                    g=ti()
                    ttl=ifu[-1]
                    utcz=str(strftime("%z"))
                    utch=int(utcz[1]+utcz[2])
                    utcm=int(utcz[3]+utcz[4])
                    if utcz[0]=="+":
                        utch=utch+int(ttl.split(":")[0])
                        if utch>12:
                            utch=utch-12
                        utcm=utcm+int(ttl.split(":")[1])
                        if utcm>60:
                            utcm=utcm-60
                            utch+=1
                    else:
                        utch=int(ttl.split(":")[0])-utch
                        utcm=int(ttl.split(":")[1])-utcm
                    if len(str(utcm))==1:
                        utcm="0"+str(utcm)
                    if len(ifu)==3:
                        ifu=(ifu[0],ifu[1],str(utch)+":"+str(utcm))
                    elif len(ifu)==4:
                        ifu=(ifu[0],ifu[1],ifu[2],str(utch)+":"+str(utcm))
                    else:
                        ifu=(ifu[0],str(utch)+":"+str(utcm))
                    sg=GridLayout(cols=2,rows=1,height=15,size_hint_y=None)
                    if self.theme_cls.theme_style=="Light":
                        cb="000000"
                    else:
                        cb="ffffff"
                    if ifu[0]==' ':
                        if ifu[1]=="None":
                            l=Label(text=' ')
                            g.add_widget(l)
                            t=it1(background_normal=ifu[2],background_down=ifu[2],border=(0,0,0,0),size_hint=(None,None),width=int((600/(int(img.open(ifu[2]).size[1])/100))*(int(img.open(ifu[2]).size[0])/100)),height=600)
                            t.bind(on_press=sh)
                            g.add_widget(t)
                            sg.add_widget(MDLabel(text=' '))
                            sg.add_widget(tbtn(text='[size=30][color='+cb+']'+ifu[-1]+'[/size][/color]',markup=True,halign='right'))
                        else:
                            b=ifu[1]
                            if len(ifu[1])>30:
                                b=""
                                c=0
                                for a in [ifu[1][i:i+30] for i in range(0, len(ifu[1]), 30)]:
                                    if len(ifu[1])==c-1:
                                        b+=a
                                    else:
                                        b+=a+"\n"
                                    c+=1
                            ime=MyButt(text='[color=000000]'+b+'[/color]',background_normal="bc.png",background_down="bc.png")
                            l=Label(text=' ')
                            g.add_widget(l)
                            g.add_widget(ime)
                            sg.add_widget(MDLabel(text=' '))
                            sg.add_widget(tbtn(text='[size=30][color='+cb+']'+ifu[-1]+'[/size][/color]',markup=True,halign='right'))
                    else:
                        if ifu[0]=="None":
                            t=it1(background_normal=ifu[1],background_down=ifu[1],border=(0,0,0,0),size_hint=(None,None),width=int((600/(int(img.open(ifu[1]).size[1])/100))*(int(img.open(ifu[1]).size[0])/100)),height=600)
                            t.bind(on_press=sh)
                            g.add_widget(t)
                            l=Label(text=' ')
                            g.add_widget(l)
                            sg.add_widget(tbtn(text='[size=30][color='+cb+']'+ifu[-1]+'[/size][/color]',markup=True,halign='left'))
                            sg.add_widget(Label(text=' '))
                        else:
                            b=ifu[0]
                            if len(ifu[0])>30:
                                b=""
                                c=0
                                for a in [ifu[0][i:i+30] for i in range(0, len(ifu[0]), 30)]:
                                    if len(ifu[0])==c-1:
                                        b+=a
                                    else:
                                        b+=a+"\n"
                                    c+=1
                            ime=m2(text='[color=000000]'+b+'[/color]',background_normal="bc.png",background_down="bc.png")
                            g.add_widget(ime)
                            l=Label(text=' ')
                            g.add_widget(l)
                            sg.add_widget(tbtn(text='[size=30][color='+cb+']'+ifu[-1]+'[/size][/color]',markup=True,halign='left'))
                            sg.add_widget(Label(text=' '))
                    layout.add_widget(g)
                    layout.add_widget(sg)
                root = ScrollView(size_hint=(None,None), size=(Window.width, Window.height-300),pos=(0,150))
                g=GridLayout(cols=1,rows=1,size_hint_y=None,height=70)
                seng=GridLayout(cols=5,rows=1,size_hint_y=None,height=80,pos=(0,70))
                te=TextInput(multiline=True,hint_text="send something here",size_hint=(None,None),height=150,width=Window.width-220)
                adpic=MDIconButton(icon="attachment",md_bg_color=self.theme_cls.primary_color,icon_size="32sp")
                sen=MDIconButton(icon="send-outline",md_bg_color=self.theme_cls.primary_color,icon_size="32sp")
                def refresh(cloc):
                    con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                    cur=con.cursor()
                    cur.execute('SELECT * FROM `'+mem+'`')
                    result=cur.fetchall()
                    con.close()
                    con=sconnect("usordlist.pix")
                    cur=con.cursor()
                    try:
                        cur.execute("DELETE FROM uslist WHERE na = '"+mem+"'")
                        cur.execute("DROP TABLE `"+mem+"`")
                    except:
                        pass
                    list=[]
                    templist2=[]
                    for a in cur.fetchall():
                    	templist2.append(a[0])
                    tempch=0
                    try:
                    	result[0][0]
                    	tempch=1
                    except:
                    	pass
                    totalpoints=int(open('total.pix',mode='r').read())
                    if tempch==1:
                        for a in result:
                            if a[0] in templist2:
                                cur.execute('INSERT INTO `'+a[0]+'`(oi,mes,ex,exn,tm,id) VALUES (?,?,?,?,?,?)',(a[1],a[2],a[3],a[4],a[5],a[6]))
                                con.commit()
                                totalpoints=int(open('total.pix',mode='rb').read())+1
                                with open('total.pix',mode='w') as fil:
                                    fil.write(str(totalpoints))
                                cur.execute("UPDATE uslist SET points = '"+str(totalpoints)+"' WHERE na ='"+str(a[0])+"'")
                                con.commit()
                            else:
                                totalpoints=int(open('total.pix',mode='rb').read())+1
                                with open('total.pix',mode='w') as fil:
                                    fil.write(str(totalpoints))
                                cur.execute('INSERT INTO uslist(na,points) VALUES (?,?)',(a[0],str(totalpoints)))
                                con.commit()
                                try:
                                    cur.execute('CREATE TABLE `'+a[0]+'`(oi VARCHAR(50),mes VARCHAR(225),ex LONGBLOB, exn VARCHAR(225), tm VARCHAR(50), id VARCHAR(50))')
                                    con.commit()
                                except:
                                    cur.execute('INSERT INTO `'+a[0]+'`(oi,mes,ex,exn,tm,id) VALUES (?,?,?,?,?,?)',(a[1],a[2],a[3],a[4],a[5],a[6]))
                                    con.commit()
                        con.close()
                        con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                        cur=con.cursor()
                        cur.execute("DROP TABLE `"+mem+"`")
                        con.commit()
                        cur.execute("CREATE TABLE `"+mem+"`(na VARCHAR(50), oi VARCHAR(50), message VARCHAR(225), ex LONGBLOB, exn VARCHAR(225), tm VARCHAR(50), id VARCHAR(50))")
                        con.commit()
                        con.close()
                    import temp
                    resultf=temp.wed
                    con=sconnect("usordlist.pix")
                    cur=con.cursor()
                    cur.execute("SELECT * FROM `"+ema+"`")
                    re=cur.fetchall()
                    con.close()
                    for fora in resultf:
                        if fora in re:
                            re.remove(fora)
                    for a in re:
                        resultf.append(a)
                    with open("temp.py","w") as fil:
                        fil.write("wed="+str(resultf))
                    list=[]
                    if re!=[]:
                        for a in re:
                            if a[0]=="o":
                                if a[1]=="None":
                                    path=ch(a[3])
                                    with open(path,mode="wb") as fil:
                                        fil.write(a[2])
                                    list.append((" ","None",path,a[4]))
                                else:
                                    list.append((" ",a[1],a[4]))
                            else:
                                if a[1]=="None":
                                    path=ch(a[3])
                                    with open(path,mode="wb") as fil:
                                        fil.write(a[2])
                                    list.append(("None",path,a[4]))
                                else:
                                    list.append((a[1],a[4]))
                        for ifu in list:
                            g=ti()
                            ttl=ifu[-1]
                            utcz=str(strftime("%z"))
                            utch=int(utcz[1]+utcz[2])
                            utcm=int(utcz[3]+utcz[4])
                            if utcz[0]=="+":
                                utch=utch+int(ttl.split(":")[0])
                                if utch>12:
                                    utch=utch-12
                                utcm=utcm+int(ttl.split(":")[1])
                                if utcm>60:
                                    utcm=utcm-60
                                    utch+=1
                            else:
                                utch=int(ttl.split(":")[0])-utch
                                utcm=int(ttl.split(":")[1])-utcm
                            if len(str(utcm))==1:
                                utcm="0"+str(utcm)
                            if len(ifu)==3:
                                ifu=(ifu[0],ifu[1],str(utch)+":"+str(utcm))
                            elif len(ifu)==4:
                                ifu=(ifu[0],ifu[1],ifu[2],str(utch)+":"+str(utcm))
                            else:
                                ifu=(ifu[0],str(utch)+":"+str(utcm))
                            sg=GridLayout(cols=2,rows=1,height=15,size_hint_y=None)
                            if self.theme_cls.theme_style=="Light":
                                cb="000000"
                            else:
                                cb="ffffff"
                            if ifu[0]==' ':
                                if ifu[1]=="None":
                                    l=Label(text=' ')
                                    g.add_widget(l)
                                    t=it1(background_normal=ifu[2],background_down=ifu[2],border=(0,0,0,0),size_hint=(None,None),width=int((600/(int(img.open(ifu[2]).size[1])/100))*(int(img.open(ifu[2]).size[0])/100)),height=600)
                                    t.bind(on_press=sh)
                                    g.add_widget(t)
                                    sg.add_widget(MDLabel(text=' '))
                                    sg.add_widget(tbtn(text='[size=30][color='+cb+']'+ifu[-1]+'[/size][/color]',markup=True,halign='right'))
                                else:
                                    b=ifu[1]
                                    if len(ifu[1])>30:
                                        b=""
                                        c=0
                                        for a in [ifu[1][i:i+30] for i in range(0, len(ifu[1]), 30)]:
                                            if len(ifu[1])==c-1:
                                                b+=a
                                            else:
                                                b+=a+"\n"
                                            c+=1
                                    ime=MyButt(text='[color=000000]'+b+'[/color]',background_normal="bc.png",background_down="bc.png")
                                    l=Label(text=' ')
                                    g.add_widget(l)
                                    g.add_widget(ime)
                                    sg.add_widget(MDLabel(text=' '))
                                    sg.add_widget(tbtn(text='[size=30][color='+cb+']'+ifu[-1]+'[/size][/color]',markup=True,halign='left'))
                            else:
                                if ifu[0]=="None":
                                    t=it1(background_normal=ifu[1],background_down=ifu[1],border=(0,0,0,0),size_hint=(None,None),width=int((600/(int(img.open(ifu[1]).size[1])/100))*(int(img.open(ifu[1]).size[0])/100)),height=600)
                                    t.bind(on_press=sh)
                                    g.add_widget(t)
                                    l=Label(text=' ')
                                    g.add_widget(l)
                                    sg.add_widget(tbtn(text='[size=30][color='+cb+']'+ifu[-1]+'[/size][/color]',markup=True,halign='left'))
                                    sg.add_widget(Label(text=' '))
                                else:
                                    b=ifu[0]
                                    if len(ifu[0])>30:
                                        b=""
                                        c=0
                                        for a in [ifu[0][i:i+30] for i in range(0, len(ifu[0]), 30)]:
                                            if len(ifu[0])==c-1:
                                                b+=a
                                            else:
                                                b+=a+"\n"
                                            c+=1
                                    ime=m2(text='[color=000000]'+b+'[/color]',background_normal="bc.png",background_down="bc.png")
                                    g.add_widget(ime)
                                    l=Label(text=' ')
                                    g.add_widget(l)
                                    sg.add_widget(tbtn(text='[size=30][color='+cb+']'+ifu[-1]+'[/size][/color]',markup=True,halign='left'))
                                    sg.add_widget(Label(text=' '))
                            layout.add_widget(g)
                            layout.add_widget(sg)
                            try:
                                layout.remove_widget(self.g)
                            except:
                                pass
                def send(txt):
                    try:
                        import sepro
                        sepros = sepro.a
                    except:
                        with open("sepro.py","w") as fil:
                            fil.write("a=False")
                        sepros=True
                    if sepros:
                        utc=str(datetime.utcnow().strftime('%I:%M'))
                        id=uuid4().hex
                        con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                        cur=con.cursor()
                        if str(type(txt))=="<class 'str'>":
                            cur.execute("INSERT INTO `"+ema+"`(na,oi,message,ex,exn,tm,id) VALUES (%s,%s,%s,%s,%s,%s,%s)",(mem,"i","None",open(txt,"rb").read(),txt.split("/")[-1],utc,id))
                            con.commit()
                            con.close()
                            con=sconnect("usordlist.pix")
                            cur=con.cursor()
                            cur.execute("INSERT INTO `"+ema+"`(oi,mes,ex,exn,tm,id) VALUES (?,?,?,?,?,?)",("o","None",open(txt,"rb").read(),txt.split("/")[-1],utc,id))
                            con.commit()
                            con.close()
                            Process(target=refresh("vl"))
                        else:
                            cur.execute("INSERT INTO `"+ema+"`(na,oi,message,ex,exn,tm,id) VALUES (%s,%s,%s,%s,%s,%s,%s)",(mem,"i",te.text,None,"None",utc,id))
                            con.commit()
                            con.close()
                            con=sconnect("usordlist.pix")
                            cur=con.cursor()
                            cur.execute("INSERT INTO `"+ema+"`(oi,mes,ex,exn,tm,id) VALUES (?,?,?,?,?,?)",("o",te.text,None,"None",utc,id))
                            con.commit()
                            con.close()
                            Process(target=refresh("n"))
                        with open("sepro.py","w") as fil:
                            fil.write("a=True")
                        te.text=""
                def sendpic(b):
                    self.g=ti()
                    l=Label(text=' ')
                    self.g.add_widget(l)
                    t=it1(background_normal="senpicbg.png",background_down="senpicbg.png",border=(0,0,0,0),size_hint=(None,None),width=int((600/(int(img.open("senpicbg.png").size[1])/100))*(int(img.open("senpicbg.png").size[0])/100)),height=600)
                    self.g.add_widget(t)
                    @run_thread
                    def Push(butonn):
                        activity1 = cast('android.app.Activity', PythonActivity.mActivity)
                        def on_activity_result(request_code, result_code, intent):
                            if request_code != RESULT_LOAD_IMAGE:
                                return
                            elif result_code == Activity.RESULT_CANCELED:
                                return
                            elif result_code != Activity.RESULT_OK:
                                raise NotImplementedError('Unknown result_code "{}"'.format(result_code))
                            else:
                                alc=1
                                selectedImage = intent.getData()
                                filePathColumn = [MediaStore_Images_Media_DATA]
                                cursor = activity1.getContentResolver().query(selectedImage,
                                        filePathColumn, None, None, None)
                                cursor.moveToFirst()
                    
                                columnIndex = cursor.getColumnIndex(filePathColumn[0])
                                picturePath = cursor.getString(columnIndex)
                                cursor.close()
                                selectedUri = intent.getData()
                                docStream = activity1.getContentResolver().openInputStream(selectedUri)
                                try:
                                    layout.add_widget(self.g)
                                except:
                                    alc=0
                                if alc==1:
                                    def send_in(ara):
                                        def send_ini(Ss):
                                            sip=ch(picturePath.split("/")[-1])
                                            FileUtils.copyToFile(docStream,io(sip))
                                            im=img.open(sip)
                                            if im.size[0]>2000:
                                                basewidth = 2000
                                                wpercent = (basewidth/float(im.size[1]))
                                                hsize = int((float(im.size[0])*float(wpercent)))
                                                im = im.resize((hsize,basewidth))
                                                im.save(sip)
                                            Process(target=send(sip)) 
                                        Clock.schedule_once(send_ini, 0.5)
                                    Clock.schedule_once(send_in, 0.5)
                            
            
                        act.bind(on_activity_result=on_activity_result)
                          
                        intent= Intent()
                        intent.setAction(Intent.ACTION_PICK)
                        intent.setData(Uri.parse('content://media/internal/images/media'))
                        
                        activity1.startActivityForResult(intent, RESULT_LOAD_IMAGE)
                    Push(b)
                      
                sen.bind(on_press=send)
                adpic.bind(on_press=sendpic)
                seng.add_widget(adpic)
                seng.add_widget(Label(text=' ',size_hint_x=None,width=20))
                seng.add_widget(te)
                seng.add_widget(Label(text=' ',size_hint_x=None,width=20))
                seng.add_widget(sen)
                layout.add_widget(g)
                root.add_widget(layout)
                ef.add_widget(root)
                ef.add_widget(subgrid)
                f.add_widget(ef)
                f.add_widget(seng)
                root.scroll_to(g)
                def init_refresh(saf):
                    Process(target=(saf))
                resh=Clock.schedule_interval(init_refresh, 3)
            
            
            
            #           =======  =========     =      ====    =========     ======
            #           =            =        = =     =   =       =              =
            # ========  =====        =       =   =    ====        =         ======   ========
            #               =        =      =======   =   =       =         =
            #          ======        =     =       =  =    =      =         ======
               
            
            
                
            def start_main(mainm,encrypted,ani=None,abtn=None):
                Window.softinput_mode=""
                w=FloatLayout()
                allg=GridLayout(cols=1)
                w.add_widget(allg)
                con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                cur=con.cursor()
                cur.execute('SELECT * FROM `'+encrypted+'`')
                result=cur.fetchall()
                con.close()
                con=sconnect("usordlist.pix")
                cur=con.cursor()
                try:
                    cur.execute("DELETE FROM uslist WHERE na = '"+encrypted+"'")
                    cur.execute("DROP TABLE `"+encrypted+"`")
                except:
                    pass
                try:
                    cur.execute('CREATE TABLE uslist(na VARCHAR(50), points INT(225))')
                    con.commit()
                except:
                	pass
                try:
                	totalpoints=int(open('total.pix',mode='r').read())
                except:
                    with open('total.pix',mode='w') as fil:
                        fil.write('0')
                    totalpoints=0
                cur.execute('SELECT * FROM uslist')
                list=[]
                templist2=[]
                for a in cur.fetchall():
                	templist2.append(a[0])
                tempch=0
                try:
                	result[0][0]
                	tempch=1
                except:
                	pass
                if tempch==1:
                    for a in result:
                        if a[0] in templist2:
                            cur.execute('INSERT INTO `'+a[0]+'`(oi,mes,ex,exn,tm,id) VALUES (?,?,?,?,?,?)',(a[1],a[2],a[3],a[4],a[5],a[6]))
                            con.commit()
                            totalpoints=int(open('total.pix',mode='rb').read())+1
                            with open('total.pix',mode='w') as fil:
                                fil.write(str(totalpoints))
                            cur.execute("UPDATE uslist SET points = '"+str(totalpoints)+"' WHERE na ='"+str(a[0])+"'")
                            con.commit()
                        else:
                            totalpoints=int(open('total.pix',mode='rb').read())+1
                            with open('total.pix',mode='w') as fil:
                                fil.write(str(totalpoints))
                            cur.execute('INSERT INTO uslist(na,points) VALUES (?,?)',(a[0],str(totalpoints)))
                            con.commit()
                            try:
                              cur.execute('CREATE TABLE `'+a[0]+'`(oi VARCHAR(50),mes VARCHAR(225),ex LONGBLOB, exn VARCHAR(225), tm VARCHAR(50), id VARCHAR(50))')
                              con.commit()
                            except:
                                pass
                            cur.execute('INSERT INTO `'+a[0]+'`(oi,mes,ex,exn,tm,id) VALUES (?,?,?,?,?,?)',(a[1],a[2],a[3],a[4],a[5],a[6]))
                            con.commit()
                    con.close()
                    con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                    cur=con.cursor()
                    cur.execute("DROP TABLE `"+encrypted+"`")
                    con.commit()
                    cur.execute("CREATE TABLE `"+encrypted+"`(na VARCHAR(50), oi VARCHAR(50), message VARCHAR(225), ex LONGBLOB, exn VARCHAR(225), tm VARCHAR(50), id VARCHAR(50))")
                    con.commit()
                con.close()
                con=sconnect("usordlist.pix")
                cur=con.cursor()
                cur.execute('SELECT * FROM uslist')
                list={}
                for a in cur.fetchall():
                  list[a[0]]=int(a[1])
                con.close()
                u=str(sorted(list.items(),key= lambda  x: (x[1],x[0]),reverse=True))
                o=u.replace('(','')
                o=o.replace(')','')
                o=o.replace(", ",':')
                o=o.replace("':", "',")
                o=o.replace('[','{')
                o=o.replace(']','}')
                o=o.replace("',", "':")
                o=o.replace(":'", ",'")
                z = literal_eval(o)
                w1=str(z.keys())
                e2=w1.replace('dict_keys','')
                e4=e2.replace("(['","")
                e1=e4.replace("'])",'')
                f1=e1.split("', '")
                list=[]
                con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                cur=con.cursor()
                for a in f1:
                    if str(a)=="([])":
                        pass
                    else:
                        cur.execute("SELECT k,s,i FROM sm WHERE o = '"+a+"'")
                        fr=cur.fetchall()
                        with open(a+'.png',mode='wb') as fil:
                            fil.write(fr[0][2])
                        list.append((a+'.png',fr[0][0],fr[0][1]))
                con.close()
                mainm.clear_widgets()
                scl = ScrollView(size_hint_y=None,size=(Window.width,Window.height-350))
                a=0
                gril = GridLayout(cols=1, spacing=20, size_hint_y=None)
                gril.bind(minimum_height=gril.setter('height'))
                def shcfm(but,mem):
                    for a in prolist:
                        if but.text==a[2]:
                            emai=a[3]
                    con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                    cur=con.cursor()
                    cur.execute("SELECT k,s FROM sm WHERE o = '"+emai+"'")
                    resu=cur.fetchall()
                    showch(emai,resu[0][0],resu[0][1],mainm,mem)
                        
                for a in list:
                    size = (change4,change4)
                    mask = img.new('L', size, 0)
                    draw = ImageDraw.Draw(mask) 
                    draw.ellipse((0, 0) + size, fill=255)
                    im = img.open(a[0])
                    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                    output.putalpha(mask)
                    im=BytesIO()
                    output.save(im, format='png')
                    im.seek(0)
                    im = CoreImage(BytesIO(im.read()), ext='png')
                    subgrid=GridLayout(rows=1, spacing=0,size_hint_y=None,height=change4,width=change4)
                    class ib(ButtonBehavior, Image):
                        def on_press(self):
                            opendp(self.texture,mainm,w)
                    profipic=ib(texture=im.texture, size_hint=(None, None),height=change4,width=change4)
                    if self.theme_cls.theme_style=="Light":
                        cb="000000"
                    else:
                        cb="ffffff"
                    with open("tot.pix",mode="w") as fil:
                        fil.write("t1t2t3t4t5")
                    name=Button(text="[b][size="+change5+"][color="+cb+"]"+a[1]+"[/size][/b] \n [size=40]"+a[2]+"[/size][/color]",halign='left',background_down="bc.png",background_normal="bc.png",text_size=(800,150),background_color=c2,markup=True)
                    prolist.append((im.texture,a[0],name.text,a[0].replace(".png", "")))
                    def shcfm_init(but):
                        shcfm(but,encrypted)
                    name.bind(on_press=shcfm_init)
                    subgrid.add_widget(profipic)
                    subgrid.add_widget(name)
                    gril.add_widget(subgrid)
                scl.add_widget(gril)
                # with allg.canvas.before:
                #     Color(0,0,0,1)
                #     allg.bg_rect = Rectangle(pos=allg.pos, size=allg.size)
                #     def update_rect(instance, value):
                #         instance.bg_rect.pos = instance.pos
                #         instance.bg_rect.size = instance.size
                #     # listen to size and position changes
                #     allg.bind(pos=update_rect, size=update_rect)
                class ib(ButtonBehavior, Image):
                    def on_press(self):
                        try:
                            sall7.clear_widgets()
                        except:
                            pass
                        gril.clear_widgets()
                        allg.remove_widget(sall6)
                        allg.remove_widget(sall2)
                        self.inte=TextInput(multiline=False,size_hint=(change3,0.04),padding_y=40)
                        self.inte.bind(on_text_validate=self.sr)
                        sbba=AnchorLayout(anchor_x="center",anchor_y="center",size_hint=(None,None),size=(150,150))
                        sbb=MDIconButton(icon="keyboard-return", size_hint=(None,None),size=(51,43))
                        sbb.bind(on_press=self.rem)
                        sbba.add_widget(sbb)
                        sall7.add_widget(sbba)
                        sall7.add_widget(self.inte)
                        scl.size=(Window.width,Window.height-150)
                    def rem(self,but):
                        mainm.clear_widgets()
                        start_main(mainm,encrypted)
                    def sr(self,btn):
                        gril.clear_widgets()
                        gril.add_widget(MDSpinner(active=True,size_hint=(None,None),size=(96,96)))
                        def sr_int(cvf):
                            con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                            cur=con.cursor()
                            cur.execute("SELECT o,s,k,i FROM sm WHERE k = '"+btn.text+"'")
                            r=cur.fetchall()
                            con.close()
                            if r==[]:
                                a=[]
                            else:
                                with open(str(r[0][0])+".png","wb") as fil:
                                    fil.write(r[0][3])
                                a=[str(r[0][0])+".png",str(r[0][2]),str(r[0][1]),str(r[0][0])]
                            if a==[]:
                                size = (change4,change4)
                                mask = img.new('L', size, 0)
                                draw = ImageDraw.Draw(mask)
                                draw.ellipse((0, 0) + size, fill=255)
                                im = img.open("person-light.png")
                                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                                output.putalpha(mask)
                                im=BytesIO()
                                output.save(im, format='png')
                                im.seek(0)
                                im = CoreImage(BytesIO(im.read()), ext='png')
                                def pres(gg):
                                    pass
                                class ib(ButtonBehavior, Image):
                                    def on_press(self):
                                        pres("a")
                                self.subgrid=GridLayout(rows=1, spacing=0,size_hint_y=None,height=change4,pos_hint={"center_x":0.5,"center_y":0.8})
                                profipic=ib(texture=im.texture, size_hint=(None, None),height=change4,width=change4)
                                name=Button(text="[b][size="+change2+"][color=000000]Not Found[/color][/size][/b]",background_normal="bc.png",background_down="bc.png",background_color=c2,halign='left',text_size=(850,100),markup=True)
                                name.bind(on_press=pres)
                                self.subgrid.add_widget(profipic)
                                self.subgrid.add_widget(name)
                                gril.clear_widgets()
                                gril.add_widget(self.subgrid)
                            else:
                                size = (change4,change4)
                                mask = img.new('L', size, 0)
                                draw = ImageDraw.Draw(mask)
                                draw.ellipse((0, 0) + size, fill=255)
                                im = img.open(a[0])
                                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                                output.putalpha(mask)
                                im=BytesIO()
                                output.save(im, format='png')
                                im.seek(0)
                                im = CoreImage(BytesIO(im.read()), ext='png')
                                def pres(gg):
                                    sp=a[3]
                                    try:
                                        con=sconnect('usordlist.pix')
                                        cur=con.cursor()
                                        cur.execute('CREATE TABLE `'+sp+'`(oi VARCHAR(50), mes VARCHAR(225), ex LONGBLOB, exn VARCHAR(225), tm VARCHAR(50), id VARCHAR(50))')
                                        con.commit()
                                        poi=open('total.pix',mode='r').read()
                                        cur.execute('INSERT INTO uslist(na,points) VALUES (?,?)',(sp,poi))
                                        con.commit()
                                        con.close()
                                        with open('total.pix',mode='w') as fil:
                                            fil.write(str(int(poi)+1))
                                    except:
                                        pass
                                    showch(sp,a[1],a[2],mainm,encrypted)
                                class ib(ButtonBehavior, Image):
                                    def on_press(self):
                                        pres("a")
                                subgrid=GridLayout(rows=1, spacing=0,size_hint_y=None,height=change4,pos_hint={"center_x":0.5,"center_y":0.8})
                                profipic=ib(texture=im.texture, size_hint=(None, None),height=change4,width=change4)
                                name=Button(text="[b][size="+change5+"][color="+c1+"]"+a[1]+"[/size][/b] \n [size=40]~"+a[2]+"[/size][/color]",halign='left',background_normal="bc.png",background_down="bc.png",background_color=c2,text_size=(800,150),markup=True)
                                name.bind(on_press=pres)
                                subgrid.add_widget(profipic)
                                subgrid.add_widget(name)
                                gril.clear_widgets()
                                gril.add_widget(subgrid)
                        Clock.schedule_once(sr_int, 0.3)
                def shbtn(but):
                    if but==bchs:
                        pass
                    else:
                        if self.theme_cls.theme_style=="Light":
                            bchs.background_color=(1,1,1,1)
                        else:
                            bchs.background_color=(0,0,0,1)
                        bchs1.background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058)
                        bchs2.background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058)
                        start_main(mainm, encrypted)
                def shbtn1(but):
                    if but==bchs1:
                        pass
                    else:
                        gril.clear_widgets()
                        bchs.background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058)
                        if self.theme_cls.theme_style=="Light":
                            bchs1.background_color=(1,1,1,1)
                        else:
                            bchs1.background_color=(0,0,0,1)
                        bchs2.background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058)
                        size = (400,400)
                        mask = img.new('L', size, 0)
                        draw = ImageDraw.Draw(mask)
                        draw.ellipse((0, 0) + size, fill=255)
                        con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                        cur=con.cursor()
                        cur.execute("SELECT k,s,h,i FROM sm WHERE o = '"+encrypted+"'")
                        rese=cur.fetchall()
                        with open(encrypted+".png","wb") as fil:
                            fil.write(rese[0][3])
                        im = img.open(encrypted+".png")
                        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                        output.putalpha(mask)
                        im=BytesIO()
                        output.save(im, format='png')
                        im.seek(0)
                        im = CoreImage(BytesIO(im.read()), ext='png')
                        def pushi(selfdf):
                            @run_thread
                            def pus():
                                activity1 = cast('android.app.Activity', PythonActivity.mActivity)
                                @mainthread
                                def on_activity_result(request_code, result_code, intent):
                                    if request_code != RESULT_LOAD_IMAGE:
                                        return
                          
                                    if result_code == Activity.RESULT_CANCELED:
                                        return
                          
                                    if result_code != Activity.RESULT_OK:
                                        raise NotImplementedError('Unknown result_code "{}"'.format(result_code))
                          
                                    selectedImage = intent.getData()
                                    filePathColumn = [MediaStore_Images_Media_DATA]
                                    cursor = activity1.getContentResolver().query(selectedImage,
                                            filePathColumn, None, None, None)
                                    cursor.moveToFirst()
                                    columnIndex = cursor.getColumnIndex(filePathColumn[0])
                                    picturePath = cursor.getString(columnIndex)
                                    cursor.close()
                                    selectedUri = intent.getData()
                                    docStream = activity1.getContentResolver().openInputStream(selectedUri)
                                    gril.remove_widget(impa)
                                    self.np=Button(size_hint=(None,None),background_normal="senpicbg.png",background_down="senpicbg.png",width=int(400/(int(img.open("senpicbg.png").size[1])/100)*(int(img.open("senpicbg.png").size[0])/100)),height=400,border=(0,0,0,0))
                                    gril.add_widget(self.np,index=2)
                        
                                    # I get an int array from the stream
                                    def pca(ad):
                                        def pca_init(d):
                                            nam=ch(picturePath.split("/")[-1])
                                            FileUtils.copyToFile(docStream,io(nam))
                                            im=img.open(nam)
                                            if im.size[0]>1080:
                                                basewidth = 1080
                                                wpercent = (basewidth/float(im.size[1]))
                                                hsize = int((float(im.size[0])*float(wpercent)))
                                                im = im.resize((hsize,basewidth))
                                                im.save(nam)
                                            with open("cp.pix","w") as fil:
                                                fil.write(nam)
                                            gril.remove_widget(self.np)
                                            gril.add_widget(Button(size_hint=(None,None),background_normal=nam,background_down=nam,width=int(400/(int(img.open(nam).size[1])/100)*(int(img.open(nam).size[0])/100)),height=400,border=(0,0,0,0)), index=2)
                                        Clock.schedule_once(pca_init,0.5)
                                    Clock.schedule_once(pca,0.5)
                        
                                act.bind(on_activity_result=on_activity_result)
                        
                                intent= Intent()
                                intent.setAction(Intent.ACTION_PICK)
                                intent.setData(Uri.parse('content://media/internal/images/media'))
                                
                                activity1.startActivityForResult(intent, RESULT_LOAD_IMAGE)
                            pus()
                        def upa(bu):
                            sia.clear_widgets()
                            lo=MDSpinner(active=True,size_hint=(None,None),size=(96,96))
                            sia.add_widget(lo)
                            def upa_e(dfs):
                                con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                                cur=con.cursor()
                                cur.execute("UPDATE sm SET k = '"+ust.text+"' WHERE o = '"+encrypted+"'")
                                con.commit()
                                cur.execute("UPDATE sm SET s = '"+ust1.text+"' WHERE o = '"+encrypted+"'")
                                con.commit()
                                cur.execute("UPDATE sm SET h = '"+ust2.text+"' WHERE o = '"+encrypted+"'")
                                con.commit()
                                sia.clear_widgets()
                                sia.add_widget(bu)
                                bu.icon="content-save-check-outline"
                            Clock.schedule_once(upa_e, 0.5)
                            try:
                                ibi=open(str(open("cp.pix").read()),mode="rb").read()
                                cur.execute("UPDATE sm SET i = %s WHERE o = %s",(ibi,encrypted))
                                con.commit()
                            except:
                                pass
                            con.close()
                        sia=AnchorLayout(anchor_x="right",anchor_y="center",size_hint_y=None,height=115)
                        si=MDIconButton(icon="content-save-outline",md_bg_color=self.theme_cls.primary_color,icon_size="32sp")
                        si.bind(on_press=upa)
                        sia.add_widget(si)
                        impa=AnchorLayout(anchor_x="left",anchor_y="center",size_hint_y=None,height=405)
                        imp=Button(size_hint=(None,None),background_normal=encrypted+".png",background_down=encrypted+".png",width=int(400/(int(img.open(encrypted+".png").size[1])/100)*(int(img.open(encrypted+".png").size[0])/100)),height=400,border=(0,0,0,0))
                        imp.bind(on_press=pushi)
                        impa.add_widget(imp)
                        ust=MDTextField(mode="rectangle",hint_text="Username",text=rese[0][0],size_hint_y=None,height=70)
                        ust1=MDTextField(mode="rectangle",hint_text="Name",text=rese[0][1],size_hint_y=None,height=70)
                        ust2=MDTextField(mode="rectangle",hint_text="Bio",text=rese[0][2],size_hint_y=None,height=70)
                        def s_k2(fas):
                            ust2.focus=True
                        Clock.schedule_once(s_k2)
                        def s_k3(fas):
                            ust1.focus=True
                        Clock.schedule_once(s_k3)
                        def s_k4(fas):
                            ust.focus=True
                        Clock.schedule_once(s_k4)
                        def s_k5(fas):
                            ust.focus=False
                        Clock.schedule_once(s_k5)
                        gril.add_widget(sia)
                        gril.add_widget(ust)
                        gril.add_widget(impa)
                        gril.add_widget(ust1)
                        gril.add_widget(ust2)
                        gril.add_widget(Label(text=" "))
                def shbtn2(colour,indicate):
                    bchs2.background_color=colour
                    try:
                        bchs1.background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058)
                        bchs.background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058)
                    except:
                        pass
                    gril.clear_widgets()
                    dsl=GridLayout(cols=7)
                    if indicate==True:
                        self.darkmodeswitch=Builder.load_string(dark_m_switch)
                    else:
                        self.darkmodeswitch=MDSwitch(icon_active="check",icon_active_color="white",icon_inactive="close",icon_inactive_color="grey")
                    def dsfa(ba,idk):
                        self.cdl(ba)
                    self.darkmodeswitch.bind(active=dsfa)
                    dsl.add_widget(MDLabel(text="Dark Mode  ",size_hint=(None,None),size=(300,200)))
                    dsl.add_widget(Label(text=" "))
                    dsl.add_widget(Label(text=" "))
                    dsl.add_widget(Label(text=" "))
                    dsl.add_widget(Label(text=" "))
                    dsl.add_widget(self.darkmodeswitch)
                    dsl.add_widget(Label(text=" "))
                    gril.add_widget(dsl)
                    gril.add_widget(MDFlatButton(text=" "))
                    gril.add_widget(MDFlatButton(text=" "))
                    repas=MDFlatButton(text="Reset password")
                    def repasf(asf):
                        def repa(sad):
                            op=self.to
                            np=self.tn
                            con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                            cur=con.cursor()
                            cur.execute("SELECT u from sm WHERE o ='"+encrypted+"'")
                            rp=cur.fetchall()[0][0]
                            if str(op.text)==str(rp):
                                cur.execute("UPDATE sm SET u='"+np.text+"' WHERE o ='"+encrypted+"'")
                                con.commit()
                                con.close()
                                rsd.dismiss()
                                def cap(Ds):
                                    rb.dismiss()
                                ca=MDFlatButton(text="OK", text_color=self.theme_cls.primary_color)
                                ca.bind(on_release=cap)
                                rb=MDDialog(text="password changed successfully",buttons=[ca])
                                rb.open()
                            else:
                                rsd.dismiss()
                                def cap(Ds):
                                    rb.dismiss()
                                ca=MDFlatButton(text="OK", text_color=self.theme_cls.primary_color)
                                ca.bind(on_release=cap)
                                rb=MDDialog(text="The old password doesn't match the real one",buttons=[ca])
                                rb.open()
                        rec=MDFlatButton(text="CANCEL", text_color=self.theme_cls.primary_color)
                        reo=MDFlatButton(text="OK", text_color=self.theme_cls.primary_color)
                        rec.bind(on_release=self.reca)
                        reo.bind(on_release=repa)
                        Content=BoxLayout(orientation="vertical",spacing="12dp",size_hint_y=None,height="120dp")
                        self.to=MDTextField(hint_text="Old password",required=True,helper_text_mode="on_error",helper_text="Enter password")
                        self.tn=MDTextField(hint_text="New password",required=True,helper_text_mode="on_error",helper_text="Enter password")
                        Content.add_widget(self.to)
                        Content.add_widget(self.tn)
                        rsd=MDDialog(title="Reset password",type="custom",content_cls=Content,buttons=[rec,reo])
                        self.rsd=rsd
                        rsd.open()
                        
                    repas.bind(on_release=repasf)
                    gril.add_widget(repas)
                sall1=GridLayout(cols=3,size_hint_y=None, height=200)
                sall6=GridLayout(cols=3,size_hint_y=None, height=200)
                sall3=AnchorLayout(anchor_x='left', anchor_y='center')
                bch=Button(background_normal="chat.png",size_hint=(None,None),background_down="chat.png",height=100,width=92,border=(0,0,0,0))
                sall4=AnchorLayout(anchor_x='center', anchor_y='center')
                bch1=Button(background_normal="profile.png",size_hint=(None,None),background_down="profile.png",height=100,width=100,border=(0,0,0,0))
                sall5=AnchorLayout(anchor_x='right', anchor_y='center')
                bch2=MDIconButton(icon="cog-outline",icon_size="40sp")
                sall2=GridLayout(cols=3,size_hint_y=None,spacing=0,height=10)
                sall7=GridLayout(cols=2,size_hint_y=None,spacing=50,height=150)
                with sall6.canvas.before:
                    Color(0.0, 0.5790408525754885, 0.7637655417406749, 0.7140319715808171)
                    sall6.bg_rect = Rectangle(pos=sall6.pos, size=sall6.size)
                    def update_rect(instance, value):
                        instance.bg_rect.pos = instance.pos
                        instance.bg_rect.size = instance.size
                    # listen to size and position changes
                    sall6.bind(pos=update_rect, size=update_rect)
                with sall7.canvas.before:
                    Color(0.0, 0.5790408525754885, 0.7637655417406749, 0.7140319715808171)
                    sall7.bg_rect = Rectangle(pos=sall7.pos, size=sall7.size)
                    def update_rect(instance, value):
                        instance.bg_rect.pos = instance.pos
                        instance.bg_rect.size = instance.size
                    # listen to size and position changes
                    sall7.bind(pos=update_rect, size=update_rect)
                def shbtn2_init(but):
                    colour=(0,0,0,1)
                    indicate=True
                    try:
                        if self.theme_cls.theme_style=="Light":
                            colour=(1,1,1,1)
                            indicate=False
                    except:
                        pass
                    shbtn2(colour,indicate)
                if self.theme_cls.theme_style=="Light":
                    bchs=Button(background_normal="bc.png",background_down="bc.png",background_color=(1,1,1,1))
                    bchs1=Button(background_normal="bc.png",background_down="bc.png",background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058))
                    bchs2=Button(background_normal="bc.png",background_down="bc.png",background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058))
                else:
                    bchs=Button(background_normal="bc.png",background_down="bc.png",background_color=(0,0,0,1))
                    bchs1=Button(background_normal="bc.png",background_down="bc.png",background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058))
                    bchs2=Button(background_normal="bc.png",background_down="bc.png",background_color=(0.0, 0.6571936056838366, 0.8241563055062167, 0.8235294117647058))
                bch.bind(on_press=shbtn)
                bch1.bind(on_press=shbtn1)
                bch2.bind(on_press=shbtn2_init)
                sall8=AnchorLayout(anchor_x="right",anchor_y="center")
                # if self.theme_cls.theme_style=="Light":
                bu= MDFloatingActionButton(icon="magnify",type="standard",icon_size="32sp")
                def b(but):
                    print("1")
                    self.but=but
                    bu.on_press(but)
                bu.bind(on_press=b)
                ml=MDLabel(text="[size=60][b][color="+c1+"]"+cp_("čĦĵĢĩ")+"[/color][/size][/b]",theme_text_color="Secondary",markup=True,padding_y=30)
                sall8.add_widget(bu)
                sall7.add_widget(ml)
                sall7.add_widget(sall8)
                sall3.add_widget(bch)
                sall1.add_widget(sall3)
                sall4.add_widget(bch1)
                sall1.add_widget(sall4)
                sall5.add_widget(bch2)
                sall1.add_widget(sall5)
                sall2.add_widget(bchs)
                sall2.add_widget(bchs1)
                sall2.add_widget(bchs2)
                sall6.add_widget(Label(text=" ",size_hint=(None,None),width=100))
                sall6.add_widget(sall1)
                sall6.add_widget(Label(text=" ",size_hint=(None,None),width=100))
                allg.add_widget(sall7)
                allg.add_widget(sall6)
                allg.add_widget(sall2)
                allg.add_widget(scl)
                mainm.add_widget(w)
                try:
                    pinfo=Context.getPackageManager().getPackageInfo(Context.getPackageName(), 0)
                    version = pinfo.versionName
                    c=pymysql.connect(host="de1.centronodes.com",user="u7943_pI3wjctdXk",password="^e2qB.xeDUrk4wQZ=vh^IG8U",database="s7943_001")
                    cu=c.cursor()
                    cu.execute("SELECT * FROM sm")
                    c.close()
                    if float(cu.fetchall()[0][0])>float(version):
                        def remo(sad):
                            upd.dismiss()
                        bac=MDFlatButton(text="MAYBE LATER", text_color=self.theme_cls.primary_color)
                        bac.bind(on_release=remo)
                        updl=MDFlatButton(text="UPDATE", text_color=self.theme_cls.primary_color)
                        def openpl(hgu):
                            uopen("https://app.pixelteams.tk/update")
                        updl.bind(on_release=openpl)
                        upd=MDDialog(title="New update is available",buttons=[bac,updl])
                        upd.open()
                except:
                    pass
                try:
                    open("tot.pix").read()
                except:
                    with open("tot.pix","w") as fil:
                        fil.write("t1")
                    
            
            
            
            
            
            
            #           =======  =========     =      ====    =========
            #           =            =        = =     =   =       =
            # ========  =====        =       =   =    ====        =     ========
            #               =        =      =======   =   =       =
            #          ======        =     =       =  =    =      =
               
            
            
            
            
            
            
                                
            def logincf(m,a,b,e,ani,abtn,mainr=None):
                    conc=9
                    try:
                        con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                        conc=0
                    except:
                        m.clear_widgets()
                        m.add_widget(Label(text="[size=50]Check your internet[/size]",markup=True, pos=(230,250)))
                        Clock.schedule_once(exit_app, 1)
                    if conc==0:
                        cor=con.cursor()
                        cheklg=0
                        try:
                            cor.execute("SELECT u FROM sm WHERE o = '"+a+"'")
                            resl=cor.fetchall()
                            resl=resl[0][0]
                            if resl==b:
                                con.close()
                                with open(".1.pix",mode="w") as fil:
                                    fil.write(cp(a)+"@pix@"+cp(b))
                                cheklg=1
                            else:
                                con.close()
                                mainr.remove_widget(ani)
                                mainr.add_widget(abtn)
                                e.text="[size=30][color=ff0000]Incorrect password or email[/color][/size]"
                                return True
                        except:
                            mainr.remove_widget(ani)
                            mainr.add_widget(abtn)
                            e.text="[size=30][color=ff0000]Incorrect password or email[/color][/size]"
                            return True
                        if cheklg==1:
                          start_main(m,a,ani,abtn)
                       
                       
            
            def loginc(em,cr,main,e,ani,abtn,mainr):
                bem=em
                bcr=cr
                em=em.text
                cr=cr.text
                if research("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu|net]{3}$)", em):
                    tcr=cr.replace(" ",'a')
                    if tcr==cr:
                        if len(cr)>7:
                            logincf(main, em,cr,e,ani,abtn,mainr)
                        else:
                            bcr.text=""
                            e.text="""[size=30][color=ff0000]Password must be more than 7[/size][/color]"""
                            mainr.remove_widget(ani)
                            mainr.add_widget(abtn)
                    else:
                        bcr.text=""
                        e.text="""[size=30][color=ff0000]Password has white spaces[/size][/color]"""
                        mainr.remove_widget(ani)
                        mainr.add_widget(abtn)
                else:
                    tcr=cr.replace(" ",'a')
                    if tcr==cr:
                        if len(cr)>7:
                            tem=em.replace(".","a")
                            tem=tem.replace("_","c")
                            if tem.isalnum():
                                try:
                                    con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                                    cor=con.cursor()
                                    tempch=9
                                except:
                                    mainr.remove_widget(ani)
                                    mainr.add_widget(abtn)
                                    tempch=0
                                    main.clear_widgets()
                                    main.add_widget(Label(text="[size=50]Check your internet[/size]",markup=True, pos=(230,250)))
                                    Clock.schedule_once(exit_app, 1)
                                if tempch==9:
                                    try:
                                        cor.execute("SELECT o FROM sm WHERE k = '"+em+"'")
                                        em=cor.fetchall()[0][0]
                                        a=logincf(main, em, cr, e, ani, abtn)
                                        if a:
                                            con.close()
                                            e.text="[size=30][color=ff0000]Incorrect password or Username[/color][/size]"
                                            mainr.remove_widget(ani)
                                            mainr.add_widget(abtn)
                                    except:
                                        e.text="[size=30][color=ff0000]Incorrect password or username[/color][/size]"
                                        mainr.remove_widget(ani)
                                        mainr.add_widget(abtn)
                            else:
                                bem.text=""
                                e.text="[size=30]Invalid Username[/size]"
                                mainr.remove_widget(ani)
                                mainr.add_widget(abtn)
                        else:
                            bcr.text=""
                            e.text="""[size=30][color=ff0000]Password must be more than 7[/size][/color]"""
                            mainr.remove_widget(ani)
                            mainr.add_widget(abtn)
                    else:
                        bcr.text=""
                        e.text="""[size=30][color=ff0000]Password has white spaces[/size][/color]"""
                        mainr.remove_widget(ani)
                        mainr.add_widget(abtn)
            
            
            
            
            
            def initing_cr(a,b,c,d,e,f,g,h,i,smai,signu,lgna):
                tc=c.replace(".","a")
                tc=tc.replace("_","c")
                tc=tc.replace(" ","$")
                chal=0
                if c=="":
                    smai.remove_widget(i)
                    neb= MDFillRoundFlatButton(text="Create",md_bg_color=self.theme_cls.bg_darkest,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                    def nbp(zsd):
                        signu(b,lgna)
                    neb.bind(on_release=nbp)
                    smai.add_widget(neb)
                    h.text='[size=30]All fields are mandatory[/size]'
                elif d=="":
                    smai.remove_widget(i)
                    neb= MDFillRoundFlatButton(text="Create",md_bg_color=self.theme_cls.bg_darkest,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                    def nbp(zsd):
                        signu(b,lgna)
                    neb.bind(on_release=nbp)
                    smai.add_widget(neb)
                    h.text='[size=30]All fields are mandatory[/size]'
                elif f=="":
                    h.text='[size=30]All fields are mandatory[/size]'
                    smai.remove_widget(i)
                    neb= MDFillRoundFlatButton(text="Create",md_bg_color=self.theme_cls.bg_darkest,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                    def nbp(zsd):
                        signu(b,lgna)
                    neb.bind(on_release=nbp)
                    smai.add_widget(neb)
                elif g=="":
                    h.text='[size=30]All fields are mandatory[/size]'
                    smai.remove_widget(i)
                    neb= MDFillRoundFlatButton(text="Create",md_bg_color=self.theme_cls.bg_darkest,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                    def nbp(zsd):
                        signu(b,lgna)
                    neb.bind(on_release=nbp)
                    smai.add_widget(neb)
                elif not tc.isalnum():
                    h.text='[color=ff0000][size=30]Username contains only number, alphabets, (.), (_)[/size][/color]'
                    smai.remove_widget(i)
                    neb= MDFillRoundFlatButton(text="Create",md_bg_color=self.theme_cls.bg_darkest,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                    def nbp(zsd):
                        signu(b,lgna)
                    neb.bind(on_release=nbp)
                    smai.add_widget(neb)
                elif f.replace(' ', 'a')!=f and len(f)<8 and chal!=5:
                    h.text='[color=ff0000][size=30]Password does not contain white spases and more than 7 characters[/size][/color]'
                    smai.remove_widget(i)
                    neb= MDFillRoundFlatButton(text="Create",md_bg_color=self.theme_cls.bg_darkest,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                    def nbp(zsd):
                        signu(b,lgna)
                    neb.bind(on_release=nbp)
                    smai.add_widget(neb)
                else:
                    tc=0
                    try:
                        con=pymysql.connect(user="pixusers",password="pix123",database="app",host="13.202.85.45")
                    except Exception as e:
                        print(e)
                        tc=1
                        a.clear_widgets()
                        a.add_widget(Label(text="[size=50]Check your internet[/size]",markup=True, pos=(230,250)))
                        Clock.schedule_once(exit_app, 1)
                        tc=1
                    if tc==0:
                        try:
                            cur = con.cursor()
                            cur.execute('INSERT INTO sm(k,o,u,s,h,i) VALUES (%s,%s,%s,%s,%s,%s)',(c,b,f,d,e,open(g,mode='rb').read()))
                            cur.execute('CREATE TABLE `'+b+'`(na VARCHAR(50), oi VARCHAR(50), message VARCHAR(225), ex LONGBLOB, exn VARCHAR(225),tm VARCHAR(50), id VARCHAR(50))')
                            con.commit()
                            con.close()
                            start_main(a,b)
                        except Exception as e:
                            print(e)
                            con.close()
                            h.text='[size=40]Email or username already exist[/size]'
                            c=''
                            b=''
                            smai.remove_widget(i)
                            neb= MDFillRoundFlatButton(text="Create",md_bg_color=self.theme_cls.bg_darkest,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                            def nbp(zsd):
                                signu(b,lgna)
                            neb.bind(on_release=nbp)
                            smai.add_widget(neb)
            #=====================register==================
            try:
                self.theme_cls.theme_style=cp_(open("mode.dl",mode="r").read())
            except:
                with open("mode.dl",mode="w") as fil:
                    fil.write("ĉĦĤĥı")
                self.theme_cls.theme_style=cp_("ĉĦĤĥı")
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
            service = AndroidService('pixel service', 'running')
            service.start('service started')
            self.service = service
            mainm=Screen()
            main = FloatLayout()
            try:
                g=open(".1.pix", mode="r").read()
                g=g.split("@pix@")
                try:
                    logincf(mainm, cp_(g[0]), cp_(g[1]), None,None,None)
                except:
                    removefil(".1.pix")
                    quit()
            except:
                wel=MDLabel(text="[size="+change1+"]L o g i n[/size]", markup=True, pos_hint={"center_x":0.85,"center_y":0.9})
                emt = MDTextField(mode="rectangle",hint_text="Username",size_hint=(change3,0.03),keyboard_suggestions=True, pos_hint={"center_x":0.5,"center_y":0.75}, multiline=False)
                sp=MDIconButton(icon="eye-outline",size_hint=(None,None),size=(50,50),pos_hint={"center_x":0.93,"center_y":0.59})
                sp.bind(on_press=self.dsp)
                self.pat = MDTextField(mode="rectangle",size_hint=(change3,0.03), hint_text="password",password=True, pos_hint={"center_x":0.5,"center_y":0.6}, multiline=False)
                su = MDFlatButton(text="Don't have an account Sign up here", text_color=(0.7843137254901961, 0.7843137254901961, 0.0, 1), pos_hint={"center_x":0.5, "center_y":0.1})
                @mainthread
                def signu(emil,logna=""):
                    mainm.clear_widgets()
                    smain = FloatLayout()
                    with smain.canvas.before:
                        Color(self.theme_cls.bg_light[0],self.theme_cls.bg_light[1],self.theme_cls.bg_light[2],self.theme_cls.bg_light[3])
                        smain.rect = RoundedRectangle(
                            pos=smain.pos,
                            size=smain.size,
                            radius=[(40, 40), (40, 40), (20, 20), (20, 20)],
                        )
                    smain.bind(pos=lambda obj, pos: setattr(smain.rect, "pos", pos))
                    smain.bind(size=lambda obj, size: setattr(smain.rect, "size", size))
                    smain.size_hint = (None, None)
                    smain.size = (Window.width-200, Window.height-300)
                    smain.pos_hint = {"center_x": 0.5, "center_y": 0.5}
                    smain.background_color = 0.26, 0.26, 0.26, 0.2
                    mainm.add_widget(smain)
                    propicri=randint(0,1)
                    if propicri==1:
                        with open("tempic.path","w") as fil:
                            fil.write("person-light.png")
                        size = (200, 200)
                        mask = img.new('L', size, 0)
                        draw = ImageDraw.Draw(mask) 
                        draw.ellipse((0, 0) + size, fill=255)
                        im = img.open("person-light.png")
                        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                        output.putalpha(mask)
                        nim=BytesIO()
                        output.save(nim, format='png')
                        nim.seek(0)
                        im = CoreImage(BytesIO(nim.read()), ext='png')
                    else:
                        with open("tempic.path","w") as fil:
                            fil.write("person-dark.png")
                        size = (200, 200)
                        mask = img.new('L', size, 0)
                        draw = ImageDraw.Draw(mask) 
                        draw.ellipse((0, 0) + size, fill=255)
                        im = img.open("person-dark.png")
                        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                        output.putalpha(mask)
                        nim=BytesIO()
                        output.save(nim, format='png')
                        nim.seek(0)
                        im = CoreImage(BytesIO(nim.read()), ext='png')
                    selectpic=MDLabel(text="[color=ffffff][size=45]Profile settings[/size][/color]",markup=True, pos_hint={"center_x":0.85,"center_y":0.9})
                    nat = MDTextField(mode="rectangle",size_hint=(0.6,0.03), pos_hint={"center_x":0.5,"center_y":0.7}, multiline=False,hint_text="Username")
                    nnt = MDTextField(mode="rectangle",text=logna,size_hint=(0.6,0.03), pos_hint={"center_x":0.5,"center_y":0.6}, multiline=False,hint_text="Name")
                    self.crti = MDTextField(mode="rectangle",size_hint=(0.6,0.03), pos_hint={"center_x":0.5,"center_y":0.5}, multiline=False, hint_text="Password",password=True)
                    tempb=Button(text="g", pos=(10000, 10000))
                    sp=Button(background_normal="show.png",background_down="show.png",size_hint=(None,None),border=(0,0,0,0),size=(50,50),pos_hint={"center_x":0.93,"center_y":0.5})
                    sp.bind(on_press=self.dsp2)
                    cbtn = MDFillRoundFlatButton(text="Create",md_bg_color=self.theme_cls.bg_darkest,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                    e=MDLabel(text=" ",markup=True, pos_hint={"center_x":0.7,"center_y":0.01})
                    def init_start_main(df):
                        a=MDSpinner(active=True,pos_hint={"center_x":0.5,"center_y":0.15}, size_hint=(0.25, 0.07))
                        smain.remove_widget(cbtn)
                        smain.add_widget(a)
                        def temp3(vgvg):
                            initing_cr(mainm,emil,nat.text,nnt.text,"",self.crti.text,str(open("tempic.path","r").read()),e,a,smain,signu,logna)
                        Clock.schedule_once(temp3, 1)
                    cbtn.bind(on_press=init_start_main)
                    smain.add_widget(selectpic)
                    smain.add_widget(tempb)
                    smain.add_widget(self.crti)
                    smain.add_widget(cbtn)
                    smain.add_widget(nat)
                    smain.add_widget(e)
                    smain.add_widget(nnt)
                    smain.add_widget(sp)
                    def s_k(fas):
                        nnt.focus=True
                    Clock.schedule_once(s_k)
                    def s_k1(fas):
                        nat.focus=True
                    Clock.schedule_once(s_k1)
                etm=Label(text=" ",markup=True, pos_hint={"center_x":0.5, "center_y":0.53})
                def glogin_init(af):
                    login_google()
                su.bind(on_release=glogin_init)
                @mainthread
                def closedialog(a):
                    self.dialog.dismiss()
                @mainthread
                def er():
                    c=MDFlatButton(text="Close")
                    c.bind(on_release=closedialog)
                    self.dialog = MDDialog(text="Error while signing using GOOGLE",buttons=[c])
                    self.dialog.open()
                def gln(ema,na, ur):
                    signu(na,logna=ema)
                initialize_google(gln,er,"379080696429-v9m7749if6n3a62ms5uemrmk9equm5cp.apps.googleusercontent.com")
                lbtn = MDFillRoundFlatButton(text="Continue",pos_hint={"center_x":0.5, "center_y":0.3}, size_hint=(0.3,0.08),md_bg_color=self.theme_cls.bg_darkest)
                def _loginc(du):
                    main.remove_widget(lbtn)
                    a=MDSpinner(active=True,pos_hint={"center_x":0.5, "center_y":0.3}, size_hint=(0.3,0.08))
                    main.add_widget(a)
                    def temp3(vgvg):
                        loginc(emt,self.pat,mainm,etm,a,lbtn,main)
                    Clock.schedule_once(temp3, 1)
                lbtn.bind(on_press=_loginc)
                with main.canvas.before:
                    Color(self.theme_cls.bg_light[0],self.theme_cls.bg_light[1],self.theme_cls.bg_light[2],self.theme_cls.bg_light[3])
                    main.rect = RoundedRectangle(
                        pos=main.pos,
                        size=main.size,
                        radius=[(40, 40), (40, 40), (20, 20), (20, 20)],
                    )
                main.bind(pos=lambda obj, pos: setattr(main.rect, "pos", pos))
                main.bind(size=lambda obj, size: setattr(main.rect, "size", size))
                main.size_hint = (None, None)
                main.size = (Window.width-200,Window.height-500)
                main.pos_hint = {"center_x": 0.5, "center_y": 0.53}
                main.background_color = 0.26, 0.26, 0.26, 0.2
                main.add_widget(wel)
                main.add_widget(emt)
                main.add_widget(etm)
                main.add_widget(self.pat)
                mainm.add_widget(su)
                main.add_widget(sp)
                main.add_widget(lbtn)
                mainm.add_widget(main)
        except Exception as e:
            c=pymysql.connect(host="de1.centronodes.com",user="u7943_pI3wjctdXk",password="^e2qB.xeDUrk4wQZ=vh^IG8U",database="s7943_001")
            cu=c.cursor()
            cu.execute("INSERT INTO er(err) VALUES ('"+str(e)+"')")
            c.commit()
            c.close()
        return mainm
    def cdl(self,but):
        def cdl_init(zs):
            if but.active:
                with open("mode.dl",mode="w") as fil:
                    fil.write("āĞįĨ")
            else:
                with open("mode.dl",mode="w") as fil:
                    fil.write("ĉĦĤĥı")
            rb=MDFlatButton(text="Restart", text_color=self.theme_cls.primary_color)
            def resap(s):
                quit()
            rb.bind(on_press=resap)
            self.dialog = MDDialog(text="You must restart the app for this to take effect.",buttons=[rb])
            self.dialog.open()
        Clock.schedule_once(cdl_init, 0.5)
    def bcaf(self,but):
        self.cond.dismiss()
    def reca(self,but):
        self.rsd.dismiss()
    def dsp(self,but):
        if but.icon=="eye-outline":
            self.pat.password=False
            but.icon="eye-off-outline"
        else:
            self.pat.password=True
            but.icon="eye-outline"
    def dsp2(self,but):
        if but.icon=="eye-outline":
            self.crti.password=False
            but.icon="eye-off-outline"
        else:
            self.crti.password=True
            but.icon="eye-outline"
myApp().run()
