from typing import Literal

CertificateKindEnum = Literal["mtls", "tls"]

CERTIFICATE_KIND_ENUM_VALUES: set[CertificateKindEnum] = {
    "mtls",
    "tls",
}


def check_certificate_kind_enum(value: str) -> CertificateKindEnum:
    if value in CERTIFICATE_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_KIND_ENUM_VALUES!r}")
