from behave import when, then
from hamcrest import assert_that, equal_to
from app import getInitialConsonantClassOfWord


@when('I look up the initial consonant of word {word}')
def lookupInitialConsonant(context, word):
    context.initialConsonantClass = getInitialConsonantClassOfWord(word)


@then('the resulting class should be {consonantClass}')
def thenResultingClassShouldBe(context, consonantClass):
    assert_that(context.initialConsonantClass.value, equal_to(consonantClass))
