from typing import Literal

ApiV1ConditionsUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ConditionsUpdateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_conditions_update_archived_error_component_code(
    value: str,
) -> ApiV1ConditionsUpdateArchivedErrorComponentCode:
    if value in API_V1_CONDITIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
