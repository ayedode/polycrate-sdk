from typing import Literal

CertificateRequestCertificateStatus = Literal["expired", "expiring_soon", "failed", "pending", "ready"]

CERTIFICATE_REQUEST_CERTIFICATE_STATUS_VALUES: set[CertificateRequestCertificateStatus] = {
    "expired",
    "expiring_soon",
    "failed",
    "pending",
    "ready",
}


def check_certificate_request_certificate_status(value: str) -> CertificateRequestCertificateStatus:
    if value in CERTIFICATE_REQUEST_CERTIFICATE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_REQUEST_CERTIFICATE_STATUS_VALUES!r}")
