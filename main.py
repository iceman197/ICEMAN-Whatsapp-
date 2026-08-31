import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.core.window import Window


class IcemanApp(App):

    def build(self):
        Window.clearcolor = (0.07, 0.07, 0.07, 1)

        self.main = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=8
        )

        # HEADER
        self.main.add_widget(
            Label(
                text="ICEMAN",
                font_size=38,
                size_hint_y=None,
                height=60
            )
        )

        self.main.add_widget(
            Label(
                text="MATH SOLVER",
                font_size=20,
                color=(0.65, 0.65, 0.65, 1),
                size_hint_y=None,
                height=35
            )
        )

        # MENU
        menu = BoxLayout(
            size_hint_y=None,
            height=55,
            spacing=5
        )

        calc_button = Button(
            text="CALCULATOR",
            font_size=16
        )

        angle_button = Button(
            text="ANGLES",
            font_size=16
        )

        calc_button.bind(
            on_press=lambda x: self.show_calculator()
        )

        angle_button.bind(
            on_press=lambda x: self.show_angles()
        )

        menu.add_widget(calc_button)
        menu.add_widget(angle_button)

        self.main.add_widget(menu)

        # CONTENT
        self.content = BoxLayout(
            orientation="vertical",
            spacing=8
        )

        self.main.add_widget(self.content)

        self.show_calculator()

        return self.main

    # =========================
    # CLEAR CONTENT
    # =========================

    def clear_content(self):
        self.content.clear_widgets()

    # =========================
    # CALCULATOR
    # =========================

    def show_calculator(self):

        self.clear_content()

        self.content.add_widget(
            Label(
                text="CALCULATOR",
                font_size=28,
                size_hint_y=None,
                height=55
            )
        )

        self.display = TextInput(
            font_size=28,
            multiline=False,
            halign="right",
            size_hint_y=None,
            height=70
        )

        self.content.add_widget(self.display)

        buttons = GridLayout(
            cols=4,
            spacing=4
        )

        values = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "(", ")", "BACK", "C"
        ]

        for value in values:

            button = Button(
                text=value,
                font_size=20
            )

            button.bind(
                on_press=lambda instance,
                v=value: self.calculator_button(v)
            )

            buttons.add_widget(button)

        self.content.add_widget(buttons)

    def calculator_button(self, value):

        if value == "C":

            self.display.text = ""

        elif value == "BACK":

            self.display.text = self.display.text[:-1]

        elif value == "=":

            try:

                expression = self.display.text

                allowed = "0123456789+-*/(). "

                if any(
                    char not in allowed
                    for char in expression
                ):
                    raise ValueError

                answer = eval(
                    expression,
                    {"__builtins__": {}},
                    {}
                )

                self.display.text = str(answer)

            except:

                self.display.text = "Error"

        else:

            self.display.text += value

    # =========================
    # ANGLE SOLVER
    # =========================

    def show_angles(self):

        self.clear_content()

        self.content.add_widget(
            Label(
                text="ANGLE SOLVER",
                font_size=28,
                size_hint_y=None,
                height=55
            )
        )

        self.problem = Spinner(
            text="Triangle Missing Angle",
            values=(
                "Triangle Missing Angle",
                "Complementary Angle",
                "Supplementary Angle",
                "Angles Around a Point",
                "Straight Line Angle"
            ),
            size_hint_y=None,
            height=55
        )

        self.problem.bind(
            text=lambda spinner, value:
            self.create_angle_inputs()
        )

        self.content.add_widget(self.problem)

        self.inputs = BoxLayout(
            orientation="vertical",
            spacing=5,
            size_hint_y=None,
            height=170
        )

        self.content.add_widget(self.inputs)

        self.result = Label(
            text="ANSWER WILL APPEAR HERE",
            font_size=20,
            size_hint_y=None,
            height=70
        )

        self.content.add_widget(self.result)

        solve = Button(
            text="SOLVE ANGLE",
            font_size=18,
            size_hint_y=None,
            height=60
        )

        solve.bind(
            on_press=lambda x: self.solve_angle()
        )

        self.content.add_widget(solve)

        self.create_angle_inputs()

    # =========================
    # CREATE INPUTS
    # =========================

    def create_angle_inputs(self):

        self.inputs.clear_widgets()

        self.entries = []

        problem = self.problem.text

        if problem == "Triangle Missing Angle":

            names = ["Angle 1", "Angle 2"]

        elif problem in (
            "Complementary Angle",
            "Supplementary Angle",
            "Straight Line Angle"
        ):

            names = ["Known Angle"]

        else:

            names = [
                "Angle 1",
                "Angle 2",
                "Angle 3"
            ]

        for name in names:

            entry = TextInput(
                hint_text=name + " (degrees)",
                font_size=18,
                multiline=False
            )

            self.entries.append(entry)

            self.inputs.add_widget(entry)

    # =========================
    # SOLVE
    # =========================

    def solve_angle(self):

        try:

            values = []

            for entry in self.entries:

                if not entry.text.strip():
                    raise ValueError(
                        "Enter all angles."
                    )

                values.append(
                    float(entry.text)
                )

            problem = self.problem.text

            if problem == "Triangle Missing Angle":

                answer = 180 - values[0] - values[1]

                if answer <= 0:
                    raise ValueError(
                        "Invalid triangle angles."
                    )

            elif problem == "Complementary Angle":

                answer = 90 - values[0]

            elif problem == "Supplementary Angle":

                answer = 180 - values[0]

            elif problem == "Straight Line Angle":

                answer = 180 - values[0]

            else:

                answer = (
                    360
                    - values[0]
                    - values[1]
                    - values[2]
                )

            self.result.text = (
                f"ANSWER: {answer:.2f}°"
            )

        except Exception as error:

            self.result.text = (
                "ERROR: " + str(error)
            )


if __name__ == "__main__":
    IcemanApp().run()