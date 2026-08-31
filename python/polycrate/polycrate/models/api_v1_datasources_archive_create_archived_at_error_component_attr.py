from typing import Literal

ApiV1DatasourcesArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_DATASOURCES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_datasources_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
