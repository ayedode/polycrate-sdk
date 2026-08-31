from typing import Literal

ApiV1CatalogueAppsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CATALOGUE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_catalogue_apps_create_archived_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateArchivedErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
