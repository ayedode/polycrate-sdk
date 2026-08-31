from typing import Literal

ApiV1PricingProductsCreateProviderEntityErrorComponentAttr = Literal["provider_entity"]

API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateProviderEntityErrorComponentAttr
] = {
    "provider_entity",
}


def check_api_v1_pricing_products_create_provider_entity_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateProviderEntityErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
