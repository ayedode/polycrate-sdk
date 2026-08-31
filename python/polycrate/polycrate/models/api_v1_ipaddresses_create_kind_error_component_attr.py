from typing import Literal

ApiV1IpaddressesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_IPADDRESSES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_ipaddresses_create_kind_error_component_attr(
    value: str,
) -> ApiV1IpaddressesCreateKindErrorComponentAttr:
    if value in API_V1_IPADDRESSES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
