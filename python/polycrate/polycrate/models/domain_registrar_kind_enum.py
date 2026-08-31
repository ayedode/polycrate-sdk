from typing import Literal

DomainRegistrarKindEnum = Literal["centralnic"]

DOMAIN_REGISTRAR_KIND_ENUM_VALUES: set[DomainRegistrarKindEnum] = {
    "centralnic",
}


def check_domain_registrar_kind_enum(value: str) -> DomainRegistrarKindEnum:
    if value in DOMAIN_REGISTRAR_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_KIND_ENUM_VALUES!r}")
