from typing import Literal

ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponentAttr = Literal["last_sync_error"]

API_V1_DATASOURCES_ARCHIVE_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponentAttr
] = {
    "last_sync_error",
}


def check_api_v1_datasources_archive_create_last_sync_error_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
