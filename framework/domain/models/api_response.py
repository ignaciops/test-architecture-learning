from dataclasses import dataclass
from typing import Any

@dataclass
class ApiResponse:
  """
  Modelo que representa la respuesta de una API.
  """
  status_code: int
  headers: dict[str, str]
  json_body: Any = None
  text_body: str = ""
  elapsed_time: float = 0.0

  @property
  def is_ok(self) -> bool:
    """
    Indica si la respuesta fue exitosa (status code 2xx).

    Returns:
        bool: True si la respuesta es exitosa, False en caso contrario.
    """
    return 200 <= self.status_code < 300