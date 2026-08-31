from typing import Literal

ApiV1DatasourcesSyncCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DATASOURCES_SYNC_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_datasources_sync_create_archived_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateArchivedErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
