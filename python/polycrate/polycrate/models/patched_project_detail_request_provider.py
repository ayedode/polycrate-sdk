from typing import Literal

PatchedProjectDetailRequestProvider = Literal[
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

PATCHED_PROJECT_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedProjectDetailRequestProvider] = {
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


def check_patched_project_detail_request_provider(value: str) -> PatchedProjectDetailRequestProvider:
    if value in PATCHED_PROJECT_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PROJECT_DETAIL_REQUEST_PROVIDER_VALUES!r}")
