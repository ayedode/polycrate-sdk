from typing import Literal

ApiV1CredentialsCreateApiKeyErrorComponentAttr = Literal["api_key"]

API_V1_CREDENTIALS_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsCreateApiKeyErrorComponentAttr] = {
    "api_key",
}


def check_api_v1_credentials_create_api_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsCreateApiKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
