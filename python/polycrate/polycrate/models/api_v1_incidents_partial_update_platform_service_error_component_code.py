from typing import Literal

ApiV1IncidentsPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
