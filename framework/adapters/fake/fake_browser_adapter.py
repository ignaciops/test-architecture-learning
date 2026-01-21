from framework.ports.browser_port import BrowserPort

class FakeBrowserAdapter(BrowserPort):
    """
    Implementación Fake para edge-to-edge testing.

    Este adapter no valida, solo simula estado del DOM.
    """

    def __init__(self, dom_state: dict = None):
        """
        Args:
            dom_state (dict): Estado simulado del DOM.
            Formato:
            {locator: {"text": str, "visible": bool}}
          """
        self.dom_state = dom_state or {}
        self.calls = []
        self.navigations = []
        self.clicks = []

    def navigate_to(self, url: str) -> None:
        self.calls.append(("navigate_to", url))
        self.navigations.append(url)

    def click(self, locator: str) -> None:
        self.calls.append(("click", locator))
        self.clicks.append(locator)

        # Simular click exitoso
        if locator in self.dom_state:
            if not self.dom_state[locator].get("visible", True):
                raise Exception(f"Element {locator} is not visible")
        else:
            raise Exception(f"Element {locator} not found")

    def get_text(self, locator:str) -> str:
        self.calls.append(("get_text", locator))

        if locator not in self.dom_state:
            raise Exception(f"Element {locator} not found")

        return self.dom_state[locator].get("text", "")

    def is_visible(self, locator: str) -> bool:
        self.calls.append(("is_visible", locator))

        if locator not in self.dom_state:
            raise Exception(f"Element {locator} not found")

        return self.dom_state[locator].get("visible", True)

    def wait_for_load_state(self, state: str = "networkidle") -> None:
        self.calls.append(("wait_for_load_state", state))
        # Simulacion. Load State es instantaneo.
        pass

    def wait_for_element(self, locator: str, timeout: int = 10000) -> None:
        self.calls.append(("wait_for_element", locator))
        # Simulacion. Elemento siempre esta disponible si existe en dom_state.
        if locator not in self.dom_state:
            raise TimeoutError(f"Element {locator} not found within timeout")

    def get_element_count(self, locator: str) -> int:
        """Retorna cantidad de elementos que coinciden con locator."""
        self.calls.append(("get_element_count", locator))

        if locator not in self.dom_state:
            return 0

        return self.dom_state[locator].get("count", 1)

    def get_structured_data(
        self,
        parent_locator: str,
        field_selectors: dict[str, str]
    ) -> list[dict[str, str]]:
        """
        Obtiene datos estructurados de componentes repetitivos.

        En fake, el dom_state debe tener estructura específica:
        {
            "structured_data:parent_locator": [
                {"field1": "value1", "field2": "value2"},
                {"field1": "value3", "field2": "value4"}
            ]
        }
        """
        self.calls.append(("get_structured_data", parent_locator, field_selectors))

        # Buscar datos estructurados en dom_state con key especial
        key = f"structured_data:{parent_locator}"

        if key not in self.dom_state:
            return []

        return self.dom_state[key]

    def get_all_texts(self, locator: str) -> list[str]:

        self.calls.append(("get_all_texts", locator))
        raise NotImplementedError(
            "get_all_texts() not implemented in FakeBrowserAdapter yet. "
            "Implement when you need it for testing."
        )

    def get_text_from_nested(
        self,
        parent_locator: str,
        child_locator: str,
        parent_index: int = 0
    ) -> str:

        self.calls.append(("get_text_from_nested", parent_locator, child_locator, parent_index))
        raise NotImplementedError(
            "get_text_from_nested() not implemented in FakeBrowserAdapter yet. "
            "Implement when you need it for testing."
        )

    def click_nested(
    self,
    parent_locator: str,
    child_locator: str,
    parent_index: int = 0
    ) -> None:
        """
        Simula click en elemento hijo dentro de padre específico.

        En fake, valida que:
        1. Hay suficientes elementos padre (según dom_state count)
        2. El elemento hijo existe dentro del padre
        3. El elemento es visible

        Args:
            parent_locator: Locator del elemento padre
            child_locator: Locator del elemento hijo
            parent_index: Índice del padre (0-based)

        Raises:
            IndexError: Si parent_index está fuera de rango
            Exception: Si elemento hijo no existe o no es visible
        """
        self.calls.append(("click_nested", parent_locator, child_locator, parent_index))

        # 1. Validar que hay suficientes elementos padre
        if parent_locator not in self.dom_state:
            raise Exception(f"Parent element not found: {parent_locator}")

        parent_count = self.dom_state[parent_locator].get("count", 1)

        if parent_index >= parent_count:
            raise IndexError(
                f"Parent index {parent_index} out of range. "
                f"Only {parent_count} elements found."
            )

        # 2. Construir key del elemento hijo específico
        # Formato: "parent >> nth=X >> child"
        nested_key = f"{parent_locator} >> nth={parent_index} >> {child_locator}"

        # 3. Validar que elemento hijo existe
        if nested_key not in self.dom_state:
            # Intentar buscar en structured_data también
            structured_key = f"structured_data:{parent_locator}"
            if structured_key in self.dom_state:
                # Si existe en structured_data, asumimos que es clickeable
                # (es un post card válido)
                self.clicks.append(nested_key)
                return
            else:
                raise Exception(f"Child element not found: {nested_key}")

        # 4. Validar que elemento es visible
        if not self.dom_state[nested_key].get("visible", True):
            raise Exception(f"Element not visible: {nested_key}")

        # 5. Registrar click
        self.clicks.append(nested_key)

    def get_all_nested_texts(
        self,
        parent_locator: str,
        child_locator: str
    ) -> list[str]:

        self.calls.append(("get_all_nested_texts", parent_locator, child_locator))
        raise NotImplementedError(
            "get_all_nested_texts() not implemented in FakeBrowserAdapter yet. "
            "Implement when you need it for testing."
        )

    def get_all_texts_from_nested(
        self,
        parent_locator: str,
        child_locator: str,
        parent_index: int = 0
    ) -> list[str]:

        self.calls.append(("get_all_texts_from_nested", parent_locator, child_locator, parent_index))
        raise NotImplementedError(
            "get_all_texts_from_nested() not implemented in FakeBrowserAdapter yet. "
            "Implement when you need it for testing."
        )

    # Metodos helper para asserts en tests
    def assert_navigated_to(self, url: str):
        assert url in self.navigations, \
          f"Expected navigation to {url}, got {self.navigations}"

    def assert_clicked(self, locator: str):
        assert locator in self.clicks, \
          f"Expected click on {locator}, got {self.clicks}"

    def get_call_count(self, method_name: str) -> int:
        """
        Retorna la cantidad de veces que se llamo un metodo
        """
        return len([call for call in self.calls if call[0] == method_name])
