from typing import Literal

ApiV1HostsPartialUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_HOSTS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_hosts_partial_update_description_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateDescriptionErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
