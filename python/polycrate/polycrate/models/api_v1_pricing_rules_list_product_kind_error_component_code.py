from typing import Literal

ApiV1PricingRulesListProductKindErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_RULES_LIST_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesListProductKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_rules_list_product_kind_error_component_code(
    value: str,
) -> ApiV1PricingRulesListProductKindErrorComponentCode:
    if value in API_V1_PRICING_RULES_LIST_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
