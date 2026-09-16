from typing import Literal

ApiV1PricingProductsCreatePopErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_PRODUCTS_CREATE_POP_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PricingProductsCreatePopErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_products_create_pop_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreatePopErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_POP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_POP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
