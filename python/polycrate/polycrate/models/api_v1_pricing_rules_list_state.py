from typing import Literal

ApiV1PricingRulesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PRICING_RULES_LIST_STATE_VALUES: set[ApiV1PricingRulesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pricing_rules_list_state(value: str) -> ApiV1PricingRulesListState:
    if value in API_V1_PRICING_RULES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_STATE_VALUES!r}")
