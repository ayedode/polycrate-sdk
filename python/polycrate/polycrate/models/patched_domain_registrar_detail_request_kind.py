from typing import Literal

PatchedDomainRegistrarDetailRequestKind = Literal["centralnic", "openprovider"]

PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_KIND_VALUES: set[PatchedDomainRegistrarDetailRequestKind] = {
    "centralnic",
    "openprovider",
}


def check_patched_domain_registrar_detail_request_kind(value: str) -> PatchedDomainRegistrarDetailRequestKind:
    if value in PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_KIND_VALUES!r}"
    )
