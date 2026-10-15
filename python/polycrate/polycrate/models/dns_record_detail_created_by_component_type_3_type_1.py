from typing import Literal

DNSRecordDetailCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[DNSRecordDetailCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_dns_record_detail_created_by_component_type_3_type_1(
    value: str,
) -> DNSRecordDetailCreatedByComponentType3Type1:
    if value in DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
