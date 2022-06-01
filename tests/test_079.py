from unittest import TestCase

try:
    from problems.problem_079 import ReceiptItem
except Exception:
    class ReceiptItem:
        pass


class ProblemTests(TestCase):
    def test_receipt_item_has_quantity_and_price(self):
        ReceiptItem(0, 0)

    def test_get_total_returns_product_of_quantity_and_price(self):
        item = ReceiptItem(12, 5.50)
        expected = 66
        self.assertEqual(
            expected,
            item.get_total(),
            msg="Expected 66 from an item with 12 quantity and 5.50 price",
        )
