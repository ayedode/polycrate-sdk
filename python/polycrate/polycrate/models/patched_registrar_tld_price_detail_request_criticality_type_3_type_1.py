from typing import Literal

PatchedRegistrarTLDPriceDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedRegistrarTLDPriceDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_registrar_tld_price_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedRegistrarTLDPriceDetailRequestCriticalityType3Type1:
    if value in PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
