from typing import Literal

PatchedDNSZoneDetailRequestDnssecAlgorithm = Literal["", "ecdsa256", "ecdsa384", "ed25519", "rsasha256"]

PATCHED_DNS_ZONE_DETAIL_REQUEST_DNSSEC_ALGORITHM_VALUES: set[PatchedDNSZoneDetailRequestDnssecAlgorithm] = {
    "",
    "ecdsa256",
    "ecdsa384",
    "ed25519",
    "rsasha256",
}


def check_patched_dns_zone_detail_request_dnssec_algorithm(value: str) -> PatchedDNSZoneDetailRequestDnssecAlgorithm:
    if value in PATCHED_DNS_ZONE_DETAIL_REQUEST_DNSSEC_ALGORITHM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_ZONE_DETAIL_REQUEST_DNSSEC_ALGORITHM_VALUES!r}"
    )
