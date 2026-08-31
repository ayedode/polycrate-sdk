from typing import Literal

ApiV1CertificatesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CERTIFICATES_LIST_STATE_VALUES: set[ApiV1CertificatesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_certificates_list_state(value: str) -> ApiV1CertificatesListState:
    if value in API_V1_CERTIFICATES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_STATE_VALUES!r}")
