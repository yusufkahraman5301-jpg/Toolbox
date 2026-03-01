from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class TroyZx(App):
    def build(self):
        # Arka plan simsiyah, asalet olsun
        Window.clearcolor = (0, 0, 0, 1)
        return Label(
            text='TroyZx',
            font_size='100sp',
            bold=True,
            color=(1, 1, 1, 1) # Beyaz yazı
        )

if __name__ == '__main__':
    TroyZx().run()
