from typing import Literal

ApiV1CertificatesArchiveCreateIpAddressesErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_IP_ADDRESSES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateIpAddressesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_archive_create_ip_addresses_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateIpAddressesErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_IP_ADDRESSES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_IP_ADDRESSES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
