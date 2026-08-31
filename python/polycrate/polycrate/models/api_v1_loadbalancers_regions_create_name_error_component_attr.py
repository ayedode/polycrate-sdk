from typing import Literal

ApiV1LoadbalancersRegionsCreateNameErrorComponentAttr = Literal["name"]

API_V1_LOADBALANCERS_REGIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_loadbalancers_regions_create_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
