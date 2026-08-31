from typing import Literal

ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_archive_create_cert_manager_status_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateCertManagerStatusErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
