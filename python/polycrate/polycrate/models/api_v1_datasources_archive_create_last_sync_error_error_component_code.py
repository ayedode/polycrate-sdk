from typing import Literal

ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DATASOURCES_ARCHIVE_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_datasources_archive_create_last_sync_error_error_component_code(
    value: str,
) -> ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponentCode:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
