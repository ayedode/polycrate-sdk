from typing import Literal

CertificateSource = Literal["discovered", "issued"]

CERTIFICATE_SOURCE_VALUES: set[CertificateSource] = {
    "discovered",
    "issued",
}


def check_certificate_source(value: str) -> CertificateSource:
    if value in CERTIFICATE_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_SOURCE_VALUES!r}")
