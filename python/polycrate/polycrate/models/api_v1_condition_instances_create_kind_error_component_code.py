from typing import Literal

ApiV1ConditionInstancesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONDITION_INSTANCES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_condition_instances_create_kind_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateKindErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
