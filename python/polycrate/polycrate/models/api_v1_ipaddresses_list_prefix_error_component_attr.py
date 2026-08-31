from typing import Literal

ApiV1IpaddressesListPrefixErrorComponentAttr = Literal["prefix"]

API_V1_IPADDRESSES_LIST_PREFIX_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesListPrefixErrorComponentAttr] = {
    "prefix",
}


def check_api_v1_ipaddresses_list_prefix_error_component_attr(
    value: str,
) -> ApiV1IpaddressesListPrefixErrorComponentAttr:
    if value in API_V1_IPADDRESSES_LIST_PREFIX_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_LIST_PREFIX_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
