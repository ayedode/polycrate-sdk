from typing import Literal

ApiV1CatalogueAppsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_catalogue_apps_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
