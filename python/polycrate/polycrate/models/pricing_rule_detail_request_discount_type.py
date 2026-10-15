from typing import Literal

PricingRuleDetailRequestDiscountType = Literal["fixed_override", "fixed_reduction", "percentage"]

PRICING_RULE_DETAIL_REQUEST_DISCOUNT_TYPE_VALUES: set[PricingRuleDetailRequestDiscountType] = {
    "fixed_override",
    "fixed_reduction",
    "percentage",
}


def check_pricing_rule_detail_request_discount_type(value: str) -> PricingRuleDetailRequestDiscountType:
    if value in PRICING_RULE_DETAIL_REQUEST_DISCOUNT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_REQUEST_DISCOUNT_TYPE_VALUES!r}")
