from typing import Literal

ApiV1CertificatesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CERTIFICATES_LIST_STATE_NOT_VALUES: set[ApiV1CertificatesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_certificates_list_state_not(value: str) -> ApiV1CertificatesListStateNot:
    if value in API_V1_CERTIFICATES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_STATE_NOT_VALUES!r}")
