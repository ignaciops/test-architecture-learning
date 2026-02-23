from framework.adapters.api.endpoints.users_endpoints import UsersEndpoints
from framework.domain.models.api_response import ApiResponse
from framework.domain.ports.api_port import ApiPort

class UsersScenario:
  """
  Escenario para interactuar con la API de usuarios.
  """

  def __init__(self, api_port: ApiPort):
    self._api = api_port
    self._users = UsersEndpoints

  def list_users(self) -> ApiResponse:
    response = self._api.get(self._users.BASE)
    return response

  def create_user(self, user_data: dict) -> ApiResponse:
    response = self._api.post(self._users.BASE, body=user_data)
    return response

  def get_user(self, user_id: int) -> ApiResponse:
    response = self._api.get(self._users.BY_ID.format(user_id=user_id))
    return response

  def get_user_badges(self, user_id: int) -> ApiResponse:
    response = self._api.get(self._users.BADGES.format(user_id=user_id))
    return response

  def update_user(self, user_id: int, user_data: dict) -> ApiResponse:
    response = self._api.patch(self._users.BY_ID.format(user_id=user_id), body=user_data)
    return response

  def delete_user(self, user_id: int) -> ApiResponse:
    response = self._api.delete(self._users.BY_ID.format(user_id=user_id))
    return response

