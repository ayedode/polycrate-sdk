from typing import Literal

ApiV1IncidentsCreateModifiedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_INCIDENTS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsCreateModifiedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_incidents_create_modified_by_user_error_component_code(
    value: str,
) -> ApiV1IncidentsCreateModifiedByUserErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
