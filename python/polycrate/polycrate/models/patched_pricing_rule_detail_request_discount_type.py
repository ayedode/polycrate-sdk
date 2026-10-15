from typing import Literal

PatchedPricingRuleDetailRequestDiscountType = Literal["fixed_override", "fixed_reduction", "percentage"]

PATCHED_PRICING_RULE_DETAIL_REQUEST_DISCOUNT_TYPE_VALUES: set[PatchedPricingRuleDetailRequestDiscountType] = {
    "fixed_override",
    "fixed_reduction",
    "percentage",
}


def check_patched_pricing_rule_detail_request_discount_type(value: str) -> PatchedPricingRuleDetailRequestDiscountType:
    if value in PATCHED_PRICING_RULE_DETAIL_REQUEST_DISCOUNT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_RULE_DETAIL_REQUEST_DISCOUNT_TYPE_VALUES!r}"
    )
