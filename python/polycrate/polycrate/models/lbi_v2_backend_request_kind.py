from typing import Literal

LbiV2BackendRequestKind = Literal["fqdn", "ip"]

LBI_V2_BACKEND_REQUEST_KIND_VALUES: set[LbiV2BackendRequestKind] = {
    "fqdn",
    "ip",
}


def check_lbi_v2_backend_request_kind(value: str) -> LbiV2BackendRequestKind:
    if value in LBI_V2_BACKEND_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_BACKEND_REQUEST_KIND_VALUES!r}")
