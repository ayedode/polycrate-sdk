from typing import Literal

ApiV1CertificatesCreateCertificateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CERTIFICATES_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreateCertificateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_certificates_create_certificate_status_error_component_code(
    value: str,
) -> ApiV1CertificatesCreateCertificateStatusErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_CERTIFICATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
