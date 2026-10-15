from typing import Literal

DeliveryControllerRequestProvider = Literal[
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

DELIVERY_CONTROLLER_REQUEST_PROVIDER_VALUES: set[DeliveryControllerRequestProvider] = {
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


def check_delivery_controller_request_provider(value: str) -> DeliveryControllerRequestProvider:
    if value in DELIVERY_CONTROLLER_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_REQUEST_PROVIDER_VALUES!r}")
