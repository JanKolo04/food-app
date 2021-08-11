from kivy.app import App
from kivy.uix.button import Button
import main as fille

class Test(App):
    def build(self):
        btn = Button(text ="Push Me !",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(600, 550))

        btn.bind(on_press = self.callback)
        return btn

    def callback(self, event):
        fille.main()

Test().run()

