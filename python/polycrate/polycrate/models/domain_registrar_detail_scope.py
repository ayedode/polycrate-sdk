from typing import Literal

DomainRegistrarDetailScope = Literal["system", "user"]

DOMAIN_REGISTRAR_DETAIL_SCOPE_VALUES: set[DomainRegistrarDetailScope] = {
    "system",
    "user",
}


def check_domain_registrar_detail_scope(value: str) -> DomainRegistrarDetailScope:
    if value in DOMAIN_REGISTRAR_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_SCOPE_VALUES!r}")
