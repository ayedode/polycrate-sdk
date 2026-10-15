from typing import Literal

DomainRegistrarDetailRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    DomainRegistrarDetailRequestCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_domain_registrar_detail_request_created_by_component_type_3_type_1(
    value: str,
) -> DomainRegistrarDetailRequestCreatedByComponentType3Type1:
    if value in DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
