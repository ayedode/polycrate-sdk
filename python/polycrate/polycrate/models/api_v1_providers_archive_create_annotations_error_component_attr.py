from typing import Literal

ApiV1ProvidersArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_providers_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
