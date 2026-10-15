from typing import Literal

DomainRegistrarDetailCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

DOMAIN_REGISTRAR_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[DomainRegistrarDetailCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_domain_registrar_detail_created_by_component_type_1(
    value: str,
) -> DomainRegistrarDetailCreatedByComponentType1:
    if value in DOMAIN_REGISTRAR_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
