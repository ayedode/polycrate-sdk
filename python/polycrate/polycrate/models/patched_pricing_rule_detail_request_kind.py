from typing import Literal

PatchedPricingRuleDetailRequestKind = Literal["generic"]

PATCHED_PRICING_RULE_DETAIL_REQUEST_KIND_VALUES: set[PatchedPricingRuleDetailRequestKind] = {
    "generic",
}


def check_patched_pricing_rule_detail_request_kind(value: str) -> PatchedPricingRuleDetailRequestKind:
    if value in PATCHED_PRICING_RULE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_RULE_DETAIL_REQUEST_KIND_VALUES!r}")
