from typing import Literal

ApiV1DatasourcesRescanNotesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_datasources_rescan_notes_create_archived_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateArchivedErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
