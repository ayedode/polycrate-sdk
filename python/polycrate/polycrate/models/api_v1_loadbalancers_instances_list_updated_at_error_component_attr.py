from typing import Literal

ApiV1LoadbalancersInstancesListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_LOADBALANCERS_INSTANCES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_loadbalancers_instances_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListUpdatedAtErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
