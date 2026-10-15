from typing import Literal

PatchedS3ClusterRequestProvider = Literal[
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

PATCHED_S3_CLUSTER_REQUEST_PROVIDER_VALUES: set[PatchedS3ClusterRequestProvider] = {
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


def check_patched_s3_cluster_request_provider(value: str) -> PatchedS3ClusterRequestProvider:
    if value in PATCHED_S3_CLUSTER_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_S3_CLUSTER_REQUEST_PROVIDER_VALUES!r}")
