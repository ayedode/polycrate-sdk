from typing import Literal

ProviderDetailRequestScopedApiKeys = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_SCOPED_API_KEYS_VALUES: set[ProviderDetailRequestScopedApiKeys] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_scoped_api_keys(value: str) -> ProviderDetailRequestScopedApiKeys:
    if value in PROVIDER_DETAIL_REQUEST_SCOPED_API_KEYS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_SCOPED_API_KEYS_VALUES!r}")
