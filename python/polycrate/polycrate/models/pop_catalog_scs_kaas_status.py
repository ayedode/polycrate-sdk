from typing import Literal

PopCatalogScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

POP_CATALOG_SCS_KAAS_STATUS_VALUES: set[PopCatalogScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_pop_catalog_scs_kaas_status(value: str) -> PopCatalogScsKaasStatus:
    if value in POP_CATALOG_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_SCS_KAAS_STATUS_VALUES!r}")
