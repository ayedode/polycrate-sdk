from typing import Literal

ApiV1PricingProductsCreateProviderTypeIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateProviderTypeIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_products_create_provider_type_id_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateProviderTypeIdErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
