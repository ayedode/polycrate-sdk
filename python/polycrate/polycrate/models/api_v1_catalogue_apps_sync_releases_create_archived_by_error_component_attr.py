from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_catalogue_apps_sync_releases_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
