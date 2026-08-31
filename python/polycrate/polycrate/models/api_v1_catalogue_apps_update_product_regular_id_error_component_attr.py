from typing import Literal

ApiV1CatalogueAppsUpdateProductRegularIdErrorComponentAttr = Literal["product_regular_id"]

API_V1_CATALOGUE_APPS_UPDATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateProductRegularIdErrorComponentAttr
] = {
    "product_regular_id",
}


def check_api_v1_catalogue_apps_update_product_regular_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateProductRegularIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
