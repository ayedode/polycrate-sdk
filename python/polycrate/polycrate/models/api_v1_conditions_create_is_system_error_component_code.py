from typing import Literal

ApiV1ConditionsCreateIsSystemErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITIONS_CREATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ConditionsCreateIsSystemErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_conditions_create_is_system_error_component_code(
    value: str,
) -> ApiV1ConditionsCreateIsSystemErrorComponentCode:
    if value in API_V1_CONDITIONS_CREATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_IS_SYSTEM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
