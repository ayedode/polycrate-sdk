from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_secretmanager_managers_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
