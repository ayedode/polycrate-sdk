from typing import Literal

DomainRegistrarDetailKind = Literal["centralnic", "openprovider"]

DOMAIN_REGISTRAR_DETAIL_KIND_VALUES: set[DomainRegistrarDetailKind] = {
    "centralnic",
    "openprovider",
}


def check_domain_registrar_detail_kind(value: str) -> DomainRegistrarDetailKind:
    if value in DOMAIN_REGISTRAR_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_KIND_VALUES!r}")
