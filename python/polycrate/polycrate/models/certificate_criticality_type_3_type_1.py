from typing import Literal

CertificateCriticalityType3Type1 = Literal["", "high", "low", "medium"]

CERTIFICATE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[CertificateCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_certificate_criticality_type_3_type_1(value: str) -> CertificateCriticalityType3Type1:
    if value in CERTIFICATE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
