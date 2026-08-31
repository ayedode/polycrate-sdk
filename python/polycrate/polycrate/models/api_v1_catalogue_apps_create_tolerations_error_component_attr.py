from typing import Literal

ApiV1CatalogueAppsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CATALOGUE_APPS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_catalogue_apps_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateTolerationsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
