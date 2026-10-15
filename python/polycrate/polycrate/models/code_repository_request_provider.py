from typing import Literal

CodeRepositoryRequestProvider = Literal[
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

CODE_REPOSITORY_REQUEST_PROVIDER_VALUES: set[CodeRepositoryRequestProvider] = {
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


def check_code_repository_request_provider(value: str) -> CodeRepositoryRequestProvider:
    if value in CODE_REPOSITORY_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_REQUEST_PROVIDER_VALUES!r}")
