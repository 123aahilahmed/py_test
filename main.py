from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDToolbar

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Toolbar
        toolbar = MDToolbar(title="Welcome App")
        toolbar.pos_hint = {"top": 1}
        
        # Welcome Label
        self.welcome_label = MDLabel(
            text="Welcome to my Advanced Python App",
            halign="center",
            theme_text_color="Primary",
            font_style="H4",
            size_hint=(0.8, None),
            height=100,
            pos_hint={"center_x": 0.5, "top": 0.8}
        )
        
        # Label for user input
        input_label = Label(
            text="Enter your name:",
            halign="center",
            font_size=24,
            size_hint=(0.8, None),
            height=100,
            pos_hint={"center_x": 0.5, "top": 0.6}
        )
        
        # Input field
        self.input_field = TextInput(
            hint_text="Enter your name",
            size_hint=(0.6, None),
            pos_hint={"center_x": 0.5, "top": 0.5}
        )
        
        # Button to perform an action
        button = MDRaisedButton(
            text="Submit",
            size_hint=(0.3, None),
            pos_hint={"center_x": 0.5, "top": 0.4}
        )
        button.bind(on_release=self.on_button_click)
        
        # Add widgets to the layout
        self.add_widget(toolbar)
        self.add_widget(self.welcome_label)
        self.add_widget(input_label)
        self.add_widget(self.input_field)
        self.add_widget(button)
        
    def on_button_click(self, *args):
        # Perform an action (e.g., greet the user)
        name = self.input_field.text.strip()
        if name:
            self.welcome_label.text = f"Thank you, {name}! See you soon!"
            Clock.schedule_once(self.close_app, 5)  # Close the app after 5 seconds
        
    def close_app(self, dt):
        MDApp.get_running_app().stop()

class MainApp(MDApp):
    def build(self):
        # Main Screen
        main_screen = MainScreen()
        
        return main_screen

if __name__ == '__main__':
    MainApp().run()
