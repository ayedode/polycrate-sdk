from typing import Literal

ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_RELEASES_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_catalogue_apps_archive_create_releases_url_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_RELEASES_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_RELEASES_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
