from typing import Literal

ApiV1ProvidersPartialUpdateUrlsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersPartialUpdateUrlsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_partial_update_urls_error_component_code(
    value: str,
) -> ApiV1ProvidersPartialUpdateUrlsErrorComponentCode:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
