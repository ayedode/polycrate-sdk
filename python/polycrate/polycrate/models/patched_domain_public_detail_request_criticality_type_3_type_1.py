from typing import Literal

PatchedDomainPublicDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedDomainPublicDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_domain_public_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedDomainPublicDetailRequestCriticalityType3Type1:
    if value in PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
