from typing import Literal

DomainContactDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

DOMAIN_CONTACT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[DomainContactDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_domain_contact_detail_request_criticality_type_1(value: str) -> DomainContactDetailRequestCriticalityType1:
    if value in DOMAIN_CONTACT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
