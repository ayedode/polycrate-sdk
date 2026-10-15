from typing import Literal

DomainContactDetailCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

DOMAIN_CONTACT_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[
    DomainContactDetailCreatedByComponentType2Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_domain_contact_detail_created_by_component_type_2_type_1(
    value: str,
) -> DomainContactDetailCreatedByComponentType2Type1:
    if value in DOMAIN_CONTACT_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
