def test_success_code():
    assert 10 / 2 == 5

def test_failure_code():
    assert 10 / 2 == 0

def test_exception():
    if output_got != desired_outputp # If something does go wrong
        raise ValueError("You got a value error!")