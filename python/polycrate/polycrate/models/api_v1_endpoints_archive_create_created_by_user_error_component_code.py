from typing import Literal

ApiV1EndpointsArchiveCreateCreatedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreateCreatedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_archive_create_created_by_user_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreateCreatedByUserErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
