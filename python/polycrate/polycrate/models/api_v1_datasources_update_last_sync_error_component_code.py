from typing import Literal

ApiV1DatasourcesUpdateLastSyncErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_DATASOURCES_UPDATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateLastSyncErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_datasources_update_last_sync_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateLastSyncErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
