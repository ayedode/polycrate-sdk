from typing import Literal

ApiV1CredentialsUpdateApiKeyErrorComponentAttr = Literal["api_key"]

API_V1_CREDENTIALS_UPDATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsUpdateApiKeyErrorComponentAttr] = {
    "api_key",
}


def check_api_v1_credentials_update_api_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsUpdateApiKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_UPDATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_UPDATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
