from typing import Literal

ApiV1ConditionInstancesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CONDITION_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_condition_instances_create_labels_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateLabelsErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
