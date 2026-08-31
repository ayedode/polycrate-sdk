from typing import Literal

ApiV1CertificatesUpdateCertificateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CERTIFICATES_UPDATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateCertificateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_certificates_update_certificate_status_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateCertificateStatusErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
