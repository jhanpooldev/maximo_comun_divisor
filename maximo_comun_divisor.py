class MCD:
    """
    Clase que representa el cálculo del Máximo Común Divisor (MCD) de dos números.
    """

    def __init__(self, num1, num2):
        """
        Constructor de la clase MCD.

        Args:
        num1 (int): El primer número entero positivo.
        num2 (int): El segundo número entero positivo.
        """
        self.setternumero1(num1)
        self.setternumero2(num2)

    def setternumero1(self, num1):
        """
        Setter para el primer número.

        Args:
        num1 (int): El primer número entero positivo.
        """
        if num1 <= 0:
            raise ValueError("El número debe ser entero y positivo.")
        self.num1 = num1

    def getternumero1(self):
        """
        Getter para el primer número.

        Returns:
        int: El primer número.
        """
        return self.num1

    def setternumero2(self, num2):
        """
        Setter para el segundo número.

        Args:
        num2 (int): El segundo número entero positivo.
        """
        if num2 <= 0:
            raise ValueError("El número debe ser entero y positivo.")
        self.num2 = num2

    def getternumero2(self):
        """
        Getter para el segundo número.

        Returns:
        int: El segundo número.
        """
        return self.num2

    def calcular_mcd(self):
        """
        Calcula el Máximo Común Divisor (MCD) de los dos números usando el algoritmo de Euclides.

        Returns:
        int: El MCD de num1 y num2.
        """
        a, b = self.num1, self.num2
        while b != 0:
            a, b = b, a % b
        return a


def solicitar_numero(mensaje):
    """
    Solicita un número entero positivo y lo valida.

    Args:
    mensaje (str): El mensaje que se muestra al solicitar la entrada.

    Returns:
    int: El número entero positivo ingresado por el usuario.
    """
    while True:
        try:
            num = int(input(mensaje))
            if num <= 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                return num
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


# Solicitar números al usuario
num1 = solicitar_numero("Ingrese el primer número entero positivo: ")
num2 = solicitar_numero("Ingrese el segundo número entero positivo: ")

# Crear una instancia de la clase MCD
mcd_obj = MCD(num1, num2)

# Calcular y mostrar el MCD
print(f"El Máximo Común Divisor de {mcd_obj.getternumero1()} y {mcd_obj.getternumero2()} es: {mcd_obj.calcular_mcd()}")
