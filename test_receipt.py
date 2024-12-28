import unittest
from Receipt import Receipt, Ingredient

class TestReceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.receipt_data = {
            "title": "Драники",
            "ingredients_list": [
                ('Картофель', 500, 400, 50),
                ('Лук', 100, 80, 20),
                ('Яйцо', 50, 40, 10),
                ('Соль', 5, 5, 2),
                ('Масло подсолнечное', 50, 40, 30),
            ],
        }
        cls.receipt = Receipt(cls.receipt_data['title'], cls.receipt_data['ingredients_list'])

    def setUp(self):
        self.receipt_data_2 = {
            "title": "Ершик",
            "ingredients_list": [
                ('Рыба', 300, 250, 200),
                ('Картофель', 200, 150, 30),
                ('Морковь', 100, 80, 20),
                ('Лук', 50, 40, 10),
                ('Соль', 5, 5, 2),
            ],
        }
        self.receipt_2 = Receipt(self.receipt_data_2['title'], self.receipt_data_2['ingredients_list'])

    def test_calc_cost(self):
        self.assertEqual(self.receipt.calc_cost(), 112)
        self.assertEqual(self.receipt_2.calc_cost(), 262)

    def test_calc_weight_raw(self):
        self.assertEqual(self.receipt.calc_weight(raw=True), 705)
        self.assertEqual(self.receipt_2.calc_weight(raw=True), 655)

    def test_calc_weight_cooked(self):
        self.assertEqual(self.receipt.calc_weight(raw=False), 565)
        self.assertEqual(self.receipt_2.calc_weight(raw=False), 525)

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
