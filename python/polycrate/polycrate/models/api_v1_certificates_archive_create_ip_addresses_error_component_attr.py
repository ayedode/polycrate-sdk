from typing import Literal

ApiV1CertificatesArchiveCreateIpAddressesErrorComponentAttr = Literal["ip_addresses"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_IP_ADDRESSES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateIpAddressesErrorComponentAttr
] = {
    "ip_addresses",
}


def check_api_v1_certificates_archive_create_ip_addresses_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateIpAddressesErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_IP_ADDRESSES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_IP_ADDRESSES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
