from typing import Literal

ProviderDetailScopedApiKeys = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_SCOPED_API_KEYS_VALUES: set[ProviderDetailScopedApiKeys] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_scoped_api_keys(value: str) -> ProviderDetailScopedApiKeys:
    if value in PROVIDER_DETAIL_SCOPED_API_KEYS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_SCOPED_API_KEYS_VALUES!r}")
