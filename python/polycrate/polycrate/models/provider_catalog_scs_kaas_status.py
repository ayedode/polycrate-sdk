from typing import Literal

ProviderCatalogScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

PROVIDER_CATALOG_SCS_KAAS_STATUS_VALUES: set[ProviderCatalogScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_provider_catalog_scs_kaas_status(value: str) -> ProviderCatalogScsKaasStatus:
    if value in PROVIDER_CATALOG_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_CATALOG_SCS_KAAS_STATUS_VALUES!r}")
