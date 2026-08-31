from typing import Literal

ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponentAttr = Literal["last_sync_error"]

API_V1_DATASOURCES_PARTIAL_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponentAttr
] = {
    "last_sync_error",
}


def check_api_v1_datasources_partial_update_last_sync_error_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
