from typing import Literal

ApiV1IpaddressesArchiveCreateIpAddressErrorComponentAttr = Literal["ip_address"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_IP_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesArchiveCreateIpAddressErrorComponentAttr
] = {
    "ip_address",
}


def check_api_v1_ipaddresses_archive_create_ip_address_error_component_attr(
    value: str,
) -> ApiV1IpaddressesArchiveCreateIpAddressErrorComponentAttr:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_IP_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_IP_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
