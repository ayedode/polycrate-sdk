from typing import Literal

PopCatalogApiType = Literal["custom_rest", "none", "openstack", "proxmox"]

POP_CATALOG_API_TYPE_VALUES: set[PopCatalogApiType] = {
    "custom_rest",
    "none",
    "openstack",
    "proxmox",
}


def check_pop_catalog_api_type(value: str) -> PopCatalogApiType:
    if value in POP_CATALOG_API_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_API_TYPE_VALUES!r}")
