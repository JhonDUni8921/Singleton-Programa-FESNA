# 🛠️ Panel de Configuración con Patrón Singleton (Python)

Este proyecto es una demostración práctica del **patrón de diseño Singleton** en Python. Simula un **gestor de configuración** que mantiene una única instancia accesible desde cualquier parte del programa.

---

## 📌 ¿Qué hace este programa?

Permite al usuario:

- Ver la configuración actual (idioma, tema y volumen).
- Modificar esos valores desde una consola interactiva.
- Mantener la configuración centralizada usando el patrón Singleton.

---

## 🧱 Estructura del proyecto

panel_config/
├── config_singleton.py # Clase Singleton que maneja los datos de configuración
├── menu.py # Menú en consola para interactuar con la configuración
└── main.py # Punto de entrada del programa
