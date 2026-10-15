from typing import Literal

PatchedDNSRecordDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedDNSRecordDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_dns_record_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedDNSRecordDetailRequestCriticalityType3Type1:
    if value in PATCHED_DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
