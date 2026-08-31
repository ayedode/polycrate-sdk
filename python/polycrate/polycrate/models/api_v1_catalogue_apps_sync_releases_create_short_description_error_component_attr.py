from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponentAttr = Literal["short_description"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponentAttr
] = {
    "short_description",
}


def check_api_v1_catalogue_apps_sync_releases_create_short_description_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
