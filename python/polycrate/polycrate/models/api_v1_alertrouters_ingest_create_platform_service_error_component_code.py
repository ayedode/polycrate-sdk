from typing import Literal

ApiV1AlertroutersIngestCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_INGEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersIngestCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_ingest_create_platform_service_error_component_code(
    value: str,
) -> ApiV1AlertroutersIngestCreatePlatformServiceErrorComponentCode:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
