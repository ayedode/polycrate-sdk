from typing import Literal

ApiV1LoadbalancersRegionsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_loadbalancers_regions_update_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
