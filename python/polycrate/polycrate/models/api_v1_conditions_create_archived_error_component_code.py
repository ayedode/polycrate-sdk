from typing import Literal

ApiV1ConditionsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITIONS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ConditionsCreateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_conditions_create_archived_error_component_code(
    value: str,
) -> ApiV1ConditionsCreateArchivedErrorComponentCode:
    if value in API_V1_CONDITIONS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
