from typing import Literal

ApiV1PrefixesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PREFIXES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_prefixes_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
