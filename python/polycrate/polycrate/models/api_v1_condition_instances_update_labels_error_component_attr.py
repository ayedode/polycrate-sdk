from typing import Literal

ApiV1ConditionInstancesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CONDITION_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_condition_instances_update_labels_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateLabelsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
