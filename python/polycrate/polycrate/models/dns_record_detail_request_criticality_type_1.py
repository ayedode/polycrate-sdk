from typing import Literal

DNSRecordDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[DNSRecordDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_dns_record_detail_request_criticality_type_1(value: str) -> DNSRecordDetailRequestCriticalityType1:
    if value in DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
