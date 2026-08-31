from typing import Literal

ApiV1PricingProductsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_products_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingProductsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
