from typing import Literal

ApiV1CatalogueAppsCreateReleasesUrlErrorComponentAttr = Literal["releases_url"]

API_V1_CATALOGUE_APPS_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateReleasesUrlErrorComponentAttr
] = {
    "releases_url",
}


def check_api_v1_catalogue_apps_create_releases_url_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateReleasesUrlErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
