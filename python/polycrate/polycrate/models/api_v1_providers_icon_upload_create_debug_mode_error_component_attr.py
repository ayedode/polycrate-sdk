from typing import Literal

ApiV1ProvidersIconUploadCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_providers_icon_upload_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateDebugModeErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
