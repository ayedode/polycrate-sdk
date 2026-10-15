from typing import Literal

DomainRegistrarListKind = Literal["centralnic", "openprovider"]

DOMAIN_REGISTRAR_LIST_KIND_VALUES: set[DomainRegistrarListKind] = {
    "centralnic",
    "openprovider",
}


def check_domain_registrar_list_kind(value: str) -> DomainRegistrarListKind:
    if value in DOMAIN_REGISTRAR_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_LIST_KIND_VALUES!r}")
