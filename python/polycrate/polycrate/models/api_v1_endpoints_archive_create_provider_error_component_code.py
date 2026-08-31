from typing import Literal

ApiV1EndpointsArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_endpoints_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreateProviderErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
