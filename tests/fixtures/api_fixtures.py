import pytest
from framework.adapters.api.httpx_api_adapter import HttpxApiAdapter
from framework.domain.ports.api_port import ApiPort
from framework.infrastructure.config import Config
from framework.domain.scenarios.api.users_scenario import UsersScenario
from framework.domain.scenarios.api.attendance_scenario import AttendancesScenario
from framework.domain.scenarios.api.badge_awarding_scenario import BadgeAwardingScenario
from framework.domain.scenarios.api.badges_scenario import BadgesScenario


@pytest.fixture
def api_adapter() -> ApiPort:
  return HttpxApiAdapter(base_url=Config.API_BASE_URL)

@pytest.fixture
def users_scenario(api_adapter) -> UsersScenario:
  return UsersScenario(api_adapter)

@pytest.fixture
def attendance_scenario(api_adapter) -> AttendancesScenario:
  return AttendancesScenario(api_adapter)

@pytest.fixture
def badges_scenario(api_adapter) -> BadgesScenario:
  return BadgesScenario(api_adapter)

@pytest.fixture
def badge_awarding_scenario(api_adapter, users_scenario, attendance_scenario) -> BadgeAwardingScenario:
  return BadgeAwardingScenario(api_adapter, users_scenario, attendance_scenario)

@pytest.fixture(scope="session")
def session_api_adapter() -> ApiPort:
  return HttpxApiAdapter(base_url=Config.API_BASE_URL)

@pytest.fixture(scope="session")
def gold_badge_created(session_api_adapter: ApiPort) -> None:
  scenario = BadgesScenario(session_api_adapter)
  badge_data = {
    "name": "Oro",
    "description": "Asistió al menos a 10 eventos",
    "criteria": {"type": "attendance_count", "threshold": 10}
  }
  scenario.create_badge(badge_data)