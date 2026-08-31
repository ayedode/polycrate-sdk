from typing import Literal

CertificateStatusEnum = Literal["expired", "expiring_soon", "failed", "pending", "ready"]

CERTIFICATE_STATUS_ENUM_VALUES: set[CertificateStatusEnum] = {
    "expired",
    "expiring_soon",
    "failed",
    "pending",
    "ready",
}


def check_certificate_status_enum(value: str) -> CertificateStatusEnum:
    if value in CERTIFICATE_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_STATUS_ENUM_VALUES!r}")
