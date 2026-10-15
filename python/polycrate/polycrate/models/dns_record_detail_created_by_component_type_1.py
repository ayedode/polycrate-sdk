from typing import Literal

DNSRecordDetailCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[DNSRecordDetailCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_dns_record_detail_created_by_component_type_1(value: str) -> DNSRecordDetailCreatedByComponentType1:
    if value in DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
