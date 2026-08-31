from typing import Literal

ApiV1ProvidersUpdateUrlsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersUpdateUrlsErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_providers_update_urls_error_component_code(value: str) -> ApiV1ProvidersUpdateUrlsErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
