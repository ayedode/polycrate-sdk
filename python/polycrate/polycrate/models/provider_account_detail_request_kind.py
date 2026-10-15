from typing import Literal

ProviderAccountDetailRequestKind = Literal["generic"]

PROVIDER_ACCOUNT_DETAIL_REQUEST_KIND_VALUES: set[ProviderAccountDetailRequestKind] = {
    "generic",
}


def check_provider_account_detail_request_kind(value: str) -> ProviderAccountDetailRequestKind:
    if value in PROVIDER_ACCOUNT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_REQUEST_KIND_VALUES!r}")
