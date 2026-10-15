from typing import Literal

PatchedAlertCategoryRequestProvider = Literal[
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

PATCHED_ALERT_CATEGORY_REQUEST_PROVIDER_VALUES: set[PatchedAlertCategoryRequestProvider] = {
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


def check_patched_alert_category_request_provider(value: str) -> PatchedAlertCategoryRequestProvider:
    if value in PATCHED_ALERT_CATEGORY_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_CATEGORY_REQUEST_PROVIDER_VALUES!r}")
