from behave import when, then
from hamcrest import assert_that, equal_to
from app import isDeadOrLiveSyllable


@when('I look up the syllable {syllable}')
def lookupSyllable(context, syllable):
    context.syllableType = isDeadOrLiveSyllable(syllable)


@then('it should return a {syllableType} syllable')
def thenShouldReturnTypeSyllable(context, syllableType):
    assert_that(context.syllableType.value, equal_to(syllableType))
