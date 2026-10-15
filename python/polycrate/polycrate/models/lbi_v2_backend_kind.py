from typing import Literal

LbiV2BackendKind = Literal["fqdn", "ip"]

LBI_V2_BACKEND_KIND_VALUES: set[LbiV2BackendKind] = {
    "fqdn",
    "ip",
}


def check_lbi_v2_backend_kind(value: str) -> LbiV2BackendKind:
    if value in LBI_V2_BACKEND_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_BACKEND_KIND_VALUES!r}")
