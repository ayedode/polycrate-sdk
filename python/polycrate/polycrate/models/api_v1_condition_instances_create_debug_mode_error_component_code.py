from typing import Literal

ApiV1ConditionInstancesCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateDebugModeErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
