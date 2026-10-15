from typing import Literal

PatchedRegistrarTLDPriceDetailRequestKind = Literal["generic"]

PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_KIND_VALUES: set[PatchedRegistrarTLDPriceDetailRequestKind] = {
    "generic",
}


def check_patched_registrar_tld_price_detail_request_kind(value: str) -> PatchedRegistrarTLDPriceDetailRequestKind:
    if value in PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_KIND_VALUES!r}"
    )
