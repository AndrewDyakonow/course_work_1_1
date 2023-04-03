import random


def morse_encode(word: str) -> str:
    """Переводит слова на английском языке в последовательности точек и тирe"""
    encode_word = ''
    for letter in word:
        encode_word += encode_letter.get(letter) + ' '
    return encode_word


def get_word() -> str:
    """Получает случайное слово из списка."""
    random_word = random.sample(list_words, 1)
    return random_word[0]


def print_statistics(answers: list) -> None:
    """Выводит статистику"""
    print()
    print(f'Всего задачек: {len(answers)}')
    print(f'Отвечено верно: {answers.count(True)}')
    print(f'Отвечено неверно: {answers.count(False)}')


def check_answers(random_word_play, user_answer):
    if user_answer == random_word_play:
        print('Правильно!')
        return True
    else:
        print(f'Неправильно! Правильный ответ {random_word_play}')
        return False


list_words = ['code', 'bit', 'list', 'soul', 'next']
encode_letter = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}
answers = []

print('Сегодня мы потренируемся расшифровывать морзянку. ')
input('Нажмите Enter и начнем ')


for game in range(1, 6):
    random_word_play = get_word()
    encode_word_play = morse_encode(random_word_play)
    user_answer = input(f'Слово №{game} {encode_word_play}')
    answers.append(check_answers(random_word_play, user_answer))

print_statistics(answers)
