from typing import Literal

ApiV1CatalogueAppsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_catalogue_apps_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
