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