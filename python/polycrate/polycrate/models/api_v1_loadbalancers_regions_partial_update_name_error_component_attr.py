from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_loadbalancers_regions_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
