from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class TroyZxApp(App):
    def build(self):
        # Arka planı siyah yapalım
        Window.clearcolor = (0, 0, 0, 1)
        
        layout = FloatLayout()
        
        # Ekranın tam ortasına TroyZx yazısı
        label = Label(
            text='TroyZx',
            font_size='80sp',
            bold=True,
            color=(1, 0, 0, 1), # Kırmızı renk (havalı dursun)
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    TroyZxApp().run()
