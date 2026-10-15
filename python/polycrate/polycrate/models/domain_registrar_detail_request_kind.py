from typing import Literal

DomainRegistrarDetailRequestKind = Literal["centralnic", "openprovider"]

DOMAIN_REGISTRAR_DETAIL_REQUEST_KIND_VALUES: set[DomainRegistrarDetailRequestKind] = {
    "centralnic",
    "openprovider",
}


def check_domain_registrar_detail_request_kind(value: str) -> DomainRegistrarDetailRequestKind:
    if value in DOMAIN_REGISTRAR_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_REQUEST_KIND_VALUES!r}")
