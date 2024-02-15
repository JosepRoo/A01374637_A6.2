"""Archivo con codigo para las reservaciones"""


class Reservation:
    """Clase para objeto reservation"""

    def __init__(self, __id, customer_id, hotel_id, room_number):
        """
        Inicializa una reservacion
        """
        self.id = __id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number

    def modify_reservation(
        self,
        customer_id=None,
        hotel_id=None,
        room_number=None
    ):
        """
        Modifica la reservacion
        """
        if customer_id is not None:
            self.customer_id = customer_id
        if hotel_id is not None:
            self.hotel_id = hotel_id
        if room_number is not None:
            self.room_number = room_number

    def display_info(self):
        """
        Imprime la informacion de la reservacion
        """
        print(
            f"Reservation ID: {self.id}, "
            f"Customer ID: {self.customer_id}, "
            f"Hotel ID: {self.hotel_id}, "
            f"Room: {self.room_number}, "
        )
