from typing import Literal

LbiV2TlsMode = Literal["passthrough", "terminate"]

LBI_V2_TLS_MODE_VALUES: set[LbiV2TlsMode] = {
    "passthrough",
    "terminate",
}


def check_lbi_v2_tls_mode(value: str) -> LbiV2TlsMode:
    if value in LBI_V2_TLS_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_TLS_MODE_VALUES!r}")
