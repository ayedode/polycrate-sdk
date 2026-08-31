from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_loadbalancers_regions_archive_create_description_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
