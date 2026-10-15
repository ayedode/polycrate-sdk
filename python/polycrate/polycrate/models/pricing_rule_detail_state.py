from typing import Literal

PricingRuleDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_RULE_DETAIL_STATE_VALUES: set[PricingRuleDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_rule_detail_state(value: str) -> PricingRuleDetailState:
    if value in PRICING_RULE_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_STATE_VALUES!r}")
