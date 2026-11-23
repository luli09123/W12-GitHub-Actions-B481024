"""執行：python -m pytest -v"""
import pytest
from inventory import needs_restock, restock_items


def test_below_threshold():
    assert needs_restock(5) is True


def test_equal_threshold():
    assert needs_restock(10) is False


def test_above_threshold():
    assert needs_restock(15) is False


def test_custom_threshold():
    assert needs_restock(12, threshold=15) is True


def test_invalid_quantity():
    with pytest.raises(ValueError):
        needs_restock(-1)


def test_restock_items():
    items = [{"name": "筆記本", "quantity": 4}, {"name": "滑鼠", "quantity": 12}]
    assert restock_items(items) == ["筆記本"]

def test_zero_quantity():
    assert needs_restock(0) is True


def test_threshold_zero():
    assert needs_restock(0, threshold=0) is False