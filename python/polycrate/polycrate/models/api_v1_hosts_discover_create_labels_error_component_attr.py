from typing import Literal

ApiV1HostsDiscoverCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_HOSTS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_hosts_discover_create_labels_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateLabelsErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
