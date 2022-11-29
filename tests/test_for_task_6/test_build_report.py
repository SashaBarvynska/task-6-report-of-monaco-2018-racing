import pytest

from task_6_racers_Barvynska import build_report
from tests.CONSTANT import (RESULT_ASC, RESULT_DESC, TABLES_IN_ORDER_ASC,
                            TABLES_IN_ORDER_DESC)


@pytest.mark.parametrize(
    "test_input, expected",
    [(TABLES_IN_ORDER_ASC, RESULT_ASC), (TABLES_IN_ORDER_DESC, RESULT_DESC)],
)
def test_build_report(test_input, expected):
    assert build_report(test_input) == expected
