Feature: Tone marker determination

  Scenario Outline: Determining if there is a tone marker
	When I look up the tone marker of word <word>
	Then the resulting tone marker should be <tone marker>
	Examples:
	  | word | tone marker         |
	  | ผ่าน | LOW_TONE_MARKER     |
	  | น้ำ  | FALLING_TONE_MARKER |
	  | โต๊ะ | HIGH_TONE_MARKER    |
	  | เจ๋ง | RISING_TONE_MARKER  |
	  | บาท  | NO_TONE_MARKER      |