from typing import Literal

ApiV1LoadbalancersRegionsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_LOADBALANCERS_REGIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_loadbalancers_regions_list_organizations_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsListOrganizationsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
