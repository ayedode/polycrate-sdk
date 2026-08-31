from typing import Literal

ApiV1DatasourcesCreateLastSyncErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_DATASOURCES_CREATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesCreateLastSyncErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_datasources_create_last_sync_error_component_code(
    value: str,
) -> ApiV1DatasourcesCreateLastSyncErrorComponentCode:
    if value in API_V1_DATASOURCES_CREATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_LAST_SYNC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
