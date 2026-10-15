from typing import Literal

CertificateScope = Literal["system", "user"]

CERTIFICATE_SCOPE_VALUES: set[CertificateScope] = {
    "system",
    "user",
}


def check_certificate_scope(value: str) -> CertificateScope:
    if value in CERTIFICATE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_SCOPE_VALUES!r}")
