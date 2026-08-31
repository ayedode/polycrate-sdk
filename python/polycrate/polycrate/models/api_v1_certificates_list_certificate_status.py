from typing import Literal

ApiV1CertificatesListCertificateStatus = Literal["expired", "expiring_soon", "failed", "pending", "ready"]

API_V1_CERTIFICATES_LIST_CERTIFICATE_STATUS_VALUES: set[ApiV1CertificatesListCertificateStatus] = {
    "expired",
    "expiring_soon",
    "failed",
    "pending",
    "ready",
}


def check_api_v1_certificates_list_certificate_status(value: str) -> ApiV1CertificatesListCertificateStatus:
    if value in API_V1_CERTIFICATES_LIST_CERTIFICATE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_CERTIFICATE_STATUS_VALUES!r}"
    )
