import src.utils as utils


def test_log_prints_message(capsys):
    utils.log("Hello, test log!")
    captured = capsys.readouterr()
    assert "Hello, test log!" in captured.out

def test_log_handles_non_string(capsys):
    utils.log(12345)
    out = capsys.readouterr().out
    assert "12345" in out

def test_log_empty_message(capsys):
    utils.log("")
    out = capsys.readouterr().out
    assert "\n" in out  # empty message still prints newline

# Example if you have a hypothetical utility for validating urls
def test_validate_url_true():
    if hasattr(utils, "validate_url"):
        assert utils.validate_url("https://site.com")
        assert not utils.validate_url("not_a_url")

# Example if you have a hypothetical formatter
def test_format_title_exists():
    if hasattr(utils, "format_title"):
        val = utils.format_title("hello world")
        assert isinstance(val, str)