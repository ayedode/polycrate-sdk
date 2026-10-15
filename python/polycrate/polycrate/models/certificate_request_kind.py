from typing import Literal

CertificateRequestKind = Literal["mtls", "tls"]

CERTIFICATE_REQUEST_KIND_VALUES: set[CertificateRequestKind] = {
    "mtls",
    "tls",
}


def check_certificate_request_kind(value: str) -> CertificateRequestKind:
    if value in CERTIFICATE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_REQUEST_KIND_VALUES!r}")
