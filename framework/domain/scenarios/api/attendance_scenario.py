from framework.adapters.api.endpoints.attendace_endpoints import AttendancesEndpoints
from framework.domain.models.api_response import ApiResponse
from framework.domain.ports.api_port import ApiPort

class AttendancesScenario:
  """
  Escenario para interactuar con la API de attendances.
  """

  def __init__(self, api_port: ApiPort):
    self._api = api_port
    self._attendances = AttendancesEndpoints

  def register_attendance(self, attendance_data: dict) -> ApiResponse:
    response = self._api.post(self._attendances.BASE, body=attendance_data)
    return response
