from typing import Literal

ApiV1CertificatesCreateCertManagerStatusErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_CREATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreateCertManagerStatusErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_create_cert_manager_status_error_component_code(
    value: str,
) -> ApiV1CertificatesCreateCertManagerStatusErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
