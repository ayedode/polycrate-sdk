from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponentAttr = Literal["target_organizations"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponentAttr
] = {
    "target_organizations",
}


def check_api_v1_block_rollout_configs_archive_create_target_organizations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
