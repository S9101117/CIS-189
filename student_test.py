import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Duck', 'Daisy')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')

    def test_object_created_all_attributes(self):
        student = t.Student('Duck', 'Daisy', '111-11-1111') # this is not self.person from setUp, but local
        assert student.last_name == 'Duck'                 # note no self here on person or assert
        assert student.first_name == 'Daisy'
        assert student.major == 'Math'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t.Student('123', 'Daisy')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = t.Student('Duck', '123')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = t.Student('Duck', 'Daisy', 'abc')
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = t.Student('Duck', 'Daisy','Math', 'rr')

    def test_person_class_display_name(self):
        self.assertEqual(str(self.student), "Duck, Daisy:")

    def test_person_class_display_name_major(self):
        p = t.Student('Duck', 'Daisy', '111-11-1111')
        self.assertEqual(str(p), "Duck, Daisy:111-11-1111")

    def test_person_str(self):
        self.assertEqual(str(self.student), 'Duck, Daisy:')

if __name__ == '__main__':
    unittest.main()
