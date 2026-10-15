from typing import Literal

CertificateCriticalityType2Type1 = Literal["", "high", "low", "medium"]

CERTIFICATE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CertificateCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_certificate_criticality_type_2_type_1(value: str) -> CertificateCriticalityType2Type1:
    if value in CERTIFICATE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
