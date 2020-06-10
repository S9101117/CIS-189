from score import coupon_calculations
import unittest


class MyTestCase( unittest.TestCase ):
    def test_price_under_ten(self):
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,5,10),x)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,5,15),x)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,5,20),x)
            with self.subTest():
                  self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,10,10),x)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,10,15),x)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,10,20),x)


    def test_price_under_between_ten_thirty(self):
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,5,10),x)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,5,15),x)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,5,20),x)
            with self.subTest():
                  self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,10,10),x)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,10,15),x)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,10,20),x)

    def test_price_under_between_thirty_fifty(self):
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(45,5,10),x)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(45,5,15),x)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(45,5,20),x)
            with self.subTest():
                  self.assertAlmostEqual(coupon_calculations.calculate_price(45,10,10),x)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(45,10,15),x)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(45,10,20),x)

    def test_price_under_over_fifty(self):
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(80,5,10),x)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(80,5,15),x)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(80,5,20),x)
            with self.subTest():
                  self.assertAlmostEqual(coupon_calculations.calculate_price(80,10,10),x)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(80,10,15),x)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(80,10,20),x)






if __name__ == '__main__':
    unittest.main()
