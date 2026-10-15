from typing import Literal

PatchedCertificateRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedCertificateRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_certificate_request_criticality_type_2_type_1(
    value: str,
) -> PatchedCertificateRequestCriticalityType2Type1:
    if value in PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
