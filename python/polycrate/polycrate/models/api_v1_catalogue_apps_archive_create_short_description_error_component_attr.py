from typing import Literal

ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponentAttr = Literal["short_description"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponentAttr
] = {
    "short_description",
}


def check_api_v1_catalogue_apps_archive_create_short_description_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
