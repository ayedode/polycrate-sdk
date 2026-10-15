from typing import Literal

PatchedProviderDetailRequestScopedApiKeys = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_SCOPED_API_KEYS_VALUES: set[PatchedProviderDetailRequestScopedApiKeys] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_scoped_api_keys(value: str) -> PatchedProviderDetailRequestScopedApiKeys:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_SCOPED_API_KEYS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_SCOPED_API_KEYS_VALUES!r}"
    )
