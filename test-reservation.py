import unittest
from reservation import Reservation

class TestReservation(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.reservation = Reservation(1, 1, 1, '101')

    def test_reservation_creation(self):
        """Test para verificar la correcta creación de una reserva."""
        self.assertEqual(self.reservation.id, 1)
        self.assertEqual(self.reservation.customer_id, 1)
        self.assertEqual(self.reservation.hotel_id, 1)
        self.assertEqual(self.reservation.room_number, '101')

    def test_modify_reservation(self):
        """Test para verificar la funcionalidad de modificar una reserva."""
        # Modificar algunos campos de la reserva
        self.reservation.modify_reservation(customer_id=2, room_number='102')
        self.assertEqual(self.reservation.customer_id, 2)
        self.assertEqual(self.reservation.room_number, '102')

if __name__ == '__main__':
    unittest.main()