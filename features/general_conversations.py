from features.respond.tts import tts
from random import choice


def who_are_you(bot_name):
    replies = [
        'I am {}, your smarter personal assistant.'.format(bot_name),
        'Oh, You forget me, I am {}'.format(bot_name),
        'I am your friend {}'.format(bot_name),
        "{}, didn't I tell you before?".format(bot_name)
    ]
    tts(choice(replies))


def how_am_i():
    replies = [
        'You are goddamn handsome!',
        'My knees go weak when I see you.',
        'You look like the kindest person that I have met.'
    ]
    tts(choice(replies))


def tell_joke():
    jokes = [
        'What happens to a frogs car when it breaks down? It gets toad away.',
        'Why was six scared of seven? Because seven ate nine.',
        'Why are mountains so funny? Because they are hill areas.',
        "This might make you laugh. How do robots eat guacamole? With computer chips.",
        'Have you ever tried to eat a clock?'
        'I hear it is very time consuming.',
        'What happened when the wheel was invented? A revolution.',
        'What do you call a fake noodle? An impasta!',
        'Did you hear about that new broom? It is sweeping the nation!',
        'What is heavy forward but not backward? Ton.',
        'No, I always forget the punch line.'
    ]
    tts(choice(jokes))


def who_am_i(username):
    tts('You are {}, a brilliant person. I love you!'.format(username))


def where_born():
    tts('I was created by a wonderful CSE team as a graduation project in the faculty of Engineering, Minya - Egypt.')


def how_are_you():
    replies = [
        'I am fine, thank you.',
        'Pretty good',
        'Cannt be better',
        'Not bad'
    ]
    tts(choice(replies))


def undefined():
    tts("I Couldn't understand you")
