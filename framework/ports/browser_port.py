# framework/ports/browser_port.py
from abc import ABC, abstractmethod
from typing import Optional

class BrowserPort(ABC):
    """
    Interface que define operaciones de navegación web.

    Análogo a una interface de TypeScript:
    interface BrowserPort {
      navigateTo(url: string): void;
      click(locator: string): void;
      getText(locator: string): string;
    }
    """
    # Navegación básica
    @abstractmethod
    def navigate_to(self, url: str) -> None:
        """Navegar a una URL"""
        pass

    @abstractmethod
    def wait_for_load_state(self, state: str = "networkidle") -> None:
        """Espera hasta que la página alcance el estado de carga especificado."""
        pass

    # Interacciones con un elemento
    @abstractmethod
    def click(self, locator: str) -> None:
        """Hacer click en un elemento"""
        pass

    @abstractmethod
    def get_text(self, locator: str) -> str:
        """Obtener texto de un elemento"""
        pass

    @abstractmethod
    def is_visible(self, locator: str) -> bool:
        """Verificar si elemento es visible"""
        pass

    @abstractmethod
    def wait_for_element(self, locator: str, timeout: int = 10000) -> None:
        """Espera hasta que el elemento sea visible o hasta que se agote el tiempo de espera."""
        pass

    # Interacciones con múltiples elementos
    @abstractmethod
    def get_all_texts(self, locator: str) -> list[str]:
        """Obtiene el texto de todos los elementos que coinciden con el locator dado."""
        pass

    @abstractmethod
    def get_element_count(self, locator: str) -> int:
        """Regresa la cantidad de elementos que coinciden con el locator dado."""
        pass

    # Operaciones con elementos anidados
    @abstractmethod
    def get_text_from_nested(
        self,
        parent_locator: str,
        child_locator: str,
        parent_index: int = 0
    ) -> str:
        """
        Obtiene el texto de un elemento hijo dentro de un elemento padre específico.

        Args:
            parent_locator (str): Locator del elemento padre.
            child_locator (str): Locator del elemento hijo.
            parent_index (int): Índice del elemento padre si hay múltiples coincidencias.

        Returns:
            str: Texto del elemento hijo.
        """
        pass

    @abstractmethod
    def click_nested(
        self,
        parent_locator: str,
        child_locator: str,
        parent_index: int = 0
    ) -> None:
        """
        Hace click en un elemento hijo dentro de un elemento padre específico.

        Args:
            parent_locator (str): Locator del elemento padre.
            child_locator (str): Locator del elemento hijo.
            parent_index (int): Índice del elemento padre si hay múltiples coincidencias.
        """
        pass

    @abstractmethod
    def get_all_nested_texts(
        self,
        parent_locator: str,
        child_locator: str
    ) -> list[str]:
        """
        Obtiene el texto de todos los elementos hijos dentro de los elementos padre que coinciden.

        Args:
            parent_locator (str): Locator del elemento padre.
            child_locator (str): Locator del elemento hijo.

        Returns:
            list[str]: Lista de textos de los elementos hijos.
        """
        pass

    @abstractmethod
    def get_structured_data(
        self,
        parent_locator: str,
        field_selectors: dict[str, str]
    ) -> list[dict[str, str]]:
        """
        Obtiene datos extructurados de componentes repetitivos.

        Por cada elemento padre, extrae multiples campos basados en los selectores proporcionados.

        Args:
            parent_locator (str): Locator del elemento padre.
            field_selectors (dict[str, str]): Diccionario donde la clave es el nombre del campo

        Returns:
            list[dict[str, str]]: Lista de diccionarios con los datos extraídos.

        Ejemplo:
            posts_data = browser.get_structured_data(
                parent_locator="[data-testid='post-card']",
                field_selectors={
                    "title": "[data-testid='post-title']",
                    "date": "[data-testid='post-date']",
                    "read_time": "[data-testid='reading-time']"
                }
            )
            # Returns:
            # [
            #     {"title": "Post 1", "date": "2023-01-01", "read_time": "5 min"},
            #     {"title": "Post 2", "date": "2023-01-02", "read_time": "7 min"}
            # ]
        """
        pass

    def get_all_texts_from_nested(
        self,
        parent_locator: str,
        child_locator: str,
        parent_index: int = 0
    ) -> list[str]:
        """
        Obtiene TODOS los textos de elementos hijos dentro de un elemento padre específico.

        Similar a get_text_from_nested, pero devuelve lista en vez de string.

        Args:
            parent_locator (str): Locator del elemento padre.
            child_locator (str): Locator del elemento hijo.
            parent_index (int): Índice del elemento padre si hay múltiples coincidencias.

        Returns:
            list[str]: Lista de textos de los elementos hijos.

        Ejemplo:
            # Obtener todos los tags del segundo blog post.
            # tags = browser.get_all_texts_from_nested(
            #     parent_locator="[data-testid='post-card']",
            #     child_locator="[data-testid='tag-']",
            #     parent_index=1
            #)
            # Returns: ["python", "testing", "automation"]
        """
        pass