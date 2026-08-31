from typing import Literal

ApiV1HostsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_HOSTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_hosts_create_labels_error_component_attr(value: str) -> ApiV1HostsCreateLabelsErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
