from typing import Literal

ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponentAttr = Literal["product_ha_id"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PRODUCT_HA_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponentAttr
] = {
    "product_ha_id",
}


def check_api_v1_catalogue_apps_archive_create_product_ha_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PRODUCT_HA_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PRODUCT_HA_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
