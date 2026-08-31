from typing import Literal

ApiV1CatalogueAppsUpdateProductHaIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_CATALOGUE_APPS_UPDATE_PRODUCT_HA_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsUpdateProductHaIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_catalogue_apps_update_product_ha_id_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsUpdateProductHaIdErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_UPDATE_PRODUCT_HA_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_PRODUCT_HA_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
