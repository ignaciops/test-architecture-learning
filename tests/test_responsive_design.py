import pytest
import allure

@pytest.mark.mobile
@allure.epic("Responsive Design")
@allure.feature("Mobile Home Page")
def test_mobile_home_page_shows_elements(
  mobile_navigation_scenario,
  mobile_home_page_scenario):
  """
  Verifica que home page carga correctamenteen mobile.

  """
  with allure.step("Navegar a home"):
    mobile_navigation_scenario.navigate_to_home()

  with allure.step("Verificar componentes principales"):
    assert mobile_home_page_scenario.verify_home_loaded()
    assert mobile_home_page_scenario.verify_hero_section_loaded()
    assert mobile_home_page_scenario.verify_featured_post_is_shown()


