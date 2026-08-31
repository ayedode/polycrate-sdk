from typing import Literal

ApiV1ProvidersPartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PROVIDERS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_providers_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
