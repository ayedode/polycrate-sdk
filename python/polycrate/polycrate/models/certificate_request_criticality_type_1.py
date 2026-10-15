from typing import Literal

CertificateRequestCriticalityType1 = Literal["", "high", "low", "medium"]

CERTIFICATE_REQUEST_CRITICALITY_TYPE_1_VALUES: set[CertificateRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_certificate_request_criticality_type_1(value: str) -> CertificateRequestCriticalityType1:
    if value in CERTIFICATE_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
