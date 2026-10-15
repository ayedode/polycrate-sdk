from typing import Literal

PricingRuleDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PricingRuleDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pricing_rule_detail_request_criticality_type_1(value: str) -> PricingRuleDetailRequestCriticalityType1:
    if value in PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
