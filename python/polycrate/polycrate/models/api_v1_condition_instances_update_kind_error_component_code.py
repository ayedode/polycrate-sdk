from typing import Literal

ApiV1ConditionInstancesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONDITION_INSTANCES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_condition_instances_update_kind_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesUpdateKindErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
