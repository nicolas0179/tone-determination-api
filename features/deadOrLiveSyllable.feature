Feature: Dead or Live syllable determination

  Scenario Outline: Determine whether the syllable is a live syllable or a dead syllable
    When I look up the syllable <syllable>
    Then it should return a <type> syllable
    Examples:
      | syllable | type |
      | ลิ       | DEAD |
      | ซัก      | DEAD |
      | ขับ      | DEAD |
      | แกะ      | DEAD |
      | ตก       | DEAD |
      | กระ      | DEAD |
      | มีด      | DEAD |
      | จริง     | LIVE |
      | เต็ม     | LIVE |
      | ปืน      | LIVE |
      | เดิม     | LIVE |
      | หา       | LIVE |
      | งู       | LIVE |
      | มา       | LIVE |
      | ชาน      | LIVE |