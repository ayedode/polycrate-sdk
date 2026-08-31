from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_catalogue_apps_sync_releases_create_display_name_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
