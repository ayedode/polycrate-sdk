from typing import Literal

ApiV1HostsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_HOSTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsArchiveCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_hosts_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1HostsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
