from typing import Literal

OrganizationRequestCriticalityType1 = Literal["", "high", "low", "medium"]

ORGANIZATION_REQUEST_CRITICALITY_TYPE_1_VALUES: set[OrganizationRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_organization_request_criticality_type_1(value: str) -> OrganizationRequestCriticalityType1:
    if value in ORGANIZATION_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
