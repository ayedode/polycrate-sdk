from typing import Literal

ApiV1CertificatesUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_update_platform_service_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
