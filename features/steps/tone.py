from behave import when, then
from hamcrest import assert_that, equal_to
from app import getTone


@when('I look up the lexical tone of the syllable {syllable}')
def lookupSyllableLexicalTone(context, syllable):
    context.tone = getTone(syllable)


@then('I should expect the tone {tone}')
def thenShouldExpectTone(context, tone):
    assert_that(context.tone.value, equal_to(tone))
