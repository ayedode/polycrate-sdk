from typing import Literal

ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_endpoints_archive_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
