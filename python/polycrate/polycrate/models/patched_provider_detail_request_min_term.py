from typing import Literal

PatchedProviderDetailRequestMinTerm = Literal["", "12m", "3m", "6m", "custom", "none"]

PATCHED_PROVIDER_DETAIL_REQUEST_MIN_TERM_VALUES: set[PatchedProviderDetailRequestMinTerm] = {
    "",
    "12m",
    "3m",
    "6m",
    "custom",
    "none",
}


def check_patched_provider_detail_request_min_term(value: str) -> PatchedProviderDetailRequestMinTerm:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_MIN_TERM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_MIN_TERM_VALUES!r}")
