from typing import Literal

ApiV1CatalogueAppsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_CATALOGUE_APPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_catalogue_apps_create_provider_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateProviderErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
