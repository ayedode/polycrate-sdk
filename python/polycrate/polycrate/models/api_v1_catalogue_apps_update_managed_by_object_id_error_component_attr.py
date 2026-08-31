from typing import Literal

ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_CATALOGUE_APPS_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_catalogue_apps_update_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
