from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_catalogue_apps_sync_releases_create_archived_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
