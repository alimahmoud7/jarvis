import re
import wikipedia
from features.respond.tts import tts


def define_subject(cleaned_message):
    try:
        wiki_data = wikipedia.summary(cleaned_message, sentences=5)
        print('BEFORE::: ', wiki_data)
        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(wiki_data)
        while m:
            wiki_data = m.group(1) + m.group(2)
            m = regEx.match(wiki_data)
        print('AFTER::: ', wiki_data)
        wiki_data = wiki_data.replace("'", "")
        tts(wiki_data)
    except wikipedia.exceptions.DisambiguationError as e:
        tts('Can you please be more specific? You may choose something from the following.')
        print("Can you please be more specific? You may choose something from the following.; {0}".format(e))
