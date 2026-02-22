import httpx
from typing import Any
from framework.domain.models.api_response import ApiResponse
from framework.domain.ports.api_port import ApiPort

class HttpxApiAdapter(ApiPort):
  """
  Implementación de ApiPort usando Httpx.
  """

  def __init__(self, base_url: str, headers: dict[str, str] | None = None):
    self._base_url = base_url
    self._headers = headers or {'Content-Type': 'application/json'}

  # Métodos para ApiResponse
  def _to_api_response(self, response: httpx.Response) -> ApiResponse:
    json_body = None
    try:
      json_body = response.json()
    except Exception:
      pass

    return ApiResponse(
      status_code=response.status_code,
      headers=dict(response.headers),
      json_body=json_body,
      text_body=response.text,
      elapsed_time=response.elapsed.total_seconds() * 1000,
    )

  def get(self, endpoint: str, params: dict[str, Any] | None = None) -> ApiResponse:
    response = httpx.get(
      f"{self._base_url}{endpoint}",
      params=params,
      headers=self._headers,
    )
    return self._to_api_response(response)

  def post(self, endpoint: str, body: dict[str, Any] | None = None) -> ApiResponse:
    response = httpx.post(
      f"{self._base_url}{endpoint}",
      json=body,
      headers=self._headers,
    )
    return self._to_api_response(response)

  def put(self, endpoint: str, body: dict[str, Any] | None = None) -> ApiResponse:
    response = httpx.put(
      f"{self._base_url}{endpoint}",
      json=body,
      headers=self._headers,
    )
    return self._to_api_response(response)

  def patch(self, endpoint: str, body: dict[str, Any] | None = None) -> ApiResponse:
    response = httpx.patch(
      f"{self._base_url}{endpoint}",
      json=body,
      headers=self._headers,
    )
    return self._to_api_response(response)

  def delete(self, endpoint: str) -> ApiResponse:
    response = httpx.delete(
      f"{self._base_url}{endpoint}",
      headers=self._headers,
    )
    return self._to_api_response(response)
