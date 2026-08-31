from typing import Literal

ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DATASOURCES_PARTIAL_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_datasources_partial_update_sync_interval_minutes_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
