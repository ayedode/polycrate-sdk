from typing import Literal

DNSRecordDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[DNSRecordDetailRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_dns_record_detail_request_criticality_type_2_type_1(
    value: str,
) -> DNSRecordDetailRequestCriticalityType2Type1:
    if value in DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
