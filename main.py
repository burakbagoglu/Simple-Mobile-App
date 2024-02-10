from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import sqlite3 as sql
import hashlib

vt = sql.connect("db.sql")
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS users ('username','password')")

def Sifreleme(sifre):
    sha256 = hashlib.sha256()
    sha256.update(sifre.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password

class Giris(Screen):
    def __init__(self, **kwargs):
        super(Giris, self).__init__(**kwargs)
        layout = FloatLayout()
        main_frame = Image(source='img/main_frame.png', allow_stretch=True, keep_ratio=False, pos=(0, 0)) 

        label = Label(text='HOŞ GELDİNİZ!', font_size=40, pos=(0, 120),font_name='LEMONMILK-Regular.otf')
        label.color = (0,0,0,1)
        
        logo = Image(source="img/logo.png",pos=(0,270))
        username_input = TextInput(hint_text='Kullanıcı adı',
                                   multiline=False,
                                   size_hint=(None, None),
                                   size=(200, 40),
                                   pos=(150, 400),
                                   background_color=(255,255,255,1))

        password_input = TextInput(hint_text='Şifre',
                                   multiline=False,
                                   size_hint=(None, None),
                                   size=(200, 40),
                                   pos=(150, 350),
                                   background_color=(255,255,255,1),
                                   password=True)


        button = Button(text='GİRİŞ', font_name='LEMONMILK-Regular.otf',
                        size_hint=(None, None),
                        size=(200, 50),
                        pos=(150,300),
                        background_color=(255,255,255,1),
                        border=(0, 0, 0, 4)
                        )
        
        button.color = (0,0,0,1)
        

        label_hesabin_yokmu= Button(text="Hesabın yok mu?",size_hint=(None, None),background_color=(255,255,255,1),
                        border=(0, 0, 0, 10),pos=(150,240),size=(200, 50),on_press=self.KayitEkranDegistir)
        
        label_hesabin_yokmu.color = (0,0,0,1)
        
        layout.add_widget(main_frame)
        layout.add_widget(username_input)
        layout.add_widget(password_input)
        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(logo)
        layout.add_widget(label_hesabin_yokmu)
        self.add_widget(layout)

    def KayitEkranDegistir(self,instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'kayit'

class Kayit(Screen):
    def __init__(self, **kwargs):
        super(Kayit, self).__init__(**kwargs)
        layout = FloatLayout()
        main_frame = Image(source='img/main_frame.png', allow_stretch=True, keep_ratio=False, pos=(0, 0)) 

        label = Label(text='HOŞ GELDİNİZ!', font_size=40, pos=(0, 120),font_name='LEMONMILK-Regular.otf')
        label.color = (0,0,0,1)
        
        logo = Image(source="img/logo.png",pos=(0,270))
        username_input = TextInput(hint_text='Kullanıcı adı',
                                   multiline=False,
                                   size_hint=(None, None),
                                   size=(200, 40),
                                   pos=(150, 400),
                                   background_color=(255,255,255,1))

        password_input = TextInput(hint_text='Şifre',
                                   multiline=False,
                                   size_hint=(None, None),
                                   size=(200, 40),
                                   pos=(150, 350),
                                   background_color=(255,255,255,1),
                                   password=True)


        button = Button(text='KAYIT OL', font_name='LEMONMILK-Regular.otf',
                        size_hint=(None, None),
                        size=(200, 50),
                        pos=(150,300),
                        background_color=(255,255,255,1),
                        border=(0, 0, 0, 4)
                        )
        
        button.color = (0,0,0,1)
        

        label_hesabin_yokmu= Button(text="Zaten hesabın var mı?",size_hint=(None, None),background_color=(255,255,255,1),
                        border=(0, 0, 0, 10),pos=(150,240),size=(200, 50),on_press=self.KayitEkranDegistir)
        
        label_hesabin_yokmu.color = (0,0,0,1)
        
        layout.add_widget(main_frame)
        layout.add_widget(username_input)
        layout.add_widget(password_input)
        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(logo)
        layout.add_widget(label_hesabin_yokmu)
        self.add_widget(layout)

    def KayitEkranDegistir(self,instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'giris'
        

class MyApp(App):
    def build(self):
        # Ekran boyutunu belirleme
        Window.clearcolor = (255, 255, 255, 1)
        Window.size = (412, 600)

       
        screen_manager = ScreenManager()

        first_screen = Giris(name='giris')
        screen_manager.add_widget(first_screen)


        second_screen = Kayit(name='kayit')
        screen_manager.add_widget(second_screen)

        return screen_manager
if __name__ == '__main__':
    MyApp().run()
