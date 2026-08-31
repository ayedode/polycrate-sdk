from typing import Literal

ApiV1LoadbalancersRegionsUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_loadbalancers_regions_update_active_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateActiveErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
