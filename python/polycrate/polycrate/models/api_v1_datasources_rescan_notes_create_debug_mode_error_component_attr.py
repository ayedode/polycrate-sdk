from typing import Literal

ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_datasources_rescan_notes_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
