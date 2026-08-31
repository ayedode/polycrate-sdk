from typing import Literal

ApiV1LoadbalancersRegionsCreateActiveErrorComponentAttr = Literal["active"]

API_V1_LOADBALANCERS_REGIONS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_loadbalancers_regions_create_active_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateActiveErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
