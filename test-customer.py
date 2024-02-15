import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer(1, "José Peréz", "johndoe@example.com")

    def test_modify_info(self):
        """Test para verificar la correcta edicion de un cliente."""
        new_name = "Juan Peréz"
        self.customer1.modify_info(name=new_name)
        self.assertEqual(self.customer1.name, new_name)

if __name__ == '__main__':
    unittest.main()