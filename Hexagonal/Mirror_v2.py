import datetime
import dictionnaire
class MirrorApp:
    def __init__(self, lang="fr"):
        self.lang = lang.lower()
        self.current_hour = datetime.datetime.now().hour

    def get_greeting(self):
        period = self._get_time_of_day()
        return dictionnaire.greetings[self.lang][period] # dégager ça pour avoir plutot un getperiod dans la classe dictionnaire

    def _get_time_of_day(self):
        if 5 <= self.current_hour < 12:
            return "morning"
        elif 12 <= self.current_hour < 18:
            return "afternoon"
        elif 18 <= self.current_hour < 22:
            return "evening"
        else:
            return "night"

    def mirror_text(self, text):
        return text[::-1]

    def is_palindrome(self, text):
        cleaned_text = text.lower().replace(" ", "")
        return cleaned_text == cleaned_text[::-1]

    def get_farewell(self):
        period = self._get_time_of_day()
        return dictionnaire.farewells[self.lang][period] #remplacer ça par un appel haut niveau avec un get vers dictionnaire

    def run(self):
        print(self.get_greeting())
        input_prompt = dictionnaire.inputs_run[self.lang]["entrer"] #same

        while True:
            user_input = input(input_prompt).lower()
            if user_input == 'exit':
                break

            if self.is_palindrome(user_input):
                print(dictionnaire.inputs_run[self.lang]["reponse"]) #same

            else:
                mirrored_text = self.mirror_text(user_input)
                print( dictionnaire.inputs_run[self.lang]["m"], mirrored_text) #same

        print(self.get_farewell())

if __name__ == "__main__":
    lang_choice = input("Choose a language (fr for French, en for English): ").lower()
    if lang_choice not in ["fr", "en"]:
        print("Invalid language choice. Defaulting to French.")
        lang_choice = "fr"
    app = MirrorApp(lang_choice)
    app.run()