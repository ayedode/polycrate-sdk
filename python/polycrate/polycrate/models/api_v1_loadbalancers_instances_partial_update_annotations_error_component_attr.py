from typing import Literal

ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_loadbalancers_instances_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
