from typing import Literal

ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponentAttr = Literal["cost_per_unit"]

API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_COST_PER_UNIT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponentAttr
] = {
    "cost_per_unit",
}


def check_api_v1_pricing_products_partial_update_cost_per_unit_error_component_attr(
    value: str,
) -> ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_COST_PER_UNIT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_COST_PER_UNIT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
