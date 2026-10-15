from typing import Literal

DomainContactDetailRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

DOMAIN_CONTACT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    DomainContactDetailRequestCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_domain_contact_detail_request_created_by_component_type_3_type_1(
    value: str,
) -> DomainContactDetailRequestCreatedByComponentType3Type1:
    if value in DOMAIN_CONTACT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
