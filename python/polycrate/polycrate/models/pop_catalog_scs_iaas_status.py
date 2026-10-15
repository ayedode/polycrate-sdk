from typing import Literal

PopCatalogScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

POP_CATALOG_SCS_IAAS_STATUS_VALUES: set[PopCatalogScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_pop_catalog_scs_iaas_status(value: str) -> PopCatalogScsIaasStatus:
    if value in POP_CATALOG_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_SCS_IAAS_STATUS_VALUES!r}")
