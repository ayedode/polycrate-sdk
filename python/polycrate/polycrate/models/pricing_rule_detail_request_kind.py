from typing import Literal

PricingRuleDetailRequestKind = Literal["generic"]

PRICING_RULE_DETAIL_REQUEST_KIND_VALUES: set[PricingRuleDetailRequestKind] = {
    "generic",
}


def check_pricing_rule_detail_request_kind(value: str) -> PricingRuleDetailRequestKind:
    if value in PRICING_RULE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_REQUEST_KIND_VALUES!r}")
