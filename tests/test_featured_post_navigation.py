import allure
import pytest

@pytest.mark.navigation
@pytest.mark.smoke
@allure.epic('Blog E2E Tests')
@allure.feature('Post Navigation')
@allure.story('Featured Post Flow')
@allure.severity(allure.severity_level.CRITICAL)
def test_user_can_read_featured_post(navigation_scenario, home_page_scenario, post_page_scenario):
  """
  Verifica que el usuario puede navegar al post destacado desde Home, y que los datos del post coinciden.

  Dado que el usuario está en la página Home
  Y el post destacado está visible
  Cuando el usuario hace click en el título del post destacado
  Entonces el usuario es llevado a la página del post destacado
  Y el título, resumen y fecha del post coinciden con los datos mostrados en la página Home.
  """

  # Arrange
  with allure.step("Navegar a la página Home"):
    navigation_scenario.navigate_to_home()
    assert home_page_scenario.verify_home_loaded(), "La página Home no cargó correctamente."

  with allure.step("Verificar que el post destacado está visible"):
    assert home_page_scenario.verify_featured_post_is_shown(), "El post destacado no está visible en Home."

  # Act
  with allure.step("Obtener datos del post destacado"):
    featured_post_data = home_page_scenario.get_featured_post_data()

    # Attach data to Allure report
    allure.attach(
      f"Title: {featured_post_data['title']}\n"
      f"Date: {featured_post_data['date']}\n"
      f"Summary: {featured_post_data['summary']}",
      name="Featured Post Data (Home Page)",
      attachment_type=allure.attachment_type.TEXT
    )

  with allure.step("Hacer click en el post destacado"):
    home_page_scenario.open_featured_post()

  # Assert
  with allure.step("Verificar que la página del post cargó correctamente"):
    assert post_page_scenario.verify_post_page_loaded(), "La página del post no cargó correctamente."

  with allure.step("Verificar que los datos del post coinciden"):
    post_title = post_page_scenario.get_post_title()
    post_date = post_page_scenario.get_publication_date()
    post_summary = post_page_scenario.get_post_summary()

    # Attach data to Allure report
    allure.attach(
      f"Title: {post_title}\n"
      f"Date: {post_date}\n"
      f"Summary: {post_summary}",
      name="Post Data (Post Page)",
      attachment_type=allure.attachment_type.TEXT
    )

    assert post_title == featured_post_data['title'], \
    f"Título no coincide. Esperado: {featured_post_data['title']}, Obtenido: {post_title}"
    assert post_date == featured_post_data['date'], \
    f"Fecha no coincide. Esperado: {featured_post_data['date']}, Obtenido: {post_date}"
    assert post_summary == featured_post_data['summary'], \
    f"Resumen no coincide. Esperado: {featured_post_data['summary']}, Obtenido: {post_summary}"