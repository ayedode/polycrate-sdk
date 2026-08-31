from typing import Literal

ApiV1IncidentsCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_create_platform_service_error_component_code(
    value: str,
) -> ApiV1IncidentsCreatePlatformServiceErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
