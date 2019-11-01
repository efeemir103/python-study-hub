import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import Data, Database

class ActivityEditorWindow(Screen):
    def __init__(self, item = None):
        self.desc = ObjectProperty(None)
        self.date = ObjectProperty(None)
        self.priority = ObjectProperty(None)
        if item is None:
            self.desc.text = ""
            self.date.text = ""
            self.priority.text = ""
        else:
            self.desc.text = item.desc
            self.dater.text = item.date
            self.priority.text = item.priority
    
    def submit(self):
        db.addItem(Data(self.desc.text, self.date.text, self.priority.text))


class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
sm = WindowManager()
db = Database("activities.csv")
screens = [ActivityEditorWindow(name = "edit"), MainWindow(name = "main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()