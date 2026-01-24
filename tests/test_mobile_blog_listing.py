import allure
import pytest

@pytest.mark.mobile
@allure.epic("Responsive Design")
@allure.feature("Mobile Blog Listing Page")
class TestBlogListing:

  @allure.story("Post Cards Display")
  @allure.title("Los post cards se muestran correctamente en la página de listado de blog")
  def test_mobile_blog_listing_displays(self, mobile_navigation_scenario, mobile_blog_listing_scenario):
    """
    Verifica que los post cards se muestran correctamente un la paágina de blog.
    Dado que el usuario está en la página de listado de blog
    Y usa un dispositivo movil.
    Cuando la página carga completamente.
    Entonces todos los post cards se muestran con título.
    """
    with allure.step("Navegar a Home"):
      mobile_navigation_scenario.navigate_to_home()
    with allure.step("Navegar a la Blog page"):
      mobile_navigation_scenario.navigate_to_blog()

    # Act
    with allure.step("Obtener todos los títulos de los posts"):
      post_titles = mobile_blog_listing_scenario.get_all_post_titles()
      posts_count = mobile_blog_listing_scenario.get_post_count()

      allure.attach(
        f"Posts count: {posts_count}",
        name="Posts Count",
        attachment_type=allure.attachment_type.TEXT
      )

    # Assert
    with allure.step("Verificar que todos los post cards se muestran con título"):
      assert posts_count > 0, f"No se encontraron posts en la página de listado de blog. Encontrados: {posts_count}"

    with allure.step("Verificar que la cantidad de títulos obtenidos coincide con la cantidad de posts"):
      assert len(post_titles) == posts_count, \
      f"La cantidad de títulos obtenidos ({len(post_titles)}) no coincide con la cantidad de posts ({posts_count})."

    with allure.step("Verificar que todos los títulos de los posts no están vacíos"):
      empty_titles = [i for i, title in enumerate(post_titles) if not title.strip()]
      assert not empty_titles, \
      f"Los siguientes posts tienen títulos vacíos: {empty_titles}"

  @allure.story("Post Navigation")
  @allure.title("El usuario puede navegar a un post específico desde la página de listado de blog")
  def test_mobile_user_can_navigate_to_specific_post(
    self,
    mobile_navigation_scenario,
    mobile_blog_listing_scenario,
    mobile_post_page_scenario):
    """
    Verifica que el usuario puede navegar a un post específico desde la página de listado de blog.

    Dado que el usuario está en la página de listado de blog
    Y usa un dispositivo móvil.
    Cuando el usuario hace click en el título del primer post.
    Entonces el usuario es llevado a la página del post.
    """

    with allure.step("Navegar a Home"):
      mobile_navigation_scenario.navigate_to_home()
    with allure.step("Navegar a la Blog page"):
      mobile_navigation_scenario.navigate_to_blog()

    # Act
    with allure.step("Obtener el título del primer post"):
      expected_title = mobile_blog_listing_scenario.get_all_post_titles()[0]
      allure.attach(
        expected_title,
        name="Expected Post Title",
        attachment_type=allure.attachment_type.TEXT
      )

    with allure.step("Hacer click en el título del primer post"):
      mobile_blog_listing_scenario.open_post_by_index(0)

    # Assert
    with allure.step("Verificar que la página del post cargó correctamente"):
      assert mobile_post_page_scenario.verify_post_page_loaded(), "La página del post no cargó correctamente."

    with allure.step("Verificar que se abrió el post correcto"):
      actual_title = mobile_post_page_scenario.get_post_title()
      allure.attach(
        actual_title,
        name="Actual Post Title",
        attachment_type=allure.attachment_type.TEXT
      )

      assert actual_title == expected_title, \
      f"Se abrió el post incorrecto. Esperado: {expected_title}, Obtenido: {actual_title}"

  @allure.story("Post Metadata Verification")
  @allure.title("Todos los posts en la página de listado de blog tienen los metadatos completos")
  def test_mobile_all_posts_have_metadata(self, mobile_blog_listing_page_loaded):
    """
    Verifica que todos los posts en la página de listado de blog tienen los metadatos completos.
    Los metadatos a verificar son: Título, Fecha, Resumen y Tiempo de lectura.

    Dado que el usuario está en la página de listado de blog.
    Y usa un dispositivo móvil.
    Cuando la página carga completamente.
    Entonces todos los posts tienen los metadatos completos.
    """
    blog_listing = mobile_blog_listing_page_loaded
    # Act & Assert
    with allure.step("Verificar que todos los posts tienen los metadatos completos"):
      has_complete_metadata = blog_listing.verify_all_posts_have_metadata()

      if not has_complete_metadata:
        posts_count = blog_listing.get_post_count()
        incomplete_posts = []

        for i in range(posts_count):
          metadata = blog_listing.get_post_metadata(i)
          missing_fields = []

          if not metadata.get("title"):
            missing_fields.append("title")
          if not metadata.get("date"):
            missing_fields.append("date")
          if not metadata.get("summary"):
            missing_fields.append("summary")
          if not metadata.get("readingTime"):
            missing_fields.append("readingTime")

          if missing_fields:
            incomplete_posts.append(f"Post {i}: missing fields: {', '.join(missing_fields)}")

        allure.attach(
          "\n".join(incomplete_posts),
          name="Incomplete Posts Metadata",
          attachment_type=allure.attachment_type.TEXT
        )

        assert False, \
        f"Algunos posts no tienen metadatos completos:\n" + "\n".join(incomplete_posts)

      assert has_complete_metadata, "Validación fallida: Algunos posts no tienen metadatos completos."