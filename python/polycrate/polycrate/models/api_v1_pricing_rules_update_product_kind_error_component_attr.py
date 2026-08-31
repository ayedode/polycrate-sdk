from typing import Literal

ApiV1PricingRulesUpdateProductKindErrorComponentAttr = Literal["product_kind"]

API_V1_PRICING_RULES_UPDATE_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesUpdateProductKindErrorComponentAttr
] = {
    "product_kind",
}


def check_api_v1_pricing_rules_update_product_kind_error_component_attr(
    value: str,
) -> ApiV1PricingRulesUpdateProductKindErrorComponentAttr:
    if value in API_V1_PRICING_RULES_UPDATE_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_UPDATE_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
