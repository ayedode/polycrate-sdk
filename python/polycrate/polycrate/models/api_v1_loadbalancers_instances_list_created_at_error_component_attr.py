from typing import Literal

ApiV1LoadbalancersInstancesListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_loadbalancers_instances_list_created_at_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListCreatedAtErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
