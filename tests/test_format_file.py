import pytest

from src.task_6_Barvynska import FormatFileTemp


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER", {'DRR': {'driver': 'Daniel Ricciardo', 'car': 'RED BULL RACING TAG HEUER'}}),
        ("MES_Marcus Ericsson_SAUBER FERRARI\nLSW_Lance Stroll_WILLIAMS MERCEDES", {'MES': {'driver': 'Marcus Ericsson', 'car': 'SAUBER FERRARI'}, 'LSW': {'driver': 'Lance Stroll', 'car': 'WILLIAMS MERCEDES'}}),
    ],
)
def test_format_file_abbreviation_data(test_input, expected):
    assert FormatFileTemp.format_file_abbreviation_data(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("SVF2018-05-24_12:02:58.917\nNHR2018-05-24_12:02:49.914", {'SVF': '12:02:58.917', 'NHR': '12:02:49.914'}),
        ("MES2018-05-24_12:05:58.778\nRGH2018-05-24_12:06:27.441\nSPF2018-05-24_12:13:13.883\nLSW2018-05-24_12:07:26.834\nDRR2018-05-24_12:11:24.067\nNHR2018-05-24_12:04:02.979\nCSR2018-05-24_12:04:28.095\nKMH2018-05-24_12:04:04.396\n", {'MES': '12:05:58.778', 'RGH': '12:06:27.441', 'SPF': '12:13:13.883', 'LSW': '12:07:26.834', 'DRR': '12:11:24.067', 'NHR': '12:04:02.979', 'CSR': '12:04:28.095', 'KMH': '12:04:04.396'}),
    ],
)
def test_format_file_time(test_input, expected):
    assert FormatFileTemp.format_file_time(test_input) == expected
