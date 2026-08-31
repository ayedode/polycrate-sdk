from typing import Literal

ApiV1LoadbalancersInstancesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_loadbalancers_instances_create_labels_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateLabelsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
