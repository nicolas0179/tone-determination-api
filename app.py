from typing import List

from flask import Flask, abort, jsonify
from pythainlp import subword_tokenize

from constants import ConsonantClass, LOW_CLASS_CONSONANTS, MID_CLASS_CONSONANTS, ALL_CONSONANTS, STOP_CONSONANTS, \
    SyllableType, Tone, SHORT_VOWELS, ToneMarker

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/api/sentence/<sentence>", methods=["GET"])
def findSentenceTones(sentence):
    return jsonify(getSentenceTones(sentence))


@app.route("/api/syllable/<syllable>", methods=["GET"])
def findTone(syllable):
    segmentedSyllable = subword_tokenize(syllable, engine='dict', keep_whitespace=False)
    if len(segmentedSyllable) != 1:
        abort(405, description="Not a single syllable!")
    return jsonify({
        "syllable": syllable,
        "tone": getTone(syllable)
    })


def getSentenceTones(sentence: str) -> List[dict[str, Tone]]:
    segmentedSentence = subword_tokenize(sentence, engine='dict', keep_whitespace=False)
    return [{
        "syllable": syllable,
        "tone": getTone(syllable)
    } for syllable in segmentedSentence]


def getTone(syllable: str) -> Tone:
    toneMarker = getToneMarker(syllable)
    if toneMarker == ToneMarker.HIGH_TONE_MARKER:
        return Tone.HIGH_TONE
    if toneMarker == ToneMarker.RISING_TONE_MARKER:
        return Tone.RISING_TONE
    initialConsonantClass = getInitialConsonantClassOfWord(syllable)
    if toneMarker == ToneMarker.LOW_TONE_MARKER and initialConsonantClass == ConsonantClass.LOW_CLASS:
        return Tone.FALLING_TONE
    if toneMarker == ToneMarker.LOW_TONE_MARKER and initialConsonantClass != ConsonantClass.LOW_CLASS:
        return Tone.LOW_TONE
    if toneMarker == ToneMarker.FALLING_TONE_MARKER and initialConsonantClass == ConsonantClass.LOW_CLASS:
        return Tone.HIGH_TONE
    if toneMarker == ToneMarker.FALLING_TONE_MARKER and initialConsonantClass != ConsonantClass.LOW_CLASS:
        return Tone.FALLING_TONE
    syllableType = isDeadOrLiveSyllable(syllable)
    if syllableType == SyllableType.LIVE and initialConsonantClass == ConsonantClass.HIGH_CLASS:
        return Tone.RISING_TONE
    if syllableType == SyllableType.LIVE and initialConsonantClass != ConsonantClass.HIGH_CLASS:
        return Tone.MID_TONE
    if initialConsonantClass == ConsonantClass.LOW_CLASS and containsShortVowel(syllable):
        return Tone.HIGH_TONE
    if initialConsonantClass == ConsonantClass.LOW_CLASS:
        return Tone.FALLING_TONE
    return Tone.LOW_TONE


def getToneMarker(syllable):
    if '่' in syllable:
        return ToneMarker.LOW_TONE_MARKER
    if '้' in syllable:
        return ToneMarker.FALLING_TONE_MARKER
    if '๊' in syllable:
        return ToneMarker.HIGH_TONE_MARKER
    if '๋' in syllable:
        return ToneMarker.RISING_TONE_MARKER
    return ToneMarker.NO_TONE_MARKER


def getConsonantClass(consonant: str) -> ConsonantClass:
    if consonant in LOW_CLASS_CONSONANTS:
        return ConsonantClass.LOW_CLASS
    if consonant in MID_CLASS_CONSONANTS:
        return ConsonantClass.MID_CLASS
    return ConsonantClass.HIGH_CLASS


def getInitialConsonant(word) -> str:
    for c in word:
        if c in ALL_CONSONANTS:
            return c


def getInitialConsonantClassOfWord(word: str) -> ConsonantClass:
    initialConsonant = getInitialConsonant(word)
    return getConsonantClass(initialConsonant)


def isDeadOrLiveSyllable(syllable: str) -> SyllableType:
    if hasFinalConsonant(syllable) and isEndingWithStopConsonant(syllable):
        return SyllableType.DEAD
    if hasFinalConsonant(syllable):
        return SyllableType.LIVE
    if containsShortVowel(syllable):
        return SyllableType.DEAD
    return SyllableType.LIVE


def hasFinalConsonant(syllable: str) -> bool:
    return syllable[-1] in ALL_CONSONANTS


def isEndingWithStopConsonant(syllable: str) -> bool:
    return syllable[-1] in STOP_CONSONANTS


def containsShortVowel(syllable: str):
    return any(c in SHORT_VOWELS for c in syllable) or all(c in ALL_CONSONANTS for c in syllable)


if __name__ == '__main__':
    app.run()

# import unicodedata as ud
#
# thai_str = 'ผ่าน'
#
# for cp in thai_str:
#     print(f'{cp}\t{ud.category(cp)}\t{ud.name(cp)}')
#
# print(sum(1 for cp in thai_str if ud.category(cp)[0] != 'M'))
