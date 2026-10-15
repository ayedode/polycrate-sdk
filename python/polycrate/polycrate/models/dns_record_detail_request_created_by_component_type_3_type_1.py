from typing import Literal

DNSRecordDetailRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

DNS_RECORD_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    DNSRecordDetailRequestCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_dns_record_detail_request_created_by_component_type_3_type_1(
    value: str,
) -> DNSRecordDetailRequestCreatedByComponentType3Type1:
    if value in DNS_RECORD_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
