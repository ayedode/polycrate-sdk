from typing import Literal

ApiV1ProvidersCreateUrlsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersCreateUrlsErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_providers_create_urls_error_component_code(value: str) -> ApiV1ProvidersCreateUrlsErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
