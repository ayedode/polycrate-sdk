from typing import Literal

ApiV1PoliciesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_POLICIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_policies_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PoliciesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
