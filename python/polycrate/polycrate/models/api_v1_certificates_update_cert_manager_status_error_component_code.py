from typing import Literal

ApiV1CertificatesUpdateCertManagerStatusErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateCertManagerStatusErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_update_cert_manager_status_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateCertManagerStatusErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
