from typing import Literal

PatchedBlockRolloutItemRequestProvider = Literal[
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

PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_PROVIDER_VALUES: set[PatchedBlockRolloutItemRequestProvider] = {
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


def check_patched_block_rollout_item_request_provider(value: str) -> PatchedBlockRolloutItemRequestProvider:
    if value in PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_PROVIDER_VALUES!r}"
    )
