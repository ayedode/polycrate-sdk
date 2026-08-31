from typing import Literal

ApiV1PricingRulesCreateProductKindErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_RULES_CREATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesCreateProductKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_rules_create_product_kind_error_component_code(
    value: str,
) -> ApiV1PricingRulesCreateProductKindErrorComponentCode:
    if value in API_V1_PRICING_RULES_CREATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
