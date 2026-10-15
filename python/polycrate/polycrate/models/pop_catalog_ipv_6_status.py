from typing import Literal

PopCatalogIpv6Status = Literal["no", "planned", "unknown", "yes"]

POP_CATALOG_IPV_6_STATUS_VALUES: set[PopCatalogIpv6Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_catalog_ipv_6_status(value: str) -> PopCatalogIpv6Status:
    if value in POP_CATALOG_IPV_6_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_IPV_6_STATUS_VALUES!r}")
