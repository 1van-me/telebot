from kivy.app import App
from kivy.uix.button import Button
class TestApp(App):
    def cn(self, instance):
        self.count+=1
        self.but.text=str(self.count)

    def build(self):
        backgraund_color=[1,0,0,1]
        self.count=0
        self.but=Button(text="press to start", font_size=40, on_press=self.cn)
        return self.but


if __name__=="__main__":
    TestApp().run()