from typing import Literal

ApiV1IncidentsArchiveCreateCreatedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_INCIDENTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsArchiveCreateCreatedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_incidents_archive_create_created_by_user_error_component_code(
    value: str,
) -> ApiV1IncidentsArchiveCreateCreatedByUserErrorComponentCode:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
