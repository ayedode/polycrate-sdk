from typing import Literal

ApiV1LoadbalancersInstancesListNameErrorComponentAttr = Literal["name"]

API_V1_LOADBALANCERS_INSTANCES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_loadbalancers_instances_list_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
