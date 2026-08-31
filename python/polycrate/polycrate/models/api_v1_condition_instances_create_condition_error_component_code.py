from typing import Literal

ApiV1ConditionInstancesCreateConditionErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_CONDITION_INSTANCES_CREATE_CONDITION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateConditionErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_condition_instances_create_condition_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateConditionErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_CONDITION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_CONDITION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
