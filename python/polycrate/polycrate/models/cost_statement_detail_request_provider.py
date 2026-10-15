from typing import Literal

CostStatementDetailRequestProvider = Literal[
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

COST_STATEMENT_DETAIL_REQUEST_PROVIDER_VALUES: set[CostStatementDetailRequestProvider] = {
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


def check_cost_statement_detail_request_provider(value: str) -> CostStatementDetailRequestProvider:
    if value in COST_STATEMENT_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_REQUEST_PROVIDER_VALUES!r}")
