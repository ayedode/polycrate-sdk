from typing import Literal

ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponentAttr = Literal["discount_type"]

API_V1_PRICING_RULES_PARTIAL_UPDATE_DISCOUNT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponentAttr
] = {
    "discount_type",
}


def check_api_v1_pricing_rules_partial_update_discount_type_error_component_attr(
    value: str,
) -> ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponentAttr:
    if value in API_V1_PRICING_RULES_PARTIAL_UPDATE_DISCOUNT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_PARTIAL_UPDATE_DISCOUNT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
