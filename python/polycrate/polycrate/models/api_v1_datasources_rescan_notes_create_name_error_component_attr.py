from typing import Literal

ApiV1DatasourcesRescanNotesCreateNameErrorComponentAttr = Literal["name"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_datasources_rescan_notes_create_name_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateNameErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
