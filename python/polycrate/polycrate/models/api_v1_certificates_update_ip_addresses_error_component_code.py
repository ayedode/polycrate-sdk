from typing import Literal

ApiV1CertificatesUpdateIpAddressesErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_UPDATE_IP_ADDRESSES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateIpAddressesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_update_ip_addresses_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateIpAddressesErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_IP_ADDRESSES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_IP_ADDRESSES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
