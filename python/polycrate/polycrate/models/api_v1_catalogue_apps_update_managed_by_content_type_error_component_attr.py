from typing import Literal

ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_CATALOGUE_APPS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_catalogue_apps_update_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
