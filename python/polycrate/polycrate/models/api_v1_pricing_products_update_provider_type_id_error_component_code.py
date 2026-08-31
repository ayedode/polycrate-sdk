from typing import Literal

ApiV1PricingProductsUpdateProviderTypeIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_PRODUCTS_UPDATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsUpdateProviderTypeIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_products_update_provider_type_id_error_component_code(
    value: str,
) -> ApiV1PricingProductsUpdateProviderTypeIdErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
