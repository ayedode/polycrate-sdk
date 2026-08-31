from typing import Literal

ApiV1ConditionInstancesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_create_tolerations_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateTolerationsErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
