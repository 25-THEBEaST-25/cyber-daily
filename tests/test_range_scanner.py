import pytest

from range_scanner import MAX_PORT, MIN_PORT, build_arg_parser, main, parse_port


def test_parse_port_accepts_valid_value():
    assert parse_port("80", "start_port") == 80


def test_parse_port_accepts_boundaries():
    assert parse_port(str(MIN_PORT), "start_port") == MIN_PORT
    assert parse_port(str(MAX_PORT), "end_port") == MAX_PORT


def test_parse_port_rejects_non_numeric():
    with pytest.raises(ValueError, match="must be an integer"):
        parse_port("abc", "start_port")


def test_parse_port_rejects_out_of_range():
    with pytest.raises(ValueError, match="must be between"):
        parse_port(str(MAX_PORT + 1), "end_port")
    with pytest.raises(ValueError, match="must be between"):
        parse_port(str(MIN_PORT - 1), "start_port")


def test_build_arg_parser_defaults_to_none_when_no_args():
    args = build_arg_parser().parse_args([])
    assert args.target is None
    assert args.start_port is None
    assert args.end_port is None


def test_build_arg_parser_parses_positional_args():
    args = build_arg_parser().parse_args(["127.0.0.1", "20", "1024"])
    assert args.target == "127.0.0.1"
    assert args.start_port == "20"
    assert args.end_port == "1024"


def test_main_rejects_empty_target(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")
    exit_code = main([])
    assert exit_code == 1
    assert "Target must not be empty" in capsys.readouterr().err


def test_main_rejects_non_numeric_port(capsys):
    exit_code = main(["127.0.0.1", "not-a-port", "80"])
    assert exit_code == 1
    assert "must be an integer" in capsys.readouterr().err


def test_main_rejects_negative_port(capsys):
    exit_code = main(["127.0.0.1", "-5", "80"])
    assert exit_code == 1
    assert "must be between" in capsys.readouterr().err


def test_main_rejects_start_greater_than_end(capsys):
    exit_code = main(["127.0.0.1", "100", "50"])
    assert exit_code == 1
    assert "start_port must not be greater than end_port" in capsys.readouterr().err


def test_main_scans_valid_range_and_returns_zero(capsys):
    exit_code = main(["127.0.0.1", "65533", "65535"])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "Scanning 127.0.0.1 from port 65533 to 65535" in out
