from typing import Literal

ApiV1PoliciesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_POLICIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_policies_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1PoliciesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
