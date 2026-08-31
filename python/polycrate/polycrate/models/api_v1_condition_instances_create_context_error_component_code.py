from typing import Literal

ApiV1ConditionInstancesCreateContextErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_CREATE_CONTEXT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateContextErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_create_context_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateContextErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_CONTEXT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_CONTEXT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
