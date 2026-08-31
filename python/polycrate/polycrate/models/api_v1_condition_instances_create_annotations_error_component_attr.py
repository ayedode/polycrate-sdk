from typing import Literal

ApiV1ConditionInstancesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CONDITION_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_condition_instances_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
