from typing import Literal

ApiV1ProvidersArchiveCreateUrlsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersArchiveCreateUrlsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_archive_create_urls_error_component_code(
    value: str,
) -> ApiV1ProvidersArchiveCreateUrlsErrorComponentCode:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
