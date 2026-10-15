from typing import Literal

PricingCalculatorStateDetailRequestProvider = Literal[
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
]

PRICING_CALCULATOR_STATE_DETAIL_REQUEST_PROVIDER_VALUES: set[PricingCalculatorStateDetailRequestProvider] = {
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
}


def check_pricing_calculator_state_detail_request_provider(value: str) -> PricingCalculatorStateDetailRequestProvider:
    if value in PRICING_CALCULATOR_STATE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
