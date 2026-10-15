from typing import Literal

ProviderDetailRequestMinTerm = Literal["", "12m", "3m", "6m", "custom", "none"]

PROVIDER_DETAIL_REQUEST_MIN_TERM_VALUES: set[ProviderDetailRequestMinTerm] = {
    "",
    "12m",
    "3m",
    "6m",
    "custom",
    "none",
}


def check_provider_detail_request_min_term(value: str) -> ProviderDetailRequestMinTerm:
    if value in PROVIDER_DETAIL_REQUEST_MIN_TERM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_MIN_TERM_VALUES!r}")
