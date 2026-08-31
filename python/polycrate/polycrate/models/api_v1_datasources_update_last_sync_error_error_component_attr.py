from typing import Literal

ApiV1DatasourcesUpdateLastSyncErrorErrorComponentAttr = Literal["last_sync_error"]

API_V1_DATASOURCES_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesUpdateLastSyncErrorErrorComponentAttr
] = {
    "last_sync_error",
}


def check_api_v1_datasources_update_last_sync_error_error_component_attr(
    value: str,
) -> ApiV1DatasourcesUpdateLastSyncErrorErrorComponentAttr:
    if value in API_V1_DATASOURCES_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
