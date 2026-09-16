from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_update_actions_error_component import ApiV1BlocksUpdateActionsErrorComponent
    from ..models.api_v1_blocks_update_actual_availability_error_component import (
        ApiV1BlocksUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_update_annotations_error_component import ApiV1BlocksUpdateAnnotationsErrorComponent
    from ..models.api_v1_blocks_update_app_version_error_component import ApiV1BlocksUpdateAppVersionErrorComponent
    from ..models.api_v1_blocks_update_archived_at_error_component import ApiV1BlocksUpdateArchivedAtErrorComponent
    from ..models.api_v1_blocks_update_archived_error_component import ApiV1BlocksUpdateArchivedErrorComponent
    from ..models.api_v1_blocks_update_archived_reason_error_component import (
        ApiV1BlocksUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_update_auto_rollout_error_component import ApiV1BlocksUpdateAutoRolloutErrorComponent
    from ..models.api_v1_blocks_update_block_poly_raw_error_component import ApiV1BlocksUpdateBlockPolyRawErrorComponent
    from ..models.api_v1_blocks_update_changelog_poly_raw_error_component import (
        ApiV1BlocksUpdateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_update_checksum_error_component import ApiV1BlocksUpdateChecksumErrorComponent
    from ..models.api_v1_blocks_update_config_error_component import ApiV1BlocksUpdateConfigErrorComponent
    from ..models.api_v1_blocks_update_created_by_brc_error_component import ApiV1BlocksUpdateCreatedByBrcErrorComponent
    from ..models.api_v1_blocks_update_created_by_component_error_component import (
        ApiV1BlocksUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_update_criticality_error_component import ApiV1BlocksUpdateCriticalityErrorComponent
    from ..models.api_v1_blocks_update_debug_mode_error_component import ApiV1BlocksUpdateDebugModeErrorComponent
    from ..models.api_v1_blocks_update_description_error_component import ApiV1BlocksUpdateDescriptionErrorComponent
    from ..models.api_v1_blocks_update_discovery_enabled_error_component import (
        ApiV1BlocksUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_update_display_name_error_component import ApiV1BlocksUpdateDisplayNameErrorComponent
    from ..models.api_v1_blocks_update_documentation_url_error_component import (
        ApiV1BlocksUpdateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_update_examples_poly_raw_error_component import (
        ApiV1BlocksUpdateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_update_flavor_error_component import ApiV1BlocksUpdateFlavorErrorComponent
    from ..models.api_v1_blocks_update_from_block_error_component import ApiV1BlocksUpdateFromBlockErrorComponent
    from ..models.api_v1_blocks_update_full_spec_error_component import ApiV1BlocksUpdateFullSpecErrorComponent
    from ..models.api_v1_blocks_update_git_repository_url_error_component import (
        ApiV1BlocksUpdateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_update_icon_url_error_component import ApiV1BlocksUpdateIconUrlErrorComponent
    from ..models.api_v1_blocks_update_is_behind_stable_error_component import (
        ApiV1BlocksUpdateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_update_kind_error_component import ApiV1BlocksUpdateKindErrorComponent
    from ..models.api_v1_blocks_update_labels_error_component import ApiV1BlocksUpdateLabelsErrorComponent
    from ..models.api_v1_blocks_update_latest_stable_error_component import ApiV1BlocksUpdateLatestStableErrorComponent
    from ..models.api_v1_blocks_update_license_error_component import ApiV1BlocksUpdateLicenseErrorComponent
    from ..models.api_v1_blocks_update_license_url_error_component import ApiV1BlocksUpdateLicenseUrlErrorComponent
    from ..models.api_v1_blocks_update_name_error_component import ApiV1BlocksUpdateNameErrorComponent
    from ..models.api_v1_blocks_update_non_field_errors_error_component import (
        ApiV1BlocksUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_update_platform_service_error_component import (
        ApiV1BlocksUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_update_provider_error_component import ApiV1BlocksUpdateProviderErrorComponent
    from ..models.api_v1_blocks_update_provider_id_error_component import ApiV1BlocksUpdateProviderIdErrorComponent
    from ..models.api_v1_blocks_update_provider_reference_error_component import (
        ApiV1BlocksUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_update_readme_md_raw_error_component import ApiV1BlocksUpdateReadmeMdRawErrorComponent
    from ..models.api_v1_blocks_update_reconciliation_enabled_error_component import (
        ApiV1BlocksUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_update_registry_url_error_component import ApiV1BlocksUpdateRegistryUrlErrorComponent
    from ..models.api_v1_blocks_update_releases_url_error_component import ApiV1BlocksUpdateReleasesUrlErrorComponent
    from ..models.api_v1_blocks_update_scope_error_component import ApiV1BlocksUpdateScopeErrorComponent
    from ..models.api_v1_blocks_update_sla_availability_error_component import (
        ApiV1BlocksUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_update_sla_target_error_component import ApiV1BlocksUpdateSlaTargetErrorComponent
    from ..models.api_v1_blocks_update_slo_availability_error_component import (
        ApiV1BlocksUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_update_slo_target_error_component import ApiV1BlocksUpdateSloTargetErrorComponent
    from ..models.api_v1_blocks_update_supports_ha_error_component import ApiV1BlocksUpdateSupportsHaErrorComponent
    from ..models.api_v1_blocks_update_target_availability_error_component import (
        ApiV1BlocksUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_update_template_block_error_component import (
        ApiV1BlocksUpdateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_update_template_error_component import ApiV1BlocksUpdateTemplateErrorComponent
    from ..models.api_v1_blocks_update_type_error_component import ApiV1BlocksUpdateTypeErrorComponent
    from ..models.api_v1_blocks_update_user_spec_error_component import ApiV1BlocksUpdateUserSpecErrorComponent
    from ..models.api_v1_blocks_update_version_error_component import ApiV1BlocksUpdateVersionErrorComponent
    from ..models.api_v1_blocks_update_website_url_error_component import ApiV1BlocksUpdateWebsiteUrlErrorComponent


T = TypeVar("T", bound="ApiV1BlocksUpdateValidationError")


@_attrs_define
class ApiV1BlocksUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksUpdateActionsErrorComponent | ApiV1BlocksUpdateActualAvailabilityErrorComponent |
            ApiV1BlocksUpdateAnnotationsErrorComponent | ApiV1BlocksUpdateAppVersionErrorComponent |
            ApiV1BlocksUpdateArchivedAtErrorComponent | ApiV1BlocksUpdateArchivedErrorComponent |
            ApiV1BlocksUpdateArchivedReasonErrorComponent | ApiV1BlocksUpdateAutoRolloutErrorComponent |
            ApiV1BlocksUpdateBlockPolyRawErrorComponent | ApiV1BlocksUpdateChangelogPolyRawErrorComponent |
            ApiV1BlocksUpdateChecksumErrorComponent | ApiV1BlocksUpdateConfigErrorComponent |
            ApiV1BlocksUpdateCreatedByBrcErrorComponent | ApiV1BlocksUpdateCreatedByComponentErrorComponent |
            ApiV1BlocksUpdateCriticalityErrorComponent | ApiV1BlocksUpdateDebugModeErrorComponent |
            ApiV1BlocksUpdateDescriptionErrorComponent | ApiV1BlocksUpdateDiscoveryEnabledErrorComponent |
            ApiV1BlocksUpdateDisplayNameErrorComponent | ApiV1BlocksUpdateDocumentationUrlErrorComponent |
            ApiV1BlocksUpdateExamplesPolyRawErrorComponent | ApiV1BlocksUpdateFlavorErrorComponent |
            ApiV1BlocksUpdateFromBlockErrorComponent | ApiV1BlocksUpdateFullSpecErrorComponent |
            ApiV1BlocksUpdateGitRepositoryUrlErrorComponent | ApiV1BlocksUpdateIconUrlErrorComponent |
            ApiV1BlocksUpdateIsBehindStableErrorComponent | ApiV1BlocksUpdateKindErrorComponent |
            ApiV1BlocksUpdateLabelsErrorComponent | ApiV1BlocksUpdateLatestStableErrorComponent |
            ApiV1BlocksUpdateLicenseErrorComponent | ApiV1BlocksUpdateLicenseUrlErrorComponent |
            ApiV1BlocksUpdateNameErrorComponent | ApiV1BlocksUpdateNonFieldErrorsErrorComponent |
            ApiV1BlocksUpdatePlatformServiceErrorComponent | ApiV1BlocksUpdateProviderErrorComponent |
            ApiV1BlocksUpdateProviderIdErrorComponent | ApiV1BlocksUpdateProviderReferenceErrorComponent |
            ApiV1BlocksUpdateReadmeMdRawErrorComponent | ApiV1BlocksUpdateReconciliationEnabledErrorComponent |
            ApiV1BlocksUpdateRegistryUrlErrorComponent | ApiV1BlocksUpdateReleasesUrlErrorComponent |
            ApiV1BlocksUpdateScopeErrorComponent | ApiV1BlocksUpdateSlaAvailabilityErrorComponent |
            ApiV1BlocksUpdateSlaTargetErrorComponent | ApiV1BlocksUpdateSloAvailabilityErrorComponent |
            ApiV1BlocksUpdateSloTargetErrorComponent | ApiV1BlocksUpdateSupportsHaErrorComponent |
            ApiV1BlocksUpdateTargetAvailabilityErrorComponent | ApiV1BlocksUpdateTemplateBlockErrorComponent |
            ApiV1BlocksUpdateTemplateErrorComponent | ApiV1BlocksUpdateTypeErrorComponent |
            ApiV1BlocksUpdateUserSpecErrorComponent | ApiV1BlocksUpdateVersionErrorComponent |
            ApiV1BlocksUpdateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksUpdateActionsErrorComponent
        | ApiV1BlocksUpdateActualAvailabilityErrorComponent
        | ApiV1BlocksUpdateAnnotationsErrorComponent
        | ApiV1BlocksUpdateAppVersionErrorComponent
        | ApiV1BlocksUpdateArchivedAtErrorComponent
        | ApiV1BlocksUpdateArchivedErrorComponent
        | ApiV1BlocksUpdateArchivedReasonErrorComponent
        | ApiV1BlocksUpdateAutoRolloutErrorComponent
        | ApiV1BlocksUpdateBlockPolyRawErrorComponent
        | ApiV1BlocksUpdateChangelogPolyRawErrorComponent
        | ApiV1BlocksUpdateChecksumErrorComponent
        | ApiV1BlocksUpdateConfigErrorComponent
        | ApiV1BlocksUpdateCreatedByBrcErrorComponent
        | ApiV1BlocksUpdateCreatedByComponentErrorComponent
        | ApiV1BlocksUpdateCriticalityErrorComponent
        | ApiV1BlocksUpdateDebugModeErrorComponent
        | ApiV1BlocksUpdateDescriptionErrorComponent
        | ApiV1BlocksUpdateDiscoveryEnabledErrorComponent
        | ApiV1BlocksUpdateDisplayNameErrorComponent
        | ApiV1BlocksUpdateDocumentationUrlErrorComponent
        | ApiV1BlocksUpdateExamplesPolyRawErrorComponent
        | ApiV1BlocksUpdateFlavorErrorComponent
        | ApiV1BlocksUpdateFromBlockErrorComponent
        | ApiV1BlocksUpdateFullSpecErrorComponent
        | ApiV1BlocksUpdateGitRepositoryUrlErrorComponent
        | ApiV1BlocksUpdateIconUrlErrorComponent
        | ApiV1BlocksUpdateIsBehindStableErrorComponent
        | ApiV1BlocksUpdateKindErrorComponent
        | ApiV1BlocksUpdateLabelsErrorComponent
        | ApiV1BlocksUpdateLatestStableErrorComponent
        | ApiV1BlocksUpdateLicenseErrorComponent
        | ApiV1BlocksUpdateLicenseUrlErrorComponent
        | ApiV1BlocksUpdateNameErrorComponent
        | ApiV1BlocksUpdateNonFieldErrorsErrorComponent
        | ApiV1BlocksUpdatePlatformServiceErrorComponent
        | ApiV1BlocksUpdateProviderErrorComponent
        | ApiV1BlocksUpdateProviderIdErrorComponent
        | ApiV1BlocksUpdateProviderReferenceErrorComponent
        | ApiV1BlocksUpdateReadmeMdRawErrorComponent
        | ApiV1BlocksUpdateReconciliationEnabledErrorComponent
        | ApiV1BlocksUpdateRegistryUrlErrorComponent
        | ApiV1BlocksUpdateReleasesUrlErrorComponent
        | ApiV1BlocksUpdateScopeErrorComponent
        | ApiV1BlocksUpdateSlaAvailabilityErrorComponent
        | ApiV1BlocksUpdateSlaTargetErrorComponent
        | ApiV1BlocksUpdateSloAvailabilityErrorComponent
        | ApiV1BlocksUpdateSloTargetErrorComponent
        | ApiV1BlocksUpdateSupportsHaErrorComponent
        | ApiV1BlocksUpdateTargetAvailabilityErrorComponent
        | ApiV1BlocksUpdateTemplateBlockErrorComponent
        | ApiV1BlocksUpdateTemplateErrorComponent
        | ApiV1BlocksUpdateTypeErrorComponent
        | ApiV1BlocksUpdateUserSpecErrorComponent
        | ApiV1BlocksUpdateVersionErrorComponent
        | ApiV1BlocksUpdateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_update_actions_error_component import (
            ApiV1BlocksUpdateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_actual_availability_error_component import (
            ApiV1BlocksUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_annotations_error_component import (
            ApiV1BlocksUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_app_version_error_component import (
            ApiV1BlocksUpdateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_archived_at_error_component import (
            ApiV1BlocksUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_archived_error_component import (
            ApiV1BlocksUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_archived_reason_error_component import (
            ApiV1BlocksUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_auto_rollout_error_component import (
            ApiV1BlocksUpdateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_block_poly_raw_error_component import (
            ApiV1BlocksUpdateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_changelog_poly_raw_error_component import (
            ApiV1BlocksUpdateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_checksum_error_component import (
            ApiV1BlocksUpdateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_config_error_component import (
            ApiV1BlocksUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_created_by_brc_error_component import (
            ApiV1BlocksUpdateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_criticality_error_component import (
            ApiV1BlocksUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_debug_mode_error_component import (
            ApiV1BlocksUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_description_error_component import (
            ApiV1BlocksUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_discovery_enabled_error_component import (
            ApiV1BlocksUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_display_name_error_component import (
            ApiV1BlocksUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_documentation_url_error_component import (
            ApiV1BlocksUpdateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_examples_poly_raw_error_component import (
            ApiV1BlocksUpdateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_flavor_error_component import (
            ApiV1BlocksUpdateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_from_block_error_component import (
            ApiV1BlocksUpdateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_full_spec_error_component import (
            ApiV1BlocksUpdateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_git_repository_url_error_component import (
            ApiV1BlocksUpdateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_icon_url_error_component import (
            ApiV1BlocksUpdateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_is_behind_stable_error_component import (
            ApiV1BlocksUpdateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_kind_error_component import (
            ApiV1BlocksUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_labels_error_component import (
            ApiV1BlocksUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_latest_stable_error_component import (
            ApiV1BlocksUpdateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_license_error_component import (
            ApiV1BlocksUpdateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_license_url_error_component import (
            ApiV1BlocksUpdateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_name_error_component import (
            ApiV1BlocksUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_non_field_errors_error_component import (
            ApiV1BlocksUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_platform_service_error_component import (
            ApiV1BlocksUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_provider_error_component import (
            ApiV1BlocksUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_provider_id_error_component import (
            ApiV1BlocksUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_provider_reference_error_component import (
            ApiV1BlocksUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_readme_md_raw_error_component import (
            ApiV1BlocksUpdateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_reconciliation_enabled_error_component import (
            ApiV1BlocksUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_registry_url_error_component import (
            ApiV1BlocksUpdateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_releases_url_error_component import (
            ApiV1BlocksUpdateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_scope_error_component import (
            ApiV1BlocksUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_sla_availability_error_component import (
            ApiV1BlocksUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_sla_target_error_component import (
            ApiV1BlocksUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_slo_availability_error_component import (
            ApiV1BlocksUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_slo_target_error_component import (
            ApiV1BlocksUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_supports_ha_error_component import (
            ApiV1BlocksUpdateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_target_availability_error_component import (
            ApiV1BlocksUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_template_block_error_component import (
            ApiV1BlocksUpdateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_template_error_component import (
            ApiV1BlocksUpdateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_type_error_component import (
            ApiV1BlocksUpdateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_user_spec_error_component import (
            ApiV1BlocksUpdateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_version_error_component import (
            ApiV1BlocksUpdateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_website_url_error_component import (
            ApiV1BlocksUpdateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksUpdateCreatedByBrcErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_blocks_update_actions_error_component import (
            ApiV1BlocksUpdateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_actual_availability_error_component import (
            ApiV1BlocksUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_annotations_error_component import (
            ApiV1BlocksUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_app_version_error_component import (
            ApiV1BlocksUpdateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_archived_at_error_component import (
            ApiV1BlocksUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_archived_error_component import (
            ApiV1BlocksUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_archived_reason_error_component import (
            ApiV1BlocksUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_auto_rollout_error_component import (
            ApiV1BlocksUpdateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_block_poly_raw_error_component import (
            ApiV1BlocksUpdateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_changelog_poly_raw_error_component import (
            ApiV1BlocksUpdateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_checksum_error_component import (
            ApiV1BlocksUpdateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_config_error_component import (
            ApiV1BlocksUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_created_by_brc_error_component import (
            ApiV1BlocksUpdateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_created_by_component_error_component import (
            ApiV1BlocksUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_criticality_error_component import (
            ApiV1BlocksUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_debug_mode_error_component import (
            ApiV1BlocksUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_description_error_component import (
            ApiV1BlocksUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_discovery_enabled_error_component import (
            ApiV1BlocksUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_display_name_error_component import (
            ApiV1BlocksUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_documentation_url_error_component import (
            ApiV1BlocksUpdateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_examples_poly_raw_error_component import (
            ApiV1BlocksUpdateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_flavor_error_component import (
            ApiV1BlocksUpdateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_from_block_error_component import (
            ApiV1BlocksUpdateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_full_spec_error_component import (
            ApiV1BlocksUpdateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_git_repository_url_error_component import (
            ApiV1BlocksUpdateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_icon_url_error_component import (
            ApiV1BlocksUpdateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_is_behind_stable_error_component import (
            ApiV1BlocksUpdateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_kind_error_component import (
            ApiV1BlocksUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_labels_error_component import (
            ApiV1BlocksUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_latest_stable_error_component import (
            ApiV1BlocksUpdateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_license_error_component import (
            ApiV1BlocksUpdateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_license_url_error_component import (
            ApiV1BlocksUpdateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_name_error_component import (
            ApiV1BlocksUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_non_field_errors_error_component import (
            ApiV1BlocksUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_platform_service_error_component import (
            ApiV1BlocksUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_provider_error_component import (
            ApiV1BlocksUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_provider_id_error_component import (
            ApiV1BlocksUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_provider_reference_error_component import (
            ApiV1BlocksUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_readme_md_raw_error_component import (
            ApiV1BlocksUpdateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_reconciliation_enabled_error_component import (
            ApiV1BlocksUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_registry_url_error_component import (
            ApiV1BlocksUpdateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_releases_url_error_component import (
            ApiV1BlocksUpdateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_scope_error_component import (
            ApiV1BlocksUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_sla_availability_error_component import (
            ApiV1BlocksUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_sla_target_error_component import (
            ApiV1BlocksUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_slo_availability_error_component import (
            ApiV1BlocksUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_slo_target_error_component import (
            ApiV1BlocksUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_supports_ha_error_component import (
            ApiV1BlocksUpdateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_target_availability_error_component import (
            ApiV1BlocksUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_template_block_error_component import (
            ApiV1BlocksUpdateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_template_error_component import (
            ApiV1BlocksUpdateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_type_error_component import (
            ApiV1BlocksUpdateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_user_spec_error_component import (
            ApiV1BlocksUpdateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_version_error_component import (
            ApiV1BlocksUpdateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_update_website_url_error_component import (
            ApiV1BlocksUpdateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksUpdateActionsErrorComponent
                | ApiV1BlocksUpdateActualAvailabilityErrorComponent
                | ApiV1BlocksUpdateAnnotationsErrorComponent
                | ApiV1BlocksUpdateAppVersionErrorComponent
                | ApiV1BlocksUpdateArchivedAtErrorComponent
                | ApiV1BlocksUpdateArchivedErrorComponent
                | ApiV1BlocksUpdateArchivedReasonErrorComponent
                | ApiV1BlocksUpdateAutoRolloutErrorComponent
                | ApiV1BlocksUpdateBlockPolyRawErrorComponent
                | ApiV1BlocksUpdateChangelogPolyRawErrorComponent
                | ApiV1BlocksUpdateChecksumErrorComponent
                | ApiV1BlocksUpdateConfigErrorComponent
                | ApiV1BlocksUpdateCreatedByBrcErrorComponent
                | ApiV1BlocksUpdateCreatedByComponentErrorComponent
                | ApiV1BlocksUpdateCriticalityErrorComponent
                | ApiV1BlocksUpdateDebugModeErrorComponent
                | ApiV1BlocksUpdateDescriptionErrorComponent
                | ApiV1BlocksUpdateDiscoveryEnabledErrorComponent
                | ApiV1BlocksUpdateDisplayNameErrorComponent
                | ApiV1BlocksUpdateDocumentationUrlErrorComponent
                | ApiV1BlocksUpdateExamplesPolyRawErrorComponent
                | ApiV1BlocksUpdateFlavorErrorComponent
                | ApiV1BlocksUpdateFromBlockErrorComponent
                | ApiV1BlocksUpdateFullSpecErrorComponent
                | ApiV1BlocksUpdateGitRepositoryUrlErrorComponent
                | ApiV1BlocksUpdateIconUrlErrorComponent
                | ApiV1BlocksUpdateIsBehindStableErrorComponent
                | ApiV1BlocksUpdateKindErrorComponent
                | ApiV1BlocksUpdateLabelsErrorComponent
                | ApiV1BlocksUpdateLatestStableErrorComponent
                | ApiV1BlocksUpdateLicenseErrorComponent
                | ApiV1BlocksUpdateLicenseUrlErrorComponent
                | ApiV1BlocksUpdateNameErrorComponent
                | ApiV1BlocksUpdateNonFieldErrorsErrorComponent
                | ApiV1BlocksUpdatePlatformServiceErrorComponent
                | ApiV1BlocksUpdateProviderErrorComponent
                | ApiV1BlocksUpdateProviderIdErrorComponent
                | ApiV1BlocksUpdateProviderReferenceErrorComponent
                | ApiV1BlocksUpdateReadmeMdRawErrorComponent
                | ApiV1BlocksUpdateReconciliationEnabledErrorComponent
                | ApiV1BlocksUpdateRegistryUrlErrorComponent
                | ApiV1BlocksUpdateReleasesUrlErrorComponent
                | ApiV1BlocksUpdateScopeErrorComponent
                | ApiV1BlocksUpdateSlaAvailabilityErrorComponent
                | ApiV1BlocksUpdateSlaTargetErrorComponent
                | ApiV1BlocksUpdateSloAvailabilityErrorComponent
                | ApiV1BlocksUpdateSloTargetErrorComponent
                | ApiV1BlocksUpdateSupportsHaErrorComponent
                | ApiV1BlocksUpdateTargetAvailabilityErrorComponent
                | ApiV1BlocksUpdateTemplateBlockErrorComponent
                | ApiV1BlocksUpdateTemplateErrorComponent
                | ApiV1BlocksUpdateTypeErrorComponent
                | ApiV1BlocksUpdateUserSpecErrorComponent
                | ApiV1BlocksUpdateVersionErrorComponent
                | ApiV1BlocksUpdateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_0 = (
                        ApiV1BlocksUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_1 = ApiV1BlocksUpdateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_2 = (
                        ApiV1BlocksUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_3 = (
                        ApiV1BlocksUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_4 = (
                        ApiV1BlocksUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_5 = (
                        ApiV1BlocksUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_6 = (
                        ApiV1BlocksUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_7 = (
                        ApiV1BlocksUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_8 = (
                        ApiV1BlocksUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_9 = (
                        ApiV1BlocksUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_10 = (
                        ApiV1BlocksUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_11 = (
                        ApiV1BlocksUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_12 = (
                        ApiV1BlocksUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_13 = (
                        ApiV1BlocksUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_14 = (
                        ApiV1BlocksUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_15 = (
                        ApiV1BlocksUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_16 = (
                        ApiV1BlocksUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_17 = (
                        ApiV1BlocksUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_18 = (
                        ApiV1BlocksUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_19 = (
                        ApiV1BlocksUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_20 = (
                        ApiV1BlocksUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_21 = (
                        ApiV1BlocksUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_22 = (
                        ApiV1BlocksUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_23 = (
                        ApiV1BlocksUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_24 = (
                        ApiV1BlocksUpdateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_25 = (
                        ApiV1BlocksUpdateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_26 = (
                        ApiV1BlocksUpdateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_27 = (
                        ApiV1BlocksUpdateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_28 = (
                        ApiV1BlocksUpdateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_29 = (
                        ApiV1BlocksUpdateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_30 = (
                        ApiV1BlocksUpdateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_31 = (
                        ApiV1BlocksUpdateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_32 = (
                        ApiV1BlocksUpdateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_33 = (
                        ApiV1BlocksUpdateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_34 = (
                        ApiV1BlocksUpdateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_35 = (
                        ApiV1BlocksUpdateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_36 = (
                        ApiV1BlocksUpdateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_37 = (
                        ApiV1BlocksUpdateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_38 = (
                        ApiV1BlocksUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_39 = (
                        ApiV1BlocksUpdateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_40 = (
                        ApiV1BlocksUpdateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_41 = (
                        ApiV1BlocksUpdateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_42 = (
                        ApiV1BlocksUpdateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_43 = (
                        ApiV1BlocksUpdateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_44 = (
                        ApiV1BlocksUpdateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_45 = (
                        ApiV1BlocksUpdateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_46 = (
                        ApiV1BlocksUpdateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_47 = (
                        ApiV1BlocksUpdateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_48 = (
                        ApiV1BlocksUpdateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_49 = (
                        ApiV1BlocksUpdateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_50 = (
                        ApiV1BlocksUpdateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_51 = (
                        ApiV1BlocksUpdateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_52 = (
                        ApiV1BlocksUpdateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_update_error_type_53 = (
                        ApiV1BlocksUpdateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_update_error_type_54 = (
                    ApiV1BlocksUpdateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_update_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_update_validation_error.additional_properties = d
        return api_v1_blocks_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
