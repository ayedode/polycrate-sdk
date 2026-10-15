from typing import Literal

LbiV2TlsRequestMode = Literal["passthrough", "terminate"]

LBI_V2_TLS_REQUEST_MODE_VALUES: set[LbiV2TlsRequestMode] = {
    "passthrough",
    "terminate",
}


def check_lbi_v2_tls_request_mode(value: str) -> LbiV2TlsRequestMode:
    if value in LBI_V2_TLS_REQUEST_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_TLS_REQUEST_MODE_VALUES!r}")
