from typing import Literal

DomainPublicDetailCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

DOMAIN_PUBLIC_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[DomainPublicDetailCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_domain_public_detail_created_by_component_type_1(value: str) -> DomainPublicDetailCreatedByComponentType1:
    if value in DOMAIN_PUBLIC_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
