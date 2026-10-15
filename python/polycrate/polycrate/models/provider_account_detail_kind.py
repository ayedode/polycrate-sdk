from typing import Literal

ProviderAccountDetailKind = Literal["generic"]

PROVIDER_ACCOUNT_DETAIL_KIND_VALUES: set[ProviderAccountDetailKind] = {
    "generic",
}


def check_provider_account_detail_kind(value: str) -> ProviderAccountDetailKind:
    if value in PROVIDER_ACCOUNT_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_KIND_VALUES!r}")
