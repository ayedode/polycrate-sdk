from typing import Literal

ApiV1ConditionInstancesCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_CONDITION_INSTANCES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_condition_instances_create_criticality_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateCriticalityErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
