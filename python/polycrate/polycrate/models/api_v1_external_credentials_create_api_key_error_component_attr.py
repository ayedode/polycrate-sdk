from typing import Literal

ApiV1ExternalCredentialsCreateApiKeyErrorComponentAttr = Literal["api_key"]

API_V1_EXTERNAL_CREDENTIALS_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ExternalCredentialsCreateApiKeyErrorComponentAttr
] = {
    "api_key",
}


def check_api_v1_external_credentials_create_api_key_error_component_attr(
    value: str,
) -> ApiV1ExternalCredentialsCreateApiKeyErrorComponentAttr:
    if value in API_V1_EXTERNAL_CREDENTIALS_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_EXTERNAL_CREDENTIALS_CREATE_API_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
