from typing import Literal

ApiV1ProvidersPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PROVIDERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_providers_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
