from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponentAttr = Literal["is_new"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_IS_NEW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponentAttr
] = {
    "is_new",
}


def check_api_v1_catalogue_apps_sync_releases_create_is_new_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_IS_NEW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_IS_NEW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
