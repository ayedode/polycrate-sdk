from typing import Literal

PatchedDNSRecordDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedDNSRecordDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_dns_record_detail_request_criticality_type_1(
    value: str,
) -> PatchedDNSRecordDetailRequestCriticalityType1:
    if value in PATCHED_DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
