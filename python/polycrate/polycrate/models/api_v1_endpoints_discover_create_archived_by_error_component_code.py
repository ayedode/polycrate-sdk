from typing import Literal

ApiV1EndpointsDiscoverCreateArchivedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_DISCOVER_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateArchivedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_discover_create_archived_by_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateArchivedByErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
