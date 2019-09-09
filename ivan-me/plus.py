from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics','resizable', 0)
Config.set('graphics','width', 400)
Config.set('graphics','height', 500)

class CalculatorApp(App):
    def update_label(self):
        self.label.text=self.formula
    def add_number(self, instance):
        if self.formula=='0':
            self.formula=""
        self.formula+=str(instance.text)
        self.update_label()
    def add_operation(self, instance):
        # if self(instance, text)=="x":
        #     self.formula+="+"
        # else:
        self.formula+=str(instance.text)
        self.update_label()
    def clear(self, instance):
        self.label.text="0"
        self.formula='0'
    def add_ostatok(self, instance):
        self.label.text = self.label.text[:-1]
        self.formula='0'
    def culc_result(self, insance):
        self.label.text=str(eval(self.label.text))
        self.formula='0'
    def build(self):
        self.formula='0'
        boxlayout=BoxLayout(orientation='vertical', padding=25, spacing=3)
        gridlayout=GridLayout(cols=4, spacing=3, size_hint=(1,.6))
        self.label=Label(text='0', font_size=40, halign='right', valign='center', size_hint=(1,.3))
        self.label.bind(size=self.label.setter('text_size'))
        boxlayout.add_widget(self.label)
        gridlayout.add_widget(Button(text='1',on_press=self.add_number))
        gridlayout.add_widget(Button(text='2',on_press=self.add_number))
        gridlayout.add_widget(Button(text='3',on_press=self.add_number))
        gridlayout.add_widget(Button(text='/',on_press=self.add_operation))
        gridlayout.add_widget(Button(text='4',on_press=self.add_number))
        gridlayout.add_widget(Button(text='5',on_press=self.add_number))
        gridlayout.add_widget(Button(text='6',on_press=self.add_number))
        gridlayout.add_widget(Button(text='*',on_press=self.add_operation))
        gridlayout.add_widget(Button(text='7',on_press=self.add_number))
        gridlayout.add_widget(Button(text='8',on_press=self.add_number))
        gridlayout.add_widget(Button(text='9',on_press=self.add_number))
        gridlayout.add_widget(Button(text='0',on_press=self.add_number))
        gridlayout.add_widget(Button(text='+',on_press=self.add_operation))
        gridlayout.add_widget(Button(text='-',on_press=self.add_operation))
        gridlayout.add_widget(Button(text='**',on_press=self.add_operation))
        gridlayout.add_widget(Button(text='//',on_press=self.add_operation))
        gridlayout.add_widget(Button(text='<-',on_press=self.add_ostatok))
        gridlayout.add_widget(Button(text='C',on_press=self.clear))
        gridlayout.add_widget(Button(text='(',on_press=self.add_number))
        gridlayout.add_widget(Button(text=')',on_press=self.add_number))
        boxlayout.add_widget(gridlayout)
        boxlayout.add_widget(Button(text='=',on_press=self.culc_result, size_hint=(1, .1)))
        #self.formula='0'
        #boxlayout=BoxLayout(orientation='vertical', padding=25)
        #gridlayout=GridLayout(cols=4, spacing=3, size_hint=(1,.3))
        #self.label=Label(text='0', font_size=40, halign='right', valign='center', size_hint=(1,.3))
        #self.label.bind(size=self.label.setter('text_size'))
        #boxlayout.add_widget(self.label)   
        #gridlayout.add_widget(Button(text='=',on_press=self.culc_result)) "    
        return boxlayout
if __name__=="__main__":
    CalculatorApp().run()