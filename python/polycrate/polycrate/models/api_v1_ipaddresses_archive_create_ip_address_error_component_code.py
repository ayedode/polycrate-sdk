from typing import Literal

ApiV1IpaddressesArchiveCreateIpAddressErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_IPADDRESSES_ARCHIVE_CREATE_IP_ADDRESS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesArchiveCreateIpAddressErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_ipaddresses_archive_create_ip_address_error_component_code(
    value: str,
) -> ApiV1IpaddressesArchiveCreateIpAddressErrorComponentCode:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_IP_ADDRESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_IP_ADDRESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
