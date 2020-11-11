from kivy.app import App
from .view import MainWindow

class MainApp(App):
    def build(self):
        print('In the __init__.py File')
        return MainWindow()
    
