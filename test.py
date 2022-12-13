def test_detect_language(test_case):
    assert detect_language(test_case.text) == test_case.expected
