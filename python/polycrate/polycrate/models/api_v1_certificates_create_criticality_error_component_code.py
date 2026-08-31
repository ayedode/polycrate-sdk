from typing import Literal

ApiV1CertificatesCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_CERTIFICATES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_certificates_create_criticality_error_component_code(
    value: str,
) -> ApiV1CertificatesCreateCriticalityErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
