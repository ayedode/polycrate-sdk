from typing import Literal

ApiV1DowntimesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_downtimes_update_annotations_error_component_code(
    value: str,
) -> ApiV1DowntimesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_DOWNTIMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
