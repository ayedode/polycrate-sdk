from typing import Literal

ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponentAttr = Literal["is_enabled"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_IS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponentAttr
] = {
    "is_enabled",
}


def check_api_v1_datasources_rescan_notes_create_is_enabled_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_IS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_IS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
