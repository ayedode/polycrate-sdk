from typing import Literal

ProviderCatalogScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

PROVIDER_CATALOG_SCS_IAAS_STATUS_VALUES: set[ProviderCatalogScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_provider_catalog_scs_iaas_status(value: str) -> ProviderCatalogScsIaasStatus:
    if value in PROVIDER_CATALOG_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_CATALOG_SCS_IAAS_STATUS_VALUES!r}")
