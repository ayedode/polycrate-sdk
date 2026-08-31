from typing import Literal

ApiV1ConditionInstancesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CONDITION_INSTANCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_condition_instances_update_annotations_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
