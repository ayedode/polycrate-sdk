from typing import Literal

ApiV1CertificatesUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_CERTIFICATES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_certificates_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateDebugModeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
