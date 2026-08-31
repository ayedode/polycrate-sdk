from typing import Literal

ApiV1RegionsPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_REGIONS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_regions_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
