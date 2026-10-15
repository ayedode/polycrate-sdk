from typing import Literal

DomainRegistrarSimpleKind = Literal["centralnic", "openprovider"]

DOMAIN_REGISTRAR_SIMPLE_KIND_VALUES: set[DomainRegistrarSimpleKind] = {
    "centralnic",
    "openprovider",
}


def check_domain_registrar_simple_kind(value: str) -> DomainRegistrarSimpleKind:
    if value in DOMAIN_REGISTRAR_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_SIMPLE_KIND_VALUES!r}")
