from typing import Literal

ApiV1PrefixesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PREFIXES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_prefixes_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PrefixesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PREFIXES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
