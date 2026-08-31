from typing import Literal

ApiV1ConditionInstancesUpdateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONDITION_INSTANCES_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesUpdateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_condition_instances_update_name_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesUpdateNameErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
