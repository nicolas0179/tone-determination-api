from behave import when, then
from hamcrest import assert_that, equal_to
from app import getSentenceTones


@when('I look up the lexical tone of each syllable of the sentence {sentence}')
def lookupSentenceLexicalTones(context, sentence):
    sentenceTones = getSentenceTones(sentence)
    context.tones = [s['tone'] for s in sentenceTones]
    context.segmentation = [s['syllable'] for s in sentenceTones]


@then('I should expect the segmentation {segmentation} with the tones {tones}')
def thenShouldExpectSegmentationAndTones(context, segmentation, tones):
    expected_segmentation = segmentation.split(',')
    expected_tones = tones.split(',')
    actual_segmentation = context.segmentation
    actual_tones = context.tones
    assert_that(actual_segmentation, equal_to(expected_segmentation))
    assert_that(actual_tones, equal_to(expected_tones))
