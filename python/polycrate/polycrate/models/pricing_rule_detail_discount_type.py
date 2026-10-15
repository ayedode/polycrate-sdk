from typing import Literal

PricingRuleDetailDiscountType = Literal["fixed_override", "fixed_reduction", "percentage"]

PRICING_RULE_DETAIL_DISCOUNT_TYPE_VALUES: set[PricingRuleDetailDiscountType] = {
    "fixed_override",
    "fixed_reduction",
    "percentage",
}


def check_pricing_rule_detail_discount_type(value: str) -> PricingRuleDetailDiscountType:
    if value in PRICING_RULE_DETAIL_DISCOUNT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_DISCOUNT_TYPE_VALUES!r}")
