from typing import Literal

PatchedCertificateRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PatchedCertificateRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_certificate_request_criticality_type_3_type_1(
    value: str,
) -> PatchedCertificateRequestCriticalityType3Type1:
    if value in PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CERTIFICATE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
