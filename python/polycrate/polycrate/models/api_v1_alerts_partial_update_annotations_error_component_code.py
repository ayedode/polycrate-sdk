from typing import Literal

ApiV1AlertsPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alerts_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
