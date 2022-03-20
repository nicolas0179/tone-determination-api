Feature: Initial consonant class determination

  Scenario Outline: Determining the initial consonant class
	When I look up the initial consonant of word <word>
	Then the resulting class should be <consonant class>
	Examples:
	  | word  | consonant class |
	  | ผ่าน  | HIGH_CLASS      |
	  | น้ำ   | LOW_CLASS       |
	  | โต๊ะ  | MID_CLASS       |
	  | เจ๋ง  | MID_CLASS       |
	  | บาท   | MID_CLASS       |
	  | หก    | HIGH_CLASS      |
	  | หลาย  | HIGH_CLASS      |
	  | ใหม่  | HIGH_CLASS      |
	  | หมด   | HIGH_CLASS      |
	  | อยาก  | MID_CLASS       |
	  | อย่าง | MID_CLASS       |
