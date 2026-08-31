from typing import Literal

ApiV1RegionsPartialUpdateStateReasonErrorComponentAttr = Literal["state_reason"]

API_V1_REGIONS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateStateReasonErrorComponentAttr
] = {
    "state_reason",
}


def check_api_v1_regions_partial_update_state_reason_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateStateReasonErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
