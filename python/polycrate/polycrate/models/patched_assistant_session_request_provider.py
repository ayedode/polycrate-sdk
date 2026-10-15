from typing import Literal

PatchedAssistantSessionRequestProvider = Literal[
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

PATCHED_ASSISTANT_SESSION_REQUEST_PROVIDER_VALUES: set[PatchedAssistantSessionRequestProvider] = {
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


def check_patched_assistant_session_request_provider(value: str) -> PatchedAssistantSessionRequestProvider:
    if value in PATCHED_ASSISTANT_SESSION_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ASSISTANT_SESSION_REQUEST_PROVIDER_VALUES!r}"
    )
