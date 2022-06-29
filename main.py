import os

class Quotes:
    quotes = {
            "en": [
                "I'm not a great programmer; I'm just a good programmer with great habits.",
                "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.",
                "First, solve the problem. Then, write the code.",
                "The best thing about a boolean is that even if you are wrong, you are only off by a bit.",
                "The best way to predict the future is to invent it.",
                "The best way to keep a programmer in the loop is to feed him programs that run forever.",
                "The best way to make sure your code works is to run it twice. If it runs once, it will probably work, but if it runs twice, it will probably crash.",
                "The best way to understand recursion is to try it.",
                "The best way to understand a program is to have a program that can run it."
            ],
            "de": [
                "Ich bin nicht ein guter Programmierer; ich bin nur ein guter Programmierer mit guten Verhältnissen.",
                "Immer programmieren, als wenn der Programmierer, der die Software verwaltet, ein violentes Psychopath ist, der weiß, wo du bist.",
                "Zuerst muss das Problem gelöst werden. Dann muss die Software geschrieben werden.",
                "Der beste Weg um einen Boolean zu erfahren ist, wenn du nicht stimmst, nur einen Bit zu verschwenden.",
                "Der beste Weg um die Zukunft zu erfahren ist es, es zu inventieren.",
                "Der beste Weg um einen Programmierer in der Schleife zu halten ist es, ihm Programme zu geben, die immer laufen.",
                "Der beste Weg um den Code zu verifizieren ist es, ihn zweimal zu testen. Wenn er einmal läuft, wird er wahrscheinlich funktionieren, aber wenn er zweimal läuft, wird er wahrscheinlich kaputt gehen.",
                "Der beste Weg um die Rekursion zu verstehen ist es, sie zu versuchen.",
                "Der beste Weg um einen Programm zu verstehen ist es, einen Programm zu haben, der ihn läuft."
            ]
        }

    def __init__(self, language):
        self.language = language
        self.quote = self.quotes[language][0]

    def get_random_quote(self):
        self.quote = self.quotes[self.language][int(os.urandom(1)[0] / 256 * len(self.quotes[self.language]))]
        return self.quote

    def add_quote(self, quote):
        self.quotes[self.language].append(quote)
        return self.quotes[self.language]

    def get_quote_list(self):
        return self.quotes[self.language]

    def get_quote_count(self):
        return len(self.quotes[self.language])

    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language
        return self.language

    def get_quote(self):
        return self.quote


if __name__ == "__main__":
    quotes = Quotes("en")
    print(quotes.get_random_quote())
    print(quotes.get_quote_count())
    print(quotes.add_quote("This is a new quote"))
    print(quotes.get_quote_count())
