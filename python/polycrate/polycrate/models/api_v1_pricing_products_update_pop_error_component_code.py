from typing import Literal

ApiV1PricingProductsUpdatePopErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_PRODUCTS_UPDATE_POP_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PricingProductsUpdatePopErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_products_update_pop_error_component_code(
    value: str,
) -> ApiV1PricingProductsUpdatePopErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_POP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_POP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
