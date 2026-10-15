from typing import Literal

PatchedCertificateRequestSource = Literal["discovered", "issued"]

PATCHED_CERTIFICATE_REQUEST_SOURCE_VALUES: set[PatchedCertificateRequestSource] = {
    "discovered",
    "issued",
}


def check_patched_certificate_request_source(value: str) -> PatchedCertificateRequestSource:
    if value in PATCHED_CERTIFICATE_REQUEST_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CERTIFICATE_REQUEST_SOURCE_VALUES!r}")
