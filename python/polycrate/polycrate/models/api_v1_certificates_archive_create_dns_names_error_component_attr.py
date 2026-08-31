from typing import Literal

ApiV1CertificatesArchiveCreateDnsNamesErrorComponentAttr = Literal["dns_names"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_DNS_NAMES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateDnsNamesErrorComponentAttr
] = {
    "dns_names",
}


def check_api_v1_certificates_archive_create_dns_names_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateDnsNamesErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_DNS_NAMES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_DNS_NAMES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
