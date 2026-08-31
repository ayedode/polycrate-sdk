from typing import Literal

ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_rescan_notes_create_is_enabled_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
