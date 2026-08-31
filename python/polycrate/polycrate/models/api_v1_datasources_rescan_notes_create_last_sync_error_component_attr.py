from typing import Literal

ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentAttr = Literal["last_sync"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_LAST_SYNC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentAttr
] = {
    "last_sync",
}


def check_api_v1_datasources_rescan_notes_create_last_sync_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_LAST_SYNC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_LAST_SYNC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
