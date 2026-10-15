from typing import Literal

ProviderDetailScope = Literal["system", "user"]

PROVIDER_DETAIL_SCOPE_VALUES: set[ProviderDetailScope] = {
    "system",
    "user",
}


def check_provider_detail_scope(value: str) -> ProviderDetailScope:
    if value in PROVIDER_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_SCOPE_VALUES!r}")
