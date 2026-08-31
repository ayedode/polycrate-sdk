from typing import Literal

ApiV1AlertroutersPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alertrouters_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1AlertroutersPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
