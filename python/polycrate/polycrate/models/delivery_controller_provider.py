from typing import Literal

DeliveryControllerProvider = Literal[
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

DELIVERY_CONTROLLER_PROVIDER_VALUES: set[DeliveryControllerProvider] = {
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


def check_delivery_controller_provider(value: str) -> DeliveryControllerProvider:
    if value in DELIVERY_CONTROLLER_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_PROVIDER_VALUES!r}")
