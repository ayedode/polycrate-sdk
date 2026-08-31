from typing import Literal

ApiV1PricingRulesCreateProductKindErrorComponentAttr = Literal["product_kind"]

API_V1_PRICING_RULES_CREATE_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesCreateProductKindErrorComponentAttr
] = {
    "product_kind",
}


def check_api_v1_pricing_rules_create_product_kind_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateProductKindErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
