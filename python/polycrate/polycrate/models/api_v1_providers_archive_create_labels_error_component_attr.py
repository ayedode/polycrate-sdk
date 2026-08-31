from typing import Literal

ApiV1ProvidersArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PROVIDERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_providers_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
