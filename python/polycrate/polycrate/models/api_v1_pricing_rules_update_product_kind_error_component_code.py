from typing import Literal

ApiV1PricingRulesUpdateProductKindErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_RULES_UPDATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesUpdateProductKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_rules_update_product_kind_error_component_code(
    value: str,
) -> ApiV1PricingRulesUpdateProductKindErrorComponentCode:
    if value in API_V1_PRICING_RULES_UPDATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_UPDATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
