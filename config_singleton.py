class Configuracion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.datos = {
                "idioma": "español",
                "tema": "claro",
                "volumen": 50
            }
        return cls._instancia

    def set(self, clave, valor):
        self.datos[clave] = valor

    def get(self, clave):
        return self.datos.get(clave, "No encontrado")

    def mostrar_todo(self):
        return self.datos
