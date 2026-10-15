from typing import Literal

PatchedCertificateRequestKind = Literal["mtls", "tls"]

PATCHED_CERTIFICATE_REQUEST_KIND_VALUES: set[PatchedCertificateRequestKind] = {
    "mtls",
    "tls",
}


def check_patched_certificate_request_kind(value: str) -> PatchedCertificateRequestKind:
    if value in PATCHED_CERTIFICATE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CERTIFICATE_REQUEST_KIND_VALUES!r}")
