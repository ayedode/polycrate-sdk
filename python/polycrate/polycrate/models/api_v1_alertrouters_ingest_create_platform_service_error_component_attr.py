from typing import Literal

ApiV1AlertroutersIngestCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ALERTROUTERS_INGEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_alertrouters_ingest_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
