from typing import Literal

ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_block_rollouts_archive_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
