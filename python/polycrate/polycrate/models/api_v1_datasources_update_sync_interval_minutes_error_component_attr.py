from typing import Literal

ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponentAttr = Literal["sync_interval_minutes"]

API_V1_DATASOURCES_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponentAttr
] = {
    "sync_interval_minutes",
}


def check_api_v1_datasources_update_sync_interval_minutes_error_component_attr(
    value: str,
) -> ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponentAttr:
    if value in API_V1_DATASOURCES_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
