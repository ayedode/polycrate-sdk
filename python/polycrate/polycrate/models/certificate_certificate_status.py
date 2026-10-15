from typing import Literal

CertificateCertificateStatus = Literal["expired", "expiring_soon", "failed", "pending", "ready"]

CERTIFICATE_CERTIFICATE_STATUS_VALUES: set[CertificateCertificateStatus] = {
    "expired",
    "expiring_soon",
    "failed",
    "pending",
    "ready",
}


def check_certificate_certificate_status(value: str) -> CertificateCertificateStatus:
    if value in CERTIFICATE_CERTIFICATE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_CERTIFICATE_STATUS_VALUES!r}")
