# -*- coding: UTF-8 -*-

from behave import when, then
from hamcrest import assert_that, equal_to
from app import getToneMarker


@when('I look up the tone marker of word {word}')
def lookupToneMarker(context, word):
    context.toneMarker = getToneMarker(word)


@then('the resulting tone marker should be {toneMarker}')
def thenResultingToneMarkerShouldBe(context, toneMarker):
    assert_that(context.toneMarker.value, equal_to(toneMarker))
