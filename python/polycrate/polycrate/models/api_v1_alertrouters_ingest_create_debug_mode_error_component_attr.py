from typing import Literal

ApiV1AlertroutersIngestCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ALERTROUTERS_INGEST_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_alertrouters_ingest_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateDebugModeErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
