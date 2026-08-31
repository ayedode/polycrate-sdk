from typing import Literal

ApiV1CatalogueAppsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CATALOGUE_APPS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_catalogue_apps_create_kind_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateKindErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
