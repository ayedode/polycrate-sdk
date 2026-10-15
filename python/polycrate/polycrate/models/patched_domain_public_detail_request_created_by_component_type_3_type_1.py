from typing import Literal

PatchedDomainPublicDetailRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    PatchedDomainPublicDetailRequestCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_domain_public_detail_request_created_by_component_type_3_type_1(
    value: str,
) -> PatchedDomainPublicDetailRequestCreatedByComponentType3Type1:
    if value in PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
