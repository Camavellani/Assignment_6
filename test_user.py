# Andrew worked on unit test for log in and searching all courses
import unittest
from test_user_class import test_user_class

class UserTest(unittest.TestCase):
    def test_login_student(self):
        print("Student Log In Test called...")
        # Arrange
        self.user_choice = 1
        self.first = "Andrew"
        self.last = "Lee"
        self.ID = "000000"
        # Act
        result = test_user_class.test_login(test_user_class, self.user_choice, self.first, self.last, self.ID)
        # Assert
        self.assertEqual(result, 10)
    def test_login_instructor(self):
        print("Instructor Log In Test called...")
        # Arrange
        self.user_choice = 2
        self.first = "Daniel"
        self.last = "Bernoulli"
        self.ID = "1"
        # Act
        result = test_user_class.test_login(test_user_class, self.user_choice, self.first, self.last, self.ID)
        # Assert
        self.assertEqual(result, 10)
    def test_login_admin(self):
        print("Admin Log In Test called...")
        # Arrange
        self.user_choice = 3
        self.first = "John"
        self.last = "Johnson"
        self.ID = "1"
        # Act
        result = test_user_class.test_login(test_user_class, self.user_choice, self.first, self.last, self.ID)
        # Assert
        self.assertEqual(result, 10)
    def test_search_courses(self):
        print("Searching Course Test called...")
        # Arrange
        
        # Act
        result = test_user_class.test_search_courses(test_user_class)
        # Assert
        self.assertEqual(result, 10)
if __name__ == "__main__":
    unittest.main()