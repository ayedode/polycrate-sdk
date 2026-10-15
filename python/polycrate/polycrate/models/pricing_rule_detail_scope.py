from typing import Literal

PricingRuleDetailScope = Literal["system", "user"]

PRICING_RULE_DETAIL_SCOPE_VALUES: set[PricingRuleDetailScope] = {
    "system",
    "user",
}


def check_pricing_rule_detail_scope(value: str) -> PricingRuleDetailScope:
    if value in PRICING_RULE_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_SCOPE_VALUES!r}")
