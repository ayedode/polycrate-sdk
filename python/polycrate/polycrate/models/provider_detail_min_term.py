from typing import Literal

ProviderDetailMinTerm = Literal["", "12m", "3m", "6m", "custom", "none"]

PROVIDER_DETAIL_MIN_TERM_VALUES: set[ProviderDetailMinTerm] = {
    "",
    "12m",
    "3m",
    "6m",
    "custom",
    "none",
}


def check_provider_detail_min_term(value: str) -> ProviderDetailMinTerm:
    if value in PROVIDER_DETAIL_MIN_TERM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_MIN_TERM_VALUES!r}")
