import random
import string

class GeneradorContrasena:
    def generar(self, longitud):
        if longitud < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres")
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(longitud))
