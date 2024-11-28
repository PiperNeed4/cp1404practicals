from kivy.app import App
from kivy.lang import Builder


CONVERSION_VALUE = 1.60934

class ConvertMilesKm(App):
    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        value = self.validate_input() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def handle_calculate(self):
        value = self.validate_input()
        result = value * CONVERSION_VALUE
        self.root.ids.output_label.text = str(result)


    def validate_input(self):
        try:
            return float(self.root.ids.input_number.text)
        except ValueError:
            return 0


ConvertMilesKm().run()
