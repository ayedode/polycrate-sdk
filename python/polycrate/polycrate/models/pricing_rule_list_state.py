from typing import Literal

PricingRuleListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_RULE_LIST_STATE_VALUES: set[PricingRuleListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_rule_list_state(value: str) -> PricingRuleListState:
    if value in PRICING_RULE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_LIST_STATE_VALUES!r}")
