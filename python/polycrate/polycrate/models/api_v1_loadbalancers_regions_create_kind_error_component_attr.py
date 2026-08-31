from typing import Literal

ApiV1LoadbalancersRegionsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_LOADBALANCERS_REGIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_loadbalancers_regions_create_kind_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateKindErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
