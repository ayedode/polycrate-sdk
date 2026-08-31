from typing import Literal

ApiV1CatalogueAppsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CATALOGUE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_catalogue_apps_create_criticality_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateCriticalityErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
