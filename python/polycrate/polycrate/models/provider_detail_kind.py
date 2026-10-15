from typing import Literal

ProviderDetailKind = Literal["hardware", "infrastructure", "software"]

PROVIDER_DETAIL_KIND_VALUES: set[ProviderDetailKind] = {
    "hardware",
    "infrastructure",
    "software",
}


def check_provider_detail_kind(value: str) -> ProviderDetailKind:
    if value in PROVIDER_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_KIND_VALUES!r}")
