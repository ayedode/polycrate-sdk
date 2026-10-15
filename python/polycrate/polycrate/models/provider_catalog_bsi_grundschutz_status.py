from typing import Literal

ProviderCatalogBsiGrundschutzStatus = Literal["no", "planned", "unknown", "yes"]

PROVIDER_CATALOG_BSI_GRUNDSCHUTZ_STATUS_VALUES: set[ProviderCatalogBsiGrundschutzStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_catalog_bsi_grundschutz_status(value: str) -> ProviderCatalogBsiGrundschutzStatus:
    if value in PROVIDER_CATALOG_BSI_GRUNDSCHUTZ_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_CATALOG_BSI_GRUNDSCHUTZ_STATUS_VALUES!r}")
