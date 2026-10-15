from typing import Literal

PricingRuleDetailKind = Literal["generic"]

PRICING_RULE_DETAIL_KIND_VALUES: set[PricingRuleDetailKind] = {
    "generic",
}


def check_pricing_rule_detail_kind(value: str) -> PricingRuleDetailKind:
    if value in PRICING_RULE_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_KIND_VALUES!r}")
