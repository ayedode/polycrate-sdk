from typing import Literal

ApiV1CatalogueAppsCreateReleasesUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CATALOGUE_APPS_CREATE_RELEASES_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsCreateReleasesUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_catalogue_apps_create_releases_url_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateReleasesUrlErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_RELEASES_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_RELEASES_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
