from typing import Literal

ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponentAttr = Literal["sync_interval_minutes"]

API_V1_DATASOURCES_PARTIAL_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponentAttr
] = {
    "sync_interval_minutes",
}


def check_api_v1_datasources_partial_update_sync_interval_minutes_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
