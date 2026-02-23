from framework.adapters.api.endpoints.badges_endpoints import BadgesEndpoints
from framework.domain.models.api_response import ApiResponse
from framework.domain.ports.api_port import ApiPort

class BadgesScenario:
  """
  Escenario para interactuar con la API de badges.
  """

  def __init__(self, api_port: ApiPort):
    self._api = api_port
    self._badges = BadgesEndpoints

  def list_badges(self) -> ApiResponse:
    response = self._api.get(self._badges.BASE)
    return response

  def create_badge(self, badge_data: dict) -> ApiResponse:
    response = self._api.post(self._badges.BASE, body=badge_data)
    return response

  def get_badge(self, badge_id: int) -> ApiResponse:
    response = self._api.get(self._badges.BY_ID.format(badge_id=badge_id))
    return response

  def update_badge(self, badge_id: int, badge_data: dict) -> ApiResponse:
    response = self._api.patch(self._badges.BY_ID.format(badge_id=badge_id), body=badge_data)
    return response
