from app import getToneMarker, getConsonantClass, getInitialConsonantClassOfWord, hasFinalConsonant, \
    isEndingWithStopConsonant, containsShortVowel, getSentenceTones
from constants import ConsonantClass, ToneMarker


def test_findSentenceTones():
    pass


def test_getSentenceTones(mocker):
    subword_tokenize_mock = mocker.patch('pythainlp.subword_tokenize', return_value=['syllabe1', 'syllabe2'])
    actual = getSentenceTones('sentence')
    subword_tokenize_mock.assert_called_once_with('sentence')


def test_findTone():
    pass


def test_getToneMarker():
    assert getToneMarker('ผ่าน') == ToneMarker.LOW_TONE_MARKER
    assert getToneMarker('น้ำ') == ToneMarker.FALLING_TONE_MARKER
    assert getToneMarker('ก๊า') == ToneMarker.HIGH_TONE_MARKER
    assert getToneMarker('ก๋า') == ToneMarker.RISING_TONE_MARKER
    assert getToneMarker('บาท') == ToneMarker.NO_TONE_MARKER


def test_getConsonantClass():
    assert getConsonantClass('ล') == ConsonantClass.LOW_CLASS
    assert getConsonantClass('ก') == ConsonantClass.MID_CLASS
    assert getConsonantClass('ข') == ConsonantClass.HIGH_CLASS


def test_getInitialConsonantClassOfWord(mocker):
    getInitialConsonantMock = mocker.patch('app.getInitialConsonant', return_value='initialConsonant')
    getConsonantClassMock = mocker.patch('app.getConsonantClass', return_value=ConsonantClass.MID_CLASS)
    actual = getInitialConsonantClassOfWord('word')
    assert actual == ConsonantClass.MID_CLASS
    getInitialConsonantMock.assert_called_once_with('word')
    getConsonantClassMock.assert_called_once_with('initialConsonant')


def test_hasFinalConsonant():
    assert hasFinalConsonant('ตก') is True
    assert hasFinalConsonant('ซัก') is True
    assert hasFinalConsonant('ลิ') is False


def test_isEndingWithStopConsonant():
    assert isEndingWithStopConsonant('ตก') is True
    assert isEndingWithStopConsonant('เกง') is False


def test_containsShortVowel():
    assert containsShortVowel('ลิ') is True
    assert containsShortVowel('เกง') is False
