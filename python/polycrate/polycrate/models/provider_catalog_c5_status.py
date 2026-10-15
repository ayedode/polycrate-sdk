from typing import Literal

ProviderCatalogC5Status = Literal["none", "planned", "typ1", "typ2"]

PROVIDER_CATALOG_C5_STATUS_VALUES: set[ProviderCatalogC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_provider_catalog_c5_status(value: str) -> ProviderCatalogC5Status:
    if value in PROVIDER_CATALOG_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_CATALOG_C5_STATUS_VALUES!r}")
