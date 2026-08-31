from typing import Literal

ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponentAttr = Literal["sync_interval_minutes"]

API_V1_DATASOURCES_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponentAttr
] = {
    "sync_interval_minutes",
}


def check_api_v1_datasources_create_sync_interval_minutes_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_SYNC_INTERVAL_MINUTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
