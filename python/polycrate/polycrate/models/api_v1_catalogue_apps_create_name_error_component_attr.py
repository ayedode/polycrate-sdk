from typing import Literal

ApiV1CatalogueAppsCreateNameErrorComponentAttr = Literal["name"]

API_V1_CATALOGUE_APPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_catalogue_apps_create_name_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateNameErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
