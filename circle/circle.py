class Circle:
    def __init__(self, radius):
        """
        Inicializa un círculo con el radio dado.
        Lanza ValueError si el radio es <= 0.
        """
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius

    def get_radius(self):
        """
        Retorna el radio del círculo.
        """
        return self.radius

    def set_radius(self, radius):
        """
        Establece un nuevo radio para el círculo.
        Lanza ValueError si el radio es <= 0.
        """
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius
