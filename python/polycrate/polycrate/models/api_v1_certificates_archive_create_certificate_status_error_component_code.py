from typing import Literal

ApiV1CertificatesArchiveCreateCertificateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateCertificateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_certificates_archive_create_certificate_status_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateCertificateStatusErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
