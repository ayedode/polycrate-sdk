from typing import Literal

ApiV1ConditionInstancesUpdateConditionErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_CONDITION_INSTANCES_UPDATE_CONDITION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesUpdateConditionErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_condition_instances_update_condition_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesUpdateConditionErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_CONDITION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_CONDITION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
