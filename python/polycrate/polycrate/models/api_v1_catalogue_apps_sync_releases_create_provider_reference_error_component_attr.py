from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_catalogue_apps_sync_releases_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
