from typing import Literal

ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_catalogue_apps_archive_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
