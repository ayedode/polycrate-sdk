from typing import Literal

NotificationSinkRequestProvider = Literal[
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

NOTIFICATION_SINK_REQUEST_PROVIDER_VALUES: set[NotificationSinkRequestProvider] = {
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


def check_notification_sink_request_provider(value: str) -> NotificationSinkRequestProvider:
    if value in NOTIFICATION_SINK_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_REQUEST_PROVIDER_VALUES!r}")
