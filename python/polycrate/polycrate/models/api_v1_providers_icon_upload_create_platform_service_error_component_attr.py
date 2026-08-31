from typing import Literal

ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_providers_icon_upload_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
