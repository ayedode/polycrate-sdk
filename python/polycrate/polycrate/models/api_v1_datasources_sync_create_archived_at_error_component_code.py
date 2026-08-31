from typing import Literal

ApiV1DatasourcesSyncCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_DATASOURCES_SYNC_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_datasources_sync_create_archived_at_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateArchivedAtErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
