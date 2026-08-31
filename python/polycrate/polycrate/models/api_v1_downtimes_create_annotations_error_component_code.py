from typing import Literal

ApiV1DowntimesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_downtimes_create_annotations_error_component_code(
    value: str,
) -> ApiV1DowntimesCreateAnnotationsErrorComponentCode:
    if value in API_V1_DOWNTIMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
