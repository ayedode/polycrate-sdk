from typing import Literal

DomainContactDetailCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

DOMAIN_CONTACT_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    DomainContactDetailCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_domain_contact_detail_created_by_component_type_3_type_1(
    value: str,
) -> DomainContactDetailCreatedByComponentType3Type1:
    if value in DOMAIN_CONTACT_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
