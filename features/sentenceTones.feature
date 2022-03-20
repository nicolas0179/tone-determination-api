Feature: Tone determination of a sentence

  Scenario Outline: Determine the lexical tone of each syllable of a sentence
    When I look up the lexical tone of each syllable of the sentence <sentence>
    Then I should expect the segmentation <segmentation> with the tones <tones>
    Examples:
      | sentence  | segmentation | tones                          |
      | ประเทศไทย | ประ,เทศ,ไทย  | LOW_TONE,FALLING_TONE,MID_TONE |