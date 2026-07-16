from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

from codex import get_all_exercises


class CodexScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(
            orientation="vertical",
            spacing=10,
            padding=20,
            **kwargs
        )

        self.show_list()


    def show_list(self):

        self.clear_widgets()

        title = Label(
            text="📖 دليل الصياد",
            font_size=35,
            size_hint=(1, 0.15)
        )

        self.add_widget(title)


        exercises = get_all_exercises()


        for exercise_id, exercise in exercises.items():

            button = Button(
                text=(
                    f"{exercise['name']}\n"
                    f"💪 {', '.join(exercise['muscles'])}\n"
                    f"⭐ الصعوبة: {exercise['difficulty']}"
                ),
                size_hint=(1, 0.12)
            )


            button.bind(
                on_press=lambda instance, e=exercise: self.show_exercise(e)
            )


            self.add_widget(button)



    def show_exercise(self, exercise):

        self.clear_widgets()


        title = Label(
            text=f"💪 {exercise['name']}",
            font_size=35,
            size_hint=(1, 0.1)
        )

        self.add_widget(title)


        image_path = exercise["image"]


        image = Image(
            source=image_path,
            size_hint=(1, 0.4)
        )

        self.add_widget(image)


        info = Label(
            text=f"""
📝 {exercise['description']}

🎯 العضلات:
{', '.join(exercise['muscles'])}

⭐ الصعوبة:
{exercise['difficulty']}

🔢 التكرارات:
{exercise['recommended_reps']}

⏱ الوقت:
{exercise['recommended_time']}
""",
            font_size=20
        )


        self.add_widget(info)


        back = Button(
            text="⬅ العودة",
            size_hint=(1, 0.12)
        )


        back.bind(
            on_press=lambda x: self.show_list()
        )


        self.add_widget(back)
