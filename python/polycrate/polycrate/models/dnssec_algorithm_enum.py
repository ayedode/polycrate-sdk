from typing import Literal

DnssecAlgorithmEnum = Literal["ecdsa256", "ecdsa384", "ed25519", "rsasha256"]

DNSSEC_ALGORITHM_ENUM_VALUES: set[DnssecAlgorithmEnum] = {
    "ecdsa256",
    "ecdsa384",
    "ed25519",
    "rsasha256",
}


def check_dnssec_algorithm_enum(value: str) -> DnssecAlgorithmEnum:
    if value in DNSSEC_ALGORITHM_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNSSEC_ALGORITHM_ENUM_VALUES!r}")
