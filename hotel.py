"""Archivo con codigo para comportamiento de hotel"""


class Hotel:
    """Clase para objeto hotel"""

    def __init__(self, __id, name, rooms):
        """
        Inicializa el objeto hotel
        """
        self.id = __id
        self.name = name
        self.rooms = rooms

    def display_info(self):
        """
        Imprime la información
        """
        print(f"Hotel ID: {self.id}, Name: {self.name}, Rooms: {self.rooms}")

    def modify_info(self, name=None, rooms=None):
        """
        Editamos la informacion del hotel
        """
        if name:
            self.name = name
        if rooms:
            self.rooms = rooms

    def check_room_availability(self, room_number):
        """
        Revisa la disponibilidad de una habitación.
        """
        return self.rooms.get(room_number, False)

    def reserve_room(self, room_number):
        """
        Reserva una habitación si esta disponible
        """
        if self.check_room_availability(room_number):
            self.rooms[room_number] = False
            return True
        return False

    def cancel_reservation(self, room_number):
        """
        Cancela una resevacion
        """
        if room_number in self.rooms and not self.rooms[room_number]:
            self.rooms[room_number] = True
            return True
        return False
