from typing import Literal

ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_partial_update_cert_manager_status_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateCertManagerStatusErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
