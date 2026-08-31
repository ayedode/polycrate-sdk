from typing import Literal

ApiV1LoadbalancersInstancesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_LOADBALANCERS_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_loadbalancers_instances_update_labels_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesUpdateLabelsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
