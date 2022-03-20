from enum import Enum


class ToneMarker(Enum):
    LOW_TONE_MARKER = 'LOW_TONE_MARKER'
    FALLING_TONE_MARKER = 'FALLING_TONE_MARKER'
    HIGH_TONE_MARKER = 'HIGH_TONE_MARKER'
    RISING_TONE_MARKER = 'RISING_TONE_MARKER'
    NO_TONE_MARKER = 'NO_TONE_MARKER'


class Tone(str, Enum):
    LOW_TONE = 'LOW_TONE'
    FALLING_TONE = 'FALLING_TONE'
    HIGH_TONE = 'HIGH_TONE'
    RISING_TONE = 'RISING_TONE'
    MID_TONE = 'MID_TONE'


class ConsonantClass(Enum):
    LOW_CLASS = 'LOW_CLASS'
    MID_CLASS = 'MID_CLASS'
    HIGH_CLASS = 'HIGH_CLASS'


class SyllableType(Enum):
    LIVE = 'LIVE'
    DEAD = 'DEAD'


LOW_CLASS_CONSONANTS = ['ค', 'ฅ', 'ฆ', 'ง', 'ช', 'ซ', 'ฌ', 'ญ', 'ฑ', 'ฒ', 'ณ', 'ท', 'ธ', 'น', 'พ', 'ฟ', 'ภ', 'ม', 'ย',
                        'ร', 'ล', 'ว', 'ฬ', 'ฮ']
MID_CLASS_CONSONANTS = ['ก', 'จ', 'ฎ', 'ฏ',	'ด', 'ต', 'บ', 'ป', 'อ']
HIGH_CLASS_CONSONANTS = ['ข', 'ฃ', 'ฉ', 'ฐ', 'ถ', 'ผ', 'ฝ', 'ศ', 'ษ', 'ส', 'ห']
ALL_CONSONANTS = [*LOW_CLASS_CONSONANTS, *MID_CLASS_CONSONANTS, *HIGH_CLASS_CONSONANTS]
STOP_CONSONANTS = ['ก', 'ข', 'ค', 'ฆ', 'ป', 'พ', 'ภ', 'ฟ', 'บ', 'ต', 'ฏ', 'ถ', 'ฐ', 'ท', 'ฒ', 'ฑ', 'ธ', 'จ', 'ช', 'ฌ',
                   'ส', 'ศ', 'ษ', 'ด', 'ฎ']

SHORT_VOWELS = ['ะ', 'รร', '็', 'ิ', 'ึ', 'ุ', 'ั', 'ไ', 'ใ']
ALL_VOWELS = ['ะัาำิีึืุูเแโใไ']
