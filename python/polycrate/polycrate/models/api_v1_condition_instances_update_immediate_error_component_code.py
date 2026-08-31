from typing import Literal

ApiV1ConditionInstancesUpdateImmediateErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_UPDATE_IMMEDIATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesUpdateImmediateErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_update_immediate_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesUpdateImmediateErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_IMMEDIATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_IMMEDIATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
