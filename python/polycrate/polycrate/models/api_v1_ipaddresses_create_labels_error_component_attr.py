from typing import Literal

ApiV1IpaddressesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_IPADDRESSES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_ipaddresses_create_labels_error_component_attr(
    value: str,
) -> ApiV1IpaddressesCreateLabelsErrorComponentAttr:
    if value in API_V1_IPADDRESSES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
