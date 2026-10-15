from typing import Literal

DomainRegistrarDetailRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[
    DomainRegistrarDetailRequestCreatedByComponentType1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_domain_registrar_detail_request_created_by_component_type_1(
    value: str,
) -> DomainRegistrarDetailRequestCreatedByComponentType1:
    if value in DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
