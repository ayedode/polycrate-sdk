from typing import Literal

ApiV1ConditionInstancesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CONDITION_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_condition_instances_create_labels_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateLabelsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
