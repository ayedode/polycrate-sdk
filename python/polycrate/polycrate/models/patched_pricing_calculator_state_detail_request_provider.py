from typing import Literal

PatchedPricingCalculatorStateDetailRequestProvider = Literal[
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

PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_PROVIDER_VALUES: set[
    PatchedPricingCalculatorStateDetailRequestProvider
] = {
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


def check_patched_pricing_calculator_state_detail_request_provider(
    value: str,
) -> PatchedPricingCalculatorStateDetailRequestProvider:
    if value in PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
