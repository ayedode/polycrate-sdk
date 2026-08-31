from typing import Literal

ApiV1PricingProductsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_products_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1PricingProductsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
