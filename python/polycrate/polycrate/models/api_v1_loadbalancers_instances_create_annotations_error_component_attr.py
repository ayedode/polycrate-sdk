from typing import Literal

ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_loadbalancers_instances_create_annotations_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
