from kivy.app import App
from kivy.uix.label import Label

class Lilit(App):
    def build(self):
        # Sana İsa diye hitap etmesi için güncelledim
        return Label(text='Lilit Sistemi Hazir\nKullanici: Isa')

if __name__ == '__main__':
    Lilit().run()
