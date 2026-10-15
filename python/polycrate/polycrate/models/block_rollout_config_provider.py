from typing import Literal

BlockRolloutConfigProvider = Literal[
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

BLOCK_ROLLOUT_CONFIG_PROVIDER_VALUES: set[BlockRolloutConfigProvider] = {
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


def check_block_rollout_config_provider(value: str) -> BlockRolloutConfigProvider:
    if value in BLOCK_ROLLOUT_CONFIG_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_PROVIDER_VALUES!r}")
