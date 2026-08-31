from typing import Literal

ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TRACKED_APP_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_catalogue_apps_archive_create_tracked_app_version_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TRACKED_APP_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TRACKED_APP_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
