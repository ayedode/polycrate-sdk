from typing import Literal

ApiV1ConditionInstancesUpdateReasonErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONDITION_INSTANCES_UPDATE_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesUpdateReasonErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_condition_instances_update_reason_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesUpdateReasonErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
