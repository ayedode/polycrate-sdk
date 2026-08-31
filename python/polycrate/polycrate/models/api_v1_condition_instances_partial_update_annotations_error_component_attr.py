from typing import Literal

ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_condition_instances_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
