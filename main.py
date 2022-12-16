from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
from kivy.utils import platform

if platform not in ["android", "ios"]:
    Window.size = (1080, 2400)

class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Fahrenheit to Celsius"
            self.input.hint_text = "Enter temperature in Fahrenheit"
            self.converted.text = ""
            self.label.text = ""
        else:
            self.state = 0
            self.toolbar.title = "Celsius to Fahrenheit"
            self.input.hint_text = "Enter temperature in Celsius"
            self.converted.text = ""
            self.label.text = ""

    def convert(self, args):
        if self.state == 0:
            try:
                val = (float(self.input.text) * 1.8) + 32
                self.converted.text = str(val)
                self.label.text = 'The temperature in Fahrenheit is:'
            except ValueError:
                self.label.text = 'Invalid input'
        else:
            try:
                val = (float(self.input.text) - 32) / 1.8
                self.converted.text = str(val)
                self.label.text = 'The temperature in Celsius is:'
            except ValueError:
                self.label.text = 'Invalid input'

    def build(self):
        self.icon = 'assets/temperature_13519.png'
        self.state = 0
        self.theme_cls.primary_palette = "BlueGray"
        screen = MDScreen()

        #Background
        screen.add_widget(Image(
            source="assets/background.jpg",
            allow_stretch = True,
            keep_ratio = False,
        ))

        # Logos
        screen.add_widget(Image(
            source="temperature-icon-png-19.png",
            pos_hint = {"center_x": 0.5, "center_y": 0.7},
            size = (20, 40),
            opacity = 0.5
        ))

        #top toolbar
        self.toolbar = MDTopAppBar(title="Celsius to Fahrenheit")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        # Collect User Input
        self.input = MDTextField(
            hint_text = "Enter temperature in Celsius",
            halign = "center",
            size_hint = (0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size = 40
        )
        screen.add_widget(self.input)

        # label widgets

        self.label = MDLabel(
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # Convert button
        screen.add_widget(MDFillRoundFlatButton(
            text = "CONVERT",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y": 0.15},
            on_press = self.convert
        ))

        return screen


ca = ConverterApp()
if __name__ == '__main__':
    ca.run()


