class TestData:
    _BASE_URL: str = "https://tracking.novaposhta.ua/#/uk"
    _PACKAGE_NUMBER: str = "20450999308642"

    @property
    def base_url(self) -> str:
        return self._BASE_URL

    @property
    def package_number(self) -> str:
        return self._PACKAGE_NUMBER
