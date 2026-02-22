# framework/ports/api_port.py
from abc import ABC, abstractmethod
from typing import Any
from framework.domain.models.api_response import ApiResponse

class ApiPort(ABC):
  """
  Interfaz que define operaciones básicas para interactuar con APIs.
  """

  @abstractmethod
  def get(self, endpoint: str, params: dict[str, Any] | None = None) -> ApiResponse:
    """
    Realiza una solicitud GET a un endpoint específico.

    Args:
        endpoint (str): URL o ruta del endpoint.
        params (dict[str, Any], optional): Parámetros de consulta para la solicitud.
    Returns:
        ApiResponse: Respuesta de la API como un objeto ApiResponse.

    """
    pass

  @abstractmethod
  def post(self, endpoint: str, body: dict[str, Any]) -> ApiResponse:
    """
    Realiza una solicitud POST a un endpoint específico.

    Args:
        endpoint (str): URL o ruta del endpoint.
        body (dict[str, Any]): Cuerpo de la solicitud.
    Returns:
        ApiResponse: Respuesta de la API como un objeto ApiResponse.

    """
    pass

  @abstractmethod
  def put(self, endpoint: str, body: dict[str, Any]) -> ApiResponse:
    """
    Realiza una solicitud PUT a un endpoint específico.

    Args:
        endpoint (str): URL o ruta del endpoint.
        body (dict[str, Any]): Cuerpo de la solicitud.
    Returns:
        ApiResponse: Respuesta de la API como un objeto ApiResponse .

    """
    pass

  @abstractmethod
  def patch(self, endpoint: str, body: dict[str, Any]) -> ApiResponse:
    """
    Realiza una solicitud PATCH a un endpoint específico.

    Args:
        endpoint (str): URL o ruta del endpoint.
        body (dict[str, Any]): Cuerpo de la solicitud.
    Returns:
        ApiResponse: Respuesta de la API como un objeto ApiResponse.

    """
    pass

  @abstractmethod
  def delete(self, endpoint: str) -> ApiResponse:
    """
    Realiza una solicitud DELETE a un endpoint específico.

    Args:
        endpoint (str): URL o ruta del endpoint.
    Returns:
        ApiResponse: Respuesta de la API como un objeto ApiResponse.

    """
    pass