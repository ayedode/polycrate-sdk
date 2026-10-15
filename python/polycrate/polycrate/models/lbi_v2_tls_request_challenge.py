from typing import Literal

LbiV2TlsRequestChallenge = Literal["dns01", "http01"]

LBI_V2_TLS_REQUEST_CHALLENGE_VALUES: set[LbiV2TlsRequestChallenge] = {
    "dns01",
    "http01",
}


def check_lbi_v2_tls_request_challenge(value: str) -> LbiV2TlsRequestChallenge:
    if value in LBI_V2_TLS_REQUEST_CHALLENGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_TLS_REQUEST_CHALLENGE_VALUES!r}")
