from typing import Literal

LbiV2TlsChallenge = Literal["dns01", "http01"]

LBI_V2_TLS_CHALLENGE_VALUES: set[LbiV2TlsChallenge] = {
    "dns01",
    "http01",
}


def check_lbi_v2_tls_challenge(value: str) -> LbiV2TlsChallenge:
    if value in LBI_V2_TLS_CHALLENGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_TLS_CHALLENGE_VALUES!r}")
