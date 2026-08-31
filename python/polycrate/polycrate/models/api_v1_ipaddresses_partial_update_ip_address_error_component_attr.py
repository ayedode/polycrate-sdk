from typing import Literal

ApiV1IpaddressesPartialUpdateIpAddressErrorComponentAttr = Literal["ip_address"]

API_V1_IPADDRESSES_PARTIAL_UPDATE_IP_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesPartialUpdateIpAddressErrorComponentAttr
] = {
    "ip_address",
}


def check_api_v1_ipaddresses_partial_update_ip_address_error_component_attr(
    value: str,
) -> ApiV1IpaddressesPartialUpdateIpAddressErrorComponentAttr:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_IP_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_IP_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
