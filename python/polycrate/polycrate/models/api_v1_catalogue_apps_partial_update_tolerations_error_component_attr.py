from typing import Literal

ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_catalogue_apps_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
