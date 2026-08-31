from typing import Literal

ApiV1LoadbalancersInstancesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_LOADBALANCERS_INSTANCES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_loadbalancers_instances_list_organizations_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListOrganizationsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
