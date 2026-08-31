from typing import Literal

ApiV1ConditionInstancesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CONDITION_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_condition_instances_update_labels_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesUpdateLabelsErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
