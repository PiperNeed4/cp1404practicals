from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def build(self):
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["John", "Samantha", "Micheal"]

    def create_labels(self):
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabels().run()
