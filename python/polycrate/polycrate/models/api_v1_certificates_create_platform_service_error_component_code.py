from typing import Literal

ApiV1CertificatesCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_create_platform_service_error_component_code(
    value: str,
) -> ApiV1CertificatesCreatePlatformServiceErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
