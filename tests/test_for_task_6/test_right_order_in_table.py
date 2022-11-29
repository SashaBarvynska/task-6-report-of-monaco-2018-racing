import pytest

from task_6_racers_Barvynska.task_6 import right_order_in_table
from tests.CONSTANT import DATA, DATA_IN_ORDER_ASC, DATA_IN_ORDER_DESC


@pytest.mark.parametrize(
    "test_data, order, expected_order",
    [(DATA, True, DATA_IN_ORDER_ASC), (DATA, True, DATA_IN_ORDER_ASC)],
)
def test_right_order_in_table(test_data, order, expected_order):
    assert right_order_in_table(test_data, order).equals(expected_order)
