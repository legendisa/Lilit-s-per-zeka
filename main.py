from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LilitSingularity(App):
    def build(self):
        self.title = "LILIT v2.0 - SINGULARITY"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Başlık ve Durum
        self.status = Label(text="[SINGULARITY MODE ACTIVE]", font_size='24sp', color=(0, 1, 0, 1))
        layout.add_widget(self.status)
        
        # Komut Girişi
        self.input = TextInput(hint_text="Komutunuzu buraya yazın...", multiline=False, size_hint=(1, 0.2))
        self.input.bind(on_text_validate=self.komut_isle)
        layout.add_widget(self.input)
        
        return layout

    def komut_isle(self, instance):
        komut = self.input.text.lower()
        if "lilit" in komut:
            self.status.text = "İşlem Başlatıldı..."
            # Buraya arka plan görevleri gelecek
        self.input.text = ""

if __name__ == "__main__":
    LilitSingularity().run()
