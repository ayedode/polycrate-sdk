from typing import Literal

PricingRuleDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_RULE_DETAIL_LAST_STATE_VALUES: set[PricingRuleDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_rule_detail_last_state(value: str) -> PricingRuleDetailLastState:
    if value in PRICING_RULE_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_LAST_STATE_VALUES!r}")
