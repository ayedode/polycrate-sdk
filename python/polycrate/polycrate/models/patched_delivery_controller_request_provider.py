from typing import Literal

PatchedDeliveryControllerRequestProvider = Literal[
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

PATCHED_DELIVERY_CONTROLLER_REQUEST_PROVIDER_VALUES: set[PatchedDeliveryControllerRequestProvider] = {
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


def check_patched_delivery_controller_request_provider(value: str) -> PatchedDeliveryControllerRequestProvider:
    if value in PATCHED_DELIVERY_CONTROLLER_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DELIVERY_CONTROLLER_REQUEST_PROVIDER_VALUES!r}"
    )
