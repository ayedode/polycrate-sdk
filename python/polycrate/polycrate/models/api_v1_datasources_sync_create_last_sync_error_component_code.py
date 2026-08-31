from typing import Literal

ApiV1DatasourcesSyncCreateLastSyncErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_DATASOURCES_SYNC_CREATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateLastSyncErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_datasources_sync_create_last_sync_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateLastSyncErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
