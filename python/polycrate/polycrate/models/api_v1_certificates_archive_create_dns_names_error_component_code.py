from typing import Literal

ApiV1CertificatesArchiveCreateDnsNamesErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateDnsNamesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_archive_create_dns_names_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateDnsNamesErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
