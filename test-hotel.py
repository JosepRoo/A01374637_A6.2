import unittest
from hotel import Hotel

class TestHotel(unittest.TestCase):

    def setUp(self):
        self.hotel1 = Hotel(1, "Hotel Test 1", {"101": True, "102": True})
        self.hotel2 = Hotel(2, "Hotel Test 2", {"201": True, "202": False})

    def test_reserve_room_available(self):
        """Test para verificar la correcta reservacion de un cuarto disponible."""
        self.assertTrue(self.hotel1.reserve_room("102"))
        self.assertFalse(self.hotel1.check_room_availability("102"))

    def test_cancel_reservation(self):
        """Test para verificar la correcta cancelación."""
        self.assertTrue(self.hotel2.cancel_reservation("202"))
        self.assertTrue(self.hotel2.check_room_availability("202"))

    def test_modify_info(self, new_name="Hotel Test 4"):
        """Test para verificar la correcta edicion de un hotel."""
        self.hotel1.modify_info(name=new_name)
        self.assertEqual(self.hotel1.name, new_name)

if __name__ == '__main__':
    unittest.main()
