from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_loadbalancers_regions_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
