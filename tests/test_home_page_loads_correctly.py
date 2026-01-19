import allure
import pytest

@pytest.mark.home
@pytest.mark.smoke
@allure.epic('Blog E2E Tests')
@allure.feature('Home Page')
@allure.story('Page Load and Components')
@allure.severity(allure.severity_level.CRITICAL)
def test_home_page_displays_all_sections(navigation_scenario, home_page_scenario):
  """
  Verifica que la página home carga correctamente y muestra todas las secciones principales.

  Dado que el usuario navega a la página Home
  Entonces la página Home carga correctamente
  Y la hero section, footer, navbar, featured post y recent posts son visibles.
  """

  # Arrange / Act
  with allure.step("Navegar a la página Home"):
    navigation_scenario.navigate_to_home()

  # Assert
  with allure.step("Verificar que la página Home cargó correctamente"):
    assert home_page_scenario.verify_home_loaded(), "La página Home no cargó correctamente."

  with allure.step("Verificar que la navbar está visible"):
    assert home_page_scenario.verify_navbar_is_visible(), "La navbar no está visible en la página Home."

  with allure.step("Verificar que la hero section está visible"):
    assert home_page_scenario.verify_hero_section_loaded(), "La hero section no está visible en la página Home."

  with allure.step("Verificar que el footer está visible"):
    assert home_page_scenario.verify_footer_loaded(), "El footer no está visible en la página Home."

  with allure.step("Verificar que el post destacado está visible"):
    assert home_page_scenario.verify_featured_post_is_shown(), "El post destacado no está visible en la página Home."

  with allure.step("Verificar que los posts recientes están visibles"):
    assert home_page_scenario.verify_recent_posts_are_listed(), "Los posts recientes no están visibles en la página Home."

