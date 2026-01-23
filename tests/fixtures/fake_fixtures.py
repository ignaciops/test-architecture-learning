import pytest
from framework.adapters.fake.fake_browser_adapter import FakeBrowserAdapter
from framework.adapters.locators.common_locators import CommonLocators
from framework.adapters.locators.blog_page_locators import BlogPageLocators
from framework.adapters.locators.post_card_locators import PostCardLocators
from framework.scenarios.blog_listing_scenario import BlogListingScenario

# Fixtures para FakeBrowserAdapter
@pytest.fixture
def fake_browser_with_complete_posts():
  """
  FakeBrowserAdapter con blog listing completo
  3 posts con metadata completa.
  """
  dom_state = {
    CommonLocators.navbarBlogLink: {
      "text": "Blog",
      "visible": True
    },

    # Blog page
    BlogPageLocators.blogPageTitle: {
      "text": "Blog",
      "visible": True
    },
    PostCardLocators.postCardContainer: {
      "count":3,
      "visible": True
    },

    # Datos estructurados
    f"structured_data:{PostCardLocators.postCardContainer}": [
            {
                "title": "Post 1: Architecture Patterns",
                "date": "2026-01-15",
                "summary": "Learning hexagonal architecture",
                "readingTime": "5 min"
            },
            {
                "title": "Post 2: Testing Strategy",
                "date": "2026-01-10",
                "summary": "Defining test approach",
                "readingTime": "7 min"
            },
            {
                "title": "Post 3: Playwright Tips",
                "date": "2026-01-05",
                "summary": "Advanced Playwright techniques",
                "readingTime": "6 min"
            }
    ],

  }
  return FakeBrowserAdapter(dom_state)

@pytest.fixture
def blog_listing_scenario_with_fake(fake_browser_with_complete_posts):
  """
  Fixture que devuelve tupla (scenario, fake_browser)
  """

  scenario = BlogListingScenario(fake_browser_with_complete_posts)
  return scenario, fake_browser_with_complete_posts

@pytest.fixture
def fake_browser_with_incomplete_metadata():
    """
    FakeBrowserAdapter con posts que tienen metadata incompleta.
    """
    dom_state = {
        BlogPageLocators.blogPageTitle: {
            "text": "Blog",
            "visible": True
        },

        PostCardLocators.postCardContainer: {
          "count": 2,
          "visible": True
        },

        f"structured_data:{PostCardLocators.postCardContainer}": [
            {
                "title": "Post sin fecha",
                "date": "",  # ← FALTA fecha
                "summary": "Some summary",
                "readingTime": "5 min"
            },
            {
                "title": "Post sin reading time",
                "date": "2026-01-15",
                "summary": "Another summary",
                "readingTime": ""  # ← FALTA reading time
            }
        ]
    }

    return FakeBrowserAdapter(dom_state)

@pytest.fixture
def fake_browser_empty():
    """
    FakeBrowserAdapter sin posts (blog vacío).
    """
    dom_state = {
        BlogPageLocators.blogPageTitle: {
            "text": "Blog",
            "visible": True
        },
        PostCardLocators.postCardContainer: {
          "count": 0,
          "visible": True
        },
        f"structured_data:{PostCardLocators.postCardContainer}": []
        # No hay post cards
    }

    return FakeBrowserAdapter(dom_state)

@pytest.fixture
def fake_browser_mobile() -> FakeBrowserAdapter:
    """Fake browser adapter configurado para mobile viewport."""
    return FakeBrowserAdapter(is_mobile=True)

@pytest.fixture
def fake_browser_desktop() -> FakeBrowserAdapter:
    """Fake browser adapter configurado para desktop viewport."""
    return FakeBrowserAdapter(is_mobile=False)