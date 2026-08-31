from typing import Literal

ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponentAttr = Literal["sync_interval_minutes"]

API_V1_DATASOURCES_SYNC_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponentAttr
] = {
    "sync_interval_minutes",
}


def check_api_v1_datasources_sync_create_sync_interval_minutes_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
