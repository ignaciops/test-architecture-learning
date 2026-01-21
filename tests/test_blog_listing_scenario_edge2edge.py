import pytest
from framework.scenarios.blog_listing_scenario import BlogListingScenario
from framework.adapters.locators.post_card_locators import PostCardLocators

class TestBlogListingScenarioEdge2Edge:
  """
  Tests edge-to-edge de BlogListingScneario usando FakeBrowserAdapter.

  Estos tests verifican LOGICA del scenario sin abrir navegador.
  Objetivo: Probar edge cases y validaciones del scenario.
  """

  def test_get_post_count_with_complete_posts(
      self,
      blog_listing_scenario_with_fake
  ):
    """
    Verifica que get_post_count funciona con posts completos.
    """
    scenario, fake_browser = blog_listing_scenario_with_fake

    # Act
    count = scenario.get_post_count()

    # Assert
    assert count == 3
    assert fake_browser.get_call_count("get_element_count")

  def test_get_post_count_with_empty_blog(
      self,
      fake_browser_empty
  ):
    """
    Verifica comportamiento con blog sin posts.
    """
    blog_listing = BlogListingScenario(fake_browser_empty)

    # Act
    count = blog_listing.get_post_count()

    # Assert
    assert count == 0

  def test_get_post_metadata_with_valid_index(
      self,
      fake_browser_with_complete_posts
  ):
    """
    Verifica obtencion de metadata con indice valido.
    """
    blog_listing = BlogListingScenario(fake_browser_with_complete_posts)

    # Act
    metadata = blog_listing.get_post_metadata(0)

    # Assert
    assert metadata["title"] == "Post 1: Architecture Patterns"
    assert metadata["date"] == "2026-01-15"
    assert metadata["readingTime"] == "5 min"

  def test_get_post_metadata_with_invalid_index_raises_error(
      self,
      fake_browser_with_complete_posts
  ):
    """
    Verifica que indice invalido lanza error.
    """
    blog_listing = BlogListingScenario(fake_browser_with_complete_posts)

    # Act / Assert
    with pytest.raises(IndexError) as exc_info:
      blog_listing.get_post_metadata(10)

    assert "out of range" in str(exc_info.value).lower()

  def test_verify_all_posts_have_metadata_with_incomplete_posts(
      self,
      fake_browser_with_incomplete_metadata
  ):
    """
    Verifica deteccion de metadata incompleta
    """
    blog_listing = BlogListingScenario(fake_browser_with_incomplete_metadata)

    # Act
    has_complete_metadata = blog_listing.verify_all_posts_have_metadata()

    # Assert
    assert has_complete_metadata is False

  def test_open_post_by_index_with_valid_index(
      self,
      blog_listing_scenario_with_fake
  ):
    """
    Verifica que open_post_by_index hace click correctamente.
    """
    scenario, fake_browser = blog_listing_scenario_with_fake

    # Act
    scenario.open_post_by_index(1)

    # Assert
    # Verificar que se hizo click en el segundo post
    expected_locator = f"{PostCardLocators.postCardContainer} >> nth=1 >> {PostCardLocators.postCardTitle}"
    fake_browser.assert_clicked(expected_locator)
