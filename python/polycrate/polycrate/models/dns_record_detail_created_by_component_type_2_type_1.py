from typing import Literal

DNSRecordDetailCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[DNSRecordDetailCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_dns_record_detail_created_by_component_type_2_type_1(
    value: str,
) -> DNSRecordDetailCreatedByComponentType2Type1:
    if value in DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
