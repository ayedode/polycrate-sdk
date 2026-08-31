from typing import Literal

ApiV1CertificatesCreateIsReadyErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_CREATE_IS_READY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreateIsReadyErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_create_is_ready_error_component_code(
    value: str,
) -> ApiV1CertificatesCreateIsReadyErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_IS_READY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_IS_READY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
