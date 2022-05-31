from unittest import TestCase

try:
    from problems.problem_079 import ReceiptItem
    from problems.problem_080 import Receipt
except Exception:
    class ReceiptItem:
        pass
    class Receipt:
        pass


class ProblemTests(TestCase):
    def test_receipt_has_tax_rate(self):
        Receipt(0)

    def test_receipt_subtotal_is_sum_of_item_totals(self):
        receipt = Receipt(0.1)
        self.assertEqual(
            0,
            receipt.get_subtotal(),
            msg="Empty receipt should have 0 subtotal",
        )

        receipt.add_item(ReceiptItem(2, 6))
        self.assertEqual(
            12,
            receipt.get_subtotal(),
            msg="Receipt with 2 items @ 6 should have 12 subtotal",
        )

        receipt.add_item(ReceiptItem(1, 5))
        self.assertEqual(
            17,
            receipt.get_subtotal(),
            msg="Receipt with 2@6 and 1@5 should have 17 subtotal",
        )

    def test_receipt_total_is_sum_of_item_totals_times_tax(self):
        receipt = Receipt(0.1)
        self.assertEqual(
            0,
            receipt.get_total(),
            msg="Empty receipt should have 0 total",
        )

        receipt.add_item(ReceiptItem(2, 6))
        self.assertAlmostEqual(
            13.2,
            receipt.get_total(),
            2,
            msg="Receipt with 2 items @ 6 should have 13.2 total",
        )

        receipt.add_item(ReceiptItem(1, 5))
        self.assertAlmostEqual(
            18.7,
            receipt.get_total(),
            2,
            msg="Receipt with 2@6 and 1@5 should have 18.7 total",
        )
