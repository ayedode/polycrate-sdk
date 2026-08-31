from typing import Literal

ApiV1EndpointsUpdateArchivedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdateArchivedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_update_archived_by_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateArchivedByErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
