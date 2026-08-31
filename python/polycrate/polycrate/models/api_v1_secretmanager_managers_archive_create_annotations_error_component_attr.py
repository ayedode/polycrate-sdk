from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_secretmanager_managers_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
