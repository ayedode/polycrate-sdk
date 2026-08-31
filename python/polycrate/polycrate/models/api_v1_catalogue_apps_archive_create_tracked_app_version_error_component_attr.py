from typing import Literal

ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponentAttr = Literal["tracked_app_version"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TRACKED_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponentAttr
] = {
    "tracked_app_version",
}


def check_api_v1_catalogue_apps_archive_create_tracked_app_version_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TRACKED_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TRACKED_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
