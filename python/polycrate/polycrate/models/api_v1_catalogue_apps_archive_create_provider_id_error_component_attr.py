from typing import Literal

ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_catalogue_apps_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
