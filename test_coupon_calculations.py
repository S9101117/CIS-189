from score import coupon_calculations
import unittest


class MyTestCase( unittest.TestCase ):
    def test_price_under_ten(self):
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,5,10),7.85)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,5,15),7.74)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,5,20),7.64)
            with self.subTest():
                  self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,10,10),3.08)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,10,15),3.24)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(6.99,10,20),3.4)


    def test_price_under_between_ten_thirty(self):
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,5,10),19.39)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,5,15),18.75)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,5,20),16.12)
            with self.subTest():
                  self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,10,10),12.62)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,10,15),12.25)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(16.99,10,20),11.88)

    def test_price_under_between_thirty_fifty(self):
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(45,5,10),50.11)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(45,5,15),47.99)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(45,5,20),45.87)
            with self.subTest():
                  self.assertAlmostEqual(coupon_calculations.calculate_price(45,10,10),45.34)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(45,10,15),39.48)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(45,10,20),37.63)

    def test_price_under_over_fifty(self):
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(80,5,10),121.55)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(80,5,15),117.58)
            with self.subTest():
                    self.assertAlmostEqual(coupon_calculations.calculate_price(80,5,20),113.6)
            with self.subTest():
                  self.assertAlmostEqual(coupon_calculations.calculate_price(80,10,10),116.78)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(80,10,15),113.07)
            with self.subTest():
                   self.assertAlmostEqual(coupon_calculations.calculate_price(80,10,20),109.36)






if __name__ == '__main__':
    unittest.main()
