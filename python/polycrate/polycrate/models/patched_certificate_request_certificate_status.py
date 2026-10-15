from typing import Literal

PatchedCertificateRequestCertificateStatus = Literal["expired", "expiring_soon", "failed", "pending", "ready"]

PATCHED_CERTIFICATE_REQUEST_CERTIFICATE_STATUS_VALUES: set[PatchedCertificateRequestCertificateStatus] = {
    "expired",
    "expiring_soon",
    "failed",
    "pending",
    "ready",
}


def check_patched_certificate_request_certificate_status(value: str) -> PatchedCertificateRequestCertificateStatus:
    if value in PATCHED_CERTIFICATE_REQUEST_CERTIFICATE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CERTIFICATE_REQUEST_CERTIFICATE_STATUS_VALUES!r}"
    )
