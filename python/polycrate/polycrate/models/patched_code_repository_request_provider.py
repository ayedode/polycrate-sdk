from typing import Literal

PatchedCodeRepositoryRequestProvider = Literal[
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

PATCHED_CODE_REPOSITORY_REQUEST_PROVIDER_VALUES: set[PatchedCodeRepositoryRequestProvider] = {
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


def check_patched_code_repository_request_provider(value: str) -> PatchedCodeRepositoryRequestProvider:
    if value in PATCHED_CODE_REPOSITORY_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CODE_REPOSITORY_REQUEST_PROVIDER_VALUES!r}")
