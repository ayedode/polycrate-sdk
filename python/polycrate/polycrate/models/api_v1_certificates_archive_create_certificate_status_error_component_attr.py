from typing import Literal

ApiV1CertificatesArchiveCreateCertificateStatusErrorComponentAttr = Literal["certificate_status"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateCertificateStatusErrorComponentAttr
] = {
    "certificate_status",
}


def check_api_v1_certificates_archive_create_certificate_status_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateCertificateStatusErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
