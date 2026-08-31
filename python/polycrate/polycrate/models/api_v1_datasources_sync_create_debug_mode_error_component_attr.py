from typing import Literal

ApiV1DatasourcesSyncCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_DATASOURCES_SYNC_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_datasources_sync_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateDebugModeErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
