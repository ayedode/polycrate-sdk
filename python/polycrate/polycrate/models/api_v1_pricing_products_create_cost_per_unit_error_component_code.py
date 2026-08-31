from typing import Literal

ApiV1PricingProductsCreateCostPerUnitErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PRICING_PRODUCTS_CREATE_COST_PER_UNIT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateCostPerUnitErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pricing_products_create_cost_per_unit_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateCostPerUnitErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_COST_PER_UNIT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_COST_PER_UNIT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
