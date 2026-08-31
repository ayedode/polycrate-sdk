from typing import Literal

ApiV1LoadbalancersRegionsListNameErrorComponentAttr = Literal["name"]

API_V1_LOADBALANCERS_REGIONS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_loadbalancers_regions_list_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsListNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
