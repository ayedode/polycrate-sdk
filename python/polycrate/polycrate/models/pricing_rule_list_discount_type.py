from typing import Literal

PricingRuleListDiscountType = Literal["fixed_override", "fixed_reduction", "percentage"]

PRICING_RULE_LIST_DISCOUNT_TYPE_VALUES: set[PricingRuleListDiscountType] = {
    "fixed_override",
    "fixed_reduction",
    "percentage",
}


def check_pricing_rule_list_discount_type(value: str) -> PricingRuleListDiscountType:
    if value in PRICING_RULE_LIST_DISCOUNT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_LIST_DISCOUNT_TYPE_VALUES!r}")
