from typing import Literal

ApiV1IpaddressesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_IPADDRESSES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_ipaddresses_update_labels_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdateLabelsErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
