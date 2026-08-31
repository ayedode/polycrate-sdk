from typing import Literal

ApiV1CertificatesSyncCreateCertDataErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_CERTIFICATES_SYNC_CREATE_CERT_DATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesSyncCreateCertDataErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_certificates_sync_create_cert_data_error_component_code(
    value: str,
) -> ApiV1CertificatesSyncCreateCertDataErrorComponentCode:
    if value in API_V1_CERTIFICATES_SYNC_CREATE_CERT_DATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_SYNC_CREATE_CERT_DATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
