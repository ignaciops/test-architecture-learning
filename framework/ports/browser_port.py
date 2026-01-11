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

    @abstractmethod
    def navigate_to(self, url: str) -> None:
        """Navegar a una URL"""
        pass

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
    def get_all_texts(self, locator: str) -> list[str]:
        """Obtiene el texto de todos los elementos que coinciden con el locator dado."""
        pass

    @abstractmethod
    def get_element_count(self, locator: str) -> int:
        """Regresa la cantidad de elementos que coinciden con el locator dado."""
        pass

    @abstractmethod
    def wait_for_element(self, locator: str, timeout: int = 10000) -> None:
        """Espera hasta que el elemento sea visible o hasta que se agote el tiempo de espera."""
        pass

    @abstractmethod
    def wait_for_load_state(self, state: str = "networkidle") -> None:
        """Espera hasta que la página alcance el estado de carga especificado."""
        pass