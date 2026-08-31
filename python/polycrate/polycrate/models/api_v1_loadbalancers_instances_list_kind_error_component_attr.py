from typing import Literal

ApiV1LoadbalancersInstancesListKindErrorComponentAttr = Literal["kind"]

API_V1_LOADBALANCERS_INSTANCES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_loadbalancers_instances_list_kind_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListKindErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
