from typing import Literal

ApiV1AlertsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsCreateAnnotationsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_alerts_create_annotations_error_component_code(
    value: str,
) -> ApiV1AlertsCreateAnnotationsErrorComponentCode:
    if value in API_V1_ALERTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
