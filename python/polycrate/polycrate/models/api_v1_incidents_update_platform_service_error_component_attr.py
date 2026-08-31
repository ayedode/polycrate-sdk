from typing import Literal

ApiV1IncidentsUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_INCIDENTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_incidents_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
