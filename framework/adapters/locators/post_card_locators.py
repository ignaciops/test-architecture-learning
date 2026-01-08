class PostCardLocators:
    """
    Locators para el componente PostCard usado en:
    - Home: Sección de Recent Posts
    - Blog: Listado completo de posts

    NO incluye Featured Post (tiene su propia estructura).
    NO incluye metadatos (están en PostMetadataLocators).
    """

    # Container principal
    postCardContainer = "[data-testid='post-card']"

    # Elementos específicos del card
    postCardTitle = "[data-testid='post-card-title']"
    postCardSummary = "[data-testid='post-card-summary']"
    postCardReadMore = "[data-testid='post-card-read-more']"

    # Nota: post-meta, post-date, reading-time, tag-list vienen de PostMetadataLocators