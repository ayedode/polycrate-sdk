from typing import Literal

ApiV1ConditionsPartialUpdateIsSystemErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITIONS_PARTIAL_UPDATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsPartialUpdateIsSystemErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conditions_partial_update_is_system_error_component_code(
    value: str,
) -> ApiV1ConditionsPartialUpdateIsSystemErrorComponentCode:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
