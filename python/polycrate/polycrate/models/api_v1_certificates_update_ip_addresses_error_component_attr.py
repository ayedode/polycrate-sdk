from typing import Literal

ApiV1CertificatesUpdateIpAddressesErrorComponentAttr = Literal["ip_addresses"]

API_V1_CERTIFICATES_UPDATE_IP_ADDRESSES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateIpAddressesErrorComponentAttr
] = {
    "ip_addresses",
}


def check_api_v1_certificates_update_ip_addresses_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateIpAddressesErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_IP_ADDRESSES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_IP_ADDRESSES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
