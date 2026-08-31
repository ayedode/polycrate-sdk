from typing import Literal

ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_catalogue_apps_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
