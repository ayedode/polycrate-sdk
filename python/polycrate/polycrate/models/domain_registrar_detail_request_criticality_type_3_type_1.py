from typing import Literal

DomainRegistrarDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

DOMAIN_REGISTRAR_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    DomainRegistrarDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_domain_registrar_detail_request_criticality_type_3_type_1(
    value: str,
) -> DomainRegistrarDetailRequestCriticalityType3Type1:
    if value in DOMAIN_REGISTRAR_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
