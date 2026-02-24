from framework.domain.scenarios.api.users_scenario import UsersScenario
from framework.domain.scenarios.api.attendance_scenario import AttendancesScenario
from framework.domain.models.api_response import ApiResponse
from framework.domain.ports.api_port import ApiPort


class BadgeAwardingScenario:

   def __init__(
      self,
      api_port: ApiPort,
      users_scenario: UsersScenario,
      attendance_scenario: AttendancesScenario
    ):
      self._api = api_port
      self._users = users_scenario
      self._attendance = attendance_scenario

   def create_user_with_attendances(self, user_data: dict, event_ids: list[int]) -> int:
      user_response = self._users.create_user(user_data)
      user_id = user_response.json_body["id"]

      for event_id in event_ids:
         self._attendance.register_attendance({
            "user_id": user_id,
            "event_id": event_id
         })

      return user_id

   def register_attendance(self, user_id: int, event_id: int) -> ApiResponse:
      return self._attendance.register_attendance({
         "user_id": user_id,
         "event_id": event_id
      })

   def user_has_badge(self, user_id: int, badge_name: str) -> bool:
      response = self._users.get_user_badges(user_id)
      badges = response.json_body["badges"]
      return any(entry["badge"]["name"] == badge_name for entry in badges)


