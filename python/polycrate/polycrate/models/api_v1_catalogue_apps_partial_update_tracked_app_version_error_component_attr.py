from typing import Literal

ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponentAttr = Literal["tracked_app_version"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_TRACKED_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponentAttr
] = {
    "tracked_app_version",
}


def check_api_v1_catalogue_apps_partial_update_tracked_app_version_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_TRACKED_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_TRACKED_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
