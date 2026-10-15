from typing import Literal

PatchedRegistrarTLDPriceDetailRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[
    PatchedRegistrarTLDPriceDetailRequestCreatedByComponentType1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_registrar_tld_price_detail_request_created_by_component_type_1(
    value: str,
) -> PatchedRegistrarTLDPriceDetailRequestCreatedByComponentType1:
    if value in PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
