from typing import Literal

ApiV1AlertsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_ALERTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsPartialUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_alerts_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
