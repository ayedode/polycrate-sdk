from typing import Literal

CertificateRequestSource = Literal["discovered", "issued"]

CERTIFICATE_REQUEST_SOURCE_VALUES: set[CertificateRequestSource] = {
    "discovered",
    "issued",
}


def check_certificate_request_source(value: str) -> CertificateRequestSource:
    if value in CERTIFICATE_REQUEST_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_REQUEST_SOURCE_VALUES!r}")
