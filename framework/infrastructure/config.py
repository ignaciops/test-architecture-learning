"""
Configuración central del framework de pruebas.
"""
import os

class Config:
  """
  Clase de configuración para parámetros globales del framework.
  Conforme vaya creciendo el framework, se agregarán más configuraciones aquí.
  """

  BASE_URL = os.getenv("BASE_URL", "https://ignaciops.dev")
  API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/")