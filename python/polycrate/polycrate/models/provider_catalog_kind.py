from typing import Literal

ProviderCatalogKind = Literal["hardware", "infrastructure", "software"]

PROVIDER_CATALOG_KIND_VALUES: set[ProviderCatalogKind] = {
    "hardware",
    "infrastructure",
    "software",
}


def check_provider_catalog_kind(value: str) -> ProviderCatalogKind:
    if value in PROVIDER_CATALOG_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_CATALOG_KIND_VALUES!r}")
