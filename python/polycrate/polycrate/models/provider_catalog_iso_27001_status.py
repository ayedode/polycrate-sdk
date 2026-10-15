from typing import Literal

ProviderCatalogIso27001Status = Literal["no", "planned", "unknown", "yes"]

PROVIDER_CATALOG_ISO_27001_STATUS_VALUES: set[ProviderCatalogIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_catalog_iso_27001_status(value: str) -> ProviderCatalogIso27001Status:
    if value in PROVIDER_CATALOG_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_CATALOG_ISO_27001_STATUS_VALUES!r}")
