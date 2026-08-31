from typing import Literal

ApiV1ConditionInstancesPartialUpdateContextErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONTEXT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateContextErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_partial_update_context_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateContextErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONTEXT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONTEXT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
