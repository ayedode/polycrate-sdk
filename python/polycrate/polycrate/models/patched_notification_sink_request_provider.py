from typing import Literal

PatchedNotificationSinkRequestProvider = Literal[
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

PATCHED_NOTIFICATION_SINK_REQUEST_PROVIDER_VALUES: set[PatchedNotificationSinkRequestProvider] = {
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


def check_patched_notification_sink_request_provider(value: str) -> PatchedNotificationSinkRequestProvider:
    if value in PATCHED_NOTIFICATION_SINK_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_NOTIFICATION_SINK_REQUEST_PROVIDER_VALUES!r}"
    )
