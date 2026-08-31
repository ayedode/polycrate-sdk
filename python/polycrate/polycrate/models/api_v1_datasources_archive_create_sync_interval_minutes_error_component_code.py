from typing import Literal

ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DATASOURCES_ARCHIVE_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_datasources_archive_create_sync_interval_minutes_error_component_code(
    value: str,
) -> ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponentCode:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
