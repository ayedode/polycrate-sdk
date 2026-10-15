from typing import Literal

PatchedDomainRegistrarDetailRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[
    PatchedDomainRegistrarDetailRequestCreatedByComponentType2Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_domain_registrar_detail_request_created_by_component_type_2_type_1(
    value: str,
) -> PatchedDomainRegistrarDetailRequestCreatedByComponentType2Type1:
    if value in PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
