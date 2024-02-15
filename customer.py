"""Archivo con codigo para los clientes"""


class Customer:
    """Clase para objeto customer"""

    def __init__(self, id__, name, email):
        """
        Inicializa un cliente
        """
        self.id = id__
        self.name = name
        self.email = email

    def display_info(self):
        """
        Imprime la informacion del cliente
        """
        print(
            f"Customer ID: {self.id}, "
            f"Name: {self.name}, "
            f"Email: {self.email}"
        )

    def modify_info(self, name=None, email=None):
        """
        Editamos al clienete
        """
        if name:
            self.name = name
        if email:
            self.email = email
