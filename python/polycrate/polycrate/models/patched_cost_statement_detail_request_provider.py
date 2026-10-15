from typing import Literal

PatchedCostStatementDetailRequestProvider = Literal[
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

PATCHED_COST_STATEMENT_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedCostStatementDetailRequestProvider] = {
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


def check_patched_cost_statement_detail_request_provider(value: str) -> PatchedCostStatementDetailRequestProvider:
    if value in PATCHED_COST_STATEMENT_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_COST_STATEMENT_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
