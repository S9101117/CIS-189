import unittest
from format_output import average_scores
import unittest.mock as mock

from format_output.average_scores import a, b, c


class MyTestCase(unittest.TestCase):
    def test_average(self):
     with mock.patch ('builtins.input', side_effect=[85, 90, 95]):
        assert average_scores.average(a,b,c)== 90



if __name__ == '__main__':
    unittest.main()
