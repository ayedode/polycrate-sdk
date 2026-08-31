from typing import Literal

ApiV1CatalogueAppsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CATALOGUE_APPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_catalogue_apps_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
