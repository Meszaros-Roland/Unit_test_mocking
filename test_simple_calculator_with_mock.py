import pytest
from simple_calculator import SimpleCalculator
from unittest.mock import Mock


def test_add_with_mock_history_service():
    mock_history = Mock()

    calc = SimpleCalculator(history_service = mock_history)

    result = calc.add(2, 3)

    assert result == 5

    mock_history.save_operation.assert_called_once()
    mock_history.save_operation.assert_called_with("add", 2, 3, 5)

def test_multiply_with_multiple_mocks():
    pass

def test_get_history_count_with_mock():
    pass