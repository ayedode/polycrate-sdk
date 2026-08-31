from typing import Literal

ApiV1CatalogueAppsCreateProductHaIdErrorComponentAttr = Literal["product_ha_id"]

API_V1_CATALOGUE_APPS_CREATE_PRODUCT_HA_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateProductHaIdErrorComponentAttr
] = {
    "product_ha_id",
}


def check_api_v1_catalogue_apps_create_product_ha_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateProductHaIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_PRODUCT_HA_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_PRODUCT_HA_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
