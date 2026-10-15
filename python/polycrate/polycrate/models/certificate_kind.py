from typing import Literal

CertificateKind = Literal["mtls", "tls"]

CERTIFICATE_KIND_VALUES: set[CertificateKind] = {
    "mtls",
    "tls",
}


def check_certificate_kind(value: str) -> CertificateKind:
    if value in CERTIFICATE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_KIND_VALUES!r}")
