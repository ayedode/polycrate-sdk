from typing import Literal

ApiV1IpaddressesListKindErrorComponentAttr = Literal["kind"]

API_V1_IPADDRESSES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_ipaddresses_list_kind_error_component_attr(value: str) -> ApiV1IpaddressesListKindErrorComponentAttr:
    if value in API_V1_IPADDRESSES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
