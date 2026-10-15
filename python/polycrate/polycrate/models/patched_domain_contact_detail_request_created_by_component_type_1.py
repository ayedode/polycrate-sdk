from typing import Literal

PatchedDomainContactDetailRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[
    PatchedDomainContactDetailRequestCreatedByComponentType1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_domain_contact_detail_request_created_by_component_type_1(
    value: str,
) -> PatchedDomainContactDetailRequestCreatedByComponentType1:
    if value in PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
