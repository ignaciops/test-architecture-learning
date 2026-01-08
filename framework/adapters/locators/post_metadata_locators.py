class PostMetadataLocators:
    """
    Locators para metadatos de posts que son GENÉRICOS y se reutilizan
    en TODOS los contextos:
    - Home (featured post)
    - Home (recent posts)
    - Blog Listing
    - Post Detail

    Estos data-testid NO tienen prefijos porque el HTML los usa de forma genérica.
    """

    # Container de metadatos
    postMetaContainer = "[data-testid='post-meta']"

    # Elementos individuales de metadata
    postDate = "[data-testid='post-date']"
    postReadTime = "[data-testid='reading-time']"

    # Tags
    postTagList = "[data-testid='tag-list']"
    # Para tags individuales, usa un selector que acepte cualquier nombre
    # Ejemplo: page.locator("[data-testid^='tag-']")
    postTagPrefix = "[data-testid^='tag-']"  # Matches tag-python, tag-testing, etc.