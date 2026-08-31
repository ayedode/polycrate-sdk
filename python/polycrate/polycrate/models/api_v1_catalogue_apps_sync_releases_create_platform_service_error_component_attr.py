from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_catalogue_apps_sync_releases_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
