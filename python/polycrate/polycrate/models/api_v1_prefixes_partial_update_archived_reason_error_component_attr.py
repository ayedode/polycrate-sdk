from typing import Literal

ApiV1PrefixesPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_prefixes_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PrefixesPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
