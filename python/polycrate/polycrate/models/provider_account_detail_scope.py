from typing import Literal

ProviderAccountDetailScope = Literal["system", "user"]

PROVIDER_ACCOUNT_DETAIL_SCOPE_VALUES: set[ProviderAccountDetailScope] = {
    "system",
    "user",
}


def check_provider_account_detail_scope(value: str) -> ProviderAccountDetailScope:
    if value in PROVIDER_ACCOUNT_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_SCOPE_VALUES!r}")
