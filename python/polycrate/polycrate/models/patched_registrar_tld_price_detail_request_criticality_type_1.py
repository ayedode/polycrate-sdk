from typing import Literal

PatchedRegistrarTLDPriceDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[
    PatchedRegistrarTLDPriceDetailRequestCriticalityType1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_registrar_tld_price_detail_request_criticality_type_1(
    value: str,
) -> PatchedRegistrarTLDPriceDetailRequestCriticalityType1:
    if value in PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
