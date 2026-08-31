from typing import Literal

ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_loadbalancers_instances_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListCreatedByComponentErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
