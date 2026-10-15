from typing import Literal

PatchedCertificateRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedCertificateRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_certificate_request_criticality_type_1(value: str) -> PatchedCertificateRequestCriticalityType1:
    if value in PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
