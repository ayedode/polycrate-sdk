from typing import Literal

PatchedDNSRecordDetailRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

PATCHED_DNS_RECORD_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[
    PatchedDNSRecordDetailRequestCreatedByComponentType2Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_dns_record_detail_request_created_by_component_type_2_type_1(
    value: str,
) -> PatchedDNSRecordDetailRequestCreatedByComponentType2Type1:
    if value in PATCHED_DNS_RECORD_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_RECORD_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
