from typing import Literal

ApiV1CatalogueAppsUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_CATALOGUE_APPS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_catalogue_apps_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
