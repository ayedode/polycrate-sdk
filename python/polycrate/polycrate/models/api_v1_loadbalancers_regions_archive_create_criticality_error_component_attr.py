from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_loadbalancers_regions_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
