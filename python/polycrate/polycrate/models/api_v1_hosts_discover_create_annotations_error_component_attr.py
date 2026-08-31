from typing import Literal

ApiV1HostsDiscoverCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_HOSTS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_hosts_discover_create_annotations_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateAnnotationsErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
