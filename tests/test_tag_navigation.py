import allure
import pytest

@pytest.mark.parametrize("post_index", [0, 2, 4])
@allure.epic("Blog E2E Tests")
@allure.story("Tag Navigation Flow")
@allure.feature("Tag Navigation")
def test_user_can_filter_posts_by_tag_from_card(blog_listing_page_loaded, tag_page_scenario, post_index):
  """
  Verifica que el usuario puede filtrar posts por tag desde post card.

  Este test se ejecuta con múltiples índices de posts (0, 2, 4)
  para validar que la funcionalidad de tags funciona consistentemente.

  Dado que el usuario está en la página Blog
  Cuando hace click en un tag de un post card
  Entonces navega a la página de ese tag (/tags/{tag}/)
  Y los posts mostrados contienen ese tag.
  """
  blog_listing = blog_listing_page_loaded

  # Act
  with allure.step(f"Obtener primer tag del post en el índice {post_index}"):
    post_tags = blog_listing.get_post_tags(post_index)

    assert len(post_tags) > 0, \
      f"Post con índice {post_index} no tiene tags."

    selected_tag = post_tags[0]
    allure.attach(
      f"Post index: {post_index}\nSelected tag: {selected_tag}",
      name="Test Parameters",
      attachment_type=allure.attachment_type.TEXT
    )

  with allure.step(f"Click en tag '{selected_tag}'"):
    blog_listing.click_tag(
      selected_tag,
      post_index
    )

  # Assert
  with allure.step(f"Verificar navegación a página de tag '{selected_tag}'"):
    assert tag_page_scenario.verify_tag_page_loaded(selected_tag), \
      f"No se navegó a la página del tag '{selected_tag}'."