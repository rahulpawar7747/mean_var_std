import unittest
import mean_var_std as mvs

class TestMeanVarStd(unittest.TestCase):

    def test_calculate_correct_result(self):
        result = mvs.calculate([0,1,2,3,4,5,6,7,8])
        self.assertEqual(result['max'][2], 8)
        self.assertEqual(result['min'][2], 0)
        self.assertEqual(result['sum'][2], 36)
        self.assertAlmostEqual(result['mean'][2], 4.0)
        self.assertAlmostEqual(result['variance'][2], 6.666666666666667, places=6)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            mvs.calculate([1, 2, 3])  # not 9 numbers

if __name__ == '__main__':
    unittest.main()
