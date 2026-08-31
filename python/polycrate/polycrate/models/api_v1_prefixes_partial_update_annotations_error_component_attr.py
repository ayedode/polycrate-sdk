from typing import Literal

ApiV1PrefixesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PREFIXES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_prefixes_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1PrefixesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
