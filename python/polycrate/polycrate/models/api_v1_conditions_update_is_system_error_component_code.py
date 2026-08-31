from typing import Literal

ApiV1ConditionsUpdateIsSystemErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITIONS_UPDATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ConditionsUpdateIsSystemErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_conditions_update_is_system_error_component_code(
    value: str,
) -> ApiV1ConditionsUpdateIsSystemErrorComponentCode:
    if value in API_V1_CONDITIONS_UPDATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
