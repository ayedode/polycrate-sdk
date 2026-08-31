from typing import Literal

ApiV1ArtifactsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ARTIFACTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_artifacts_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
