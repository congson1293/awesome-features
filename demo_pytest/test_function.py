from function_to_test import extract_sentiment, text_contain_word
import pytest
"""
Reference: https://towardsdatascience.com/pytest-for-data-scientists-2990319e55e6
"""
# Test a single function


def test_extract_sentiment_positive():

    text = "I think today will be a great day"

    sentiment = extract_sentiment(text)

    assert sentiment > 0

# Parametrize with a List of Samples


testdata = ["I think today will be a great day",
            "I do not think this will turn out well"]


@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

# Parametrize with a List of Examples and Expected Outputs
# Test one Function at a time
# pytest test_func.py::test_text_contain_word


testdata2 = [
    ('There is a duck in this text', True),
    ('There is nothing here', False)
]


@pytest.mark.parametrize('sample, expected_output', testdata2)
def test_text_contain_word(sample, expected_output):

    word = 'duck'

    assert text_contain_word(word, sample) == expected_output

# Fixtures: Use the Same Data to Test Different Functions


@pytest.fixture
def example_data():
    return 'Today I found a duck and I am happy'


def test_extract_sentiment(example_data):

    sentiment = extract_sentiment(example_data)

    assert sentiment > 0


def test_text_contain_word(example_data):

    word = 'duck'

    assert text_contain_word(word, example_data) == True
