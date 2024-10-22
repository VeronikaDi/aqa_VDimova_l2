class TestData:

    _BASE_URL: str = "https://qauto2.forstudy.space"

    _USER_NAME: str = "Mifodii"
    _USER_LAST_NAME: str = "Aprofiev"
    _USER_EMAIL: str = "mif_ap_check@gmail.com"
    _USER_PASSWORD: str = "nihaIdrYT67!."

    @property
    def base_url(self) -> str:
        return self._BASE_URL

    @property
    def user_name(self) -> str:
        return self._USER_NAME

    @property
    def user_last_name(self) -> str:
        return self._USER_LAST_NAME

    @property
    def user_email(self) -> str:
        return self._USER_EMAIL

    @property
    def user_password(self) -> str:
        return self._USER_PASSWORD
