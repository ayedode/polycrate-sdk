from typing import Literal

ApiV1PopsUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_POPS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateArchivedReasonErrorComponentAttr] = {
    "archived_reason",
}


def check_api_v1_pops_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PopsUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
