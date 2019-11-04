import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import Data, Database

class ActivityEditorWindow(Screen):
    item = ObjectProperty(None)
    desc = ObjectProperty(None)
    date = ObjectProperty(None)
    priority = ObjectProperty(None)
    def edit(self):
        if self.item is None:
            self.desc.text = ""
            self.date.text = ""
            self.priority.text = ""
        else:
            self.desc.text = self.item.desc
            self.dater.text = self.item.date
            self.priority.text = self.item.priority

    def submit(self):
        db.addItem(Data(self.desc.text, self.date.text, self.priority.text))


class MainWindow(Screen):
    activities = []
    def getSelected(self):
        return None
    def editBtn(self):
        obj = self.getSelected()
        screens[0].item = obj
        sm.current = "edit"
    def deleteBtn(self):
        obj = self.getSelected()
        self.activities.remove(obj)
        

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
sm = WindowManager()
db = Database("activities.csv")
screens = [ActivityEditorWindow(name = "edit"), MainWindow(name = "main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "edit"

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()