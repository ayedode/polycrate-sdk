from typing import Literal

PatchedDomainRegistrarDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[
    PatchedDomainRegistrarDetailRequestCriticalityType1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_domain_registrar_detail_request_criticality_type_1(
    value: str,
) -> PatchedDomainRegistrarDetailRequestCriticalityType1:
    if value in PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
