from typing import Literal

AlertCategoryRequestProvider = Literal[
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

ALERT_CATEGORY_REQUEST_PROVIDER_VALUES: set[AlertCategoryRequestProvider] = {
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


def check_alert_category_request_provider(value: str) -> AlertCategoryRequestProvider:
    if value in ALERT_CATEGORY_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_REQUEST_PROVIDER_VALUES!r}")
