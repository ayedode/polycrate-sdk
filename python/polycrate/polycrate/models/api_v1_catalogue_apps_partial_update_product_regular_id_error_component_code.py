from typing import Literal

ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_catalogue_apps_partial_update_product_regular_id_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
