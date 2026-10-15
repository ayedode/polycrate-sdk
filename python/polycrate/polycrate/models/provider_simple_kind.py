from typing import Literal

ProviderSimpleKind = Literal["hardware", "infrastructure", "software"]

PROVIDER_SIMPLE_KIND_VALUES: set[ProviderSimpleKind] = {
    "hardware",
    "infrastructure",
    "software",
}


def check_provider_simple_kind(value: str) -> ProviderSimpleKind:
    if value in PROVIDER_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_SIMPLE_KIND_VALUES!r}")
