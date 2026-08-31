from typing import Literal

ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollouts_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
