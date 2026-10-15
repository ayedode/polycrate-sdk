from typing import Literal

BlockRolloutItemRequestProvider = Literal[
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

BLOCK_ROLLOUT_ITEM_REQUEST_PROVIDER_VALUES: set[BlockRolloutItemRequestProvider] = {
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


def check_block_rollout_item_request_provider(value: str) -> BlockRolloutItemRequestProvider:
    if value in BLOCK_ROLLOUT_ITEM_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_REQUEST_PROVIDER_VALUES!r}")
