from typing import Literal

DNSZoneDetailRequestDnssecAlgorithm = Literal["", "ecdsa256", "ecdsa384", "ed25519", "rsasha256"]

DNS_ZONE_DETAIL_REQUEST_DNSSEC_ALGORITHM_VALUES: set[DNSZoneDetailRequestDnssecAlgorithm] = {
    "",
    "ecdsa256",
    "ecdsa384",
    "ed25519",
    "rsasha256",
}


def check_dns_zone_detail_request_dnssec_algorithm(value: str) -> DNSZoneDetailRequestDnssecAlgorithm:
    if value in DNS_ZONE_DETAIL_REQUEST_DNSSEC_ALGORITHM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_REQUEST_DNSSEC_ALGORITHM_VALUES!r}")
