from typing import Literal

ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_catalogue_apps_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
