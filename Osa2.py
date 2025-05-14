from colorama import Fore, init
import emoji

init(autoreset=True)

moods = {
    "happy": (Fore.YELLOW, "Tore kuulda! Jätka samas vaimus!", ":smile:"),
    "sad": (Fore.BLUE, "Kurb kuulda. Homme on uus päev!", ":pensive:"),
    "tired": (Fore.MAGENTA, "Võta aeg maha ja puhka!", ":sleeping:"),
    "excited": (Fore.GREEN, "Suurepärane! Jaga oma energiat maailmaga!", ":star_struck:")
}

user_mood = input("Kuidas sa täna end tunned? (happy, sad, tired, excited): ").strip().lower()

if user_mood in moods:
    color, message, emoji_symbol = moods[user_mood]
    print(color + message + " " + emoji.emojize(emoji_symbol, language="alias"))
else:
    print(Fore.RED + "Tundmatu meeleolu. Palun proovi: happy, sad, tired või excited.")
