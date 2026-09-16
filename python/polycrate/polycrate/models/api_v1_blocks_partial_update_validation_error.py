from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_partial_update_actions_error_component import (
        ApiV1BlocksPartialUpdateActionsErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_actual_availability_error_component import (
        ApiV1BlocksPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_annotations_error_component import (
        ApiV1BlocksPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_app_version_error_component import (
        ApiV1BlocksPartialUpdateAppVersionErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_archived_at_error_component import (
        ApiV1BlocksPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_archived_error_component import (
        ApiV1BlocksPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_archived_reason_error_component import (
        ApiV1BlocksPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_auto_rollout_error_component import (
        ApiV1BlocksPartialUpdateAutoRolloutErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_block_poly_raw_error_component import (
        ApiV1BlocksPartialUpdateBlockPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_changelog_poly_raw_error_component import (
        ApiV1BlocksPartialUpdateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_checksum_error_component import (
        ApiV1BlocksPartialUpdateChecksumErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_config_error_component import (
        ApiV1BlocksPartialUpdateConfigErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_created_by_brc_error_component import (
        ApiV1BlocksPartialUpdateCreatedByBrcErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_created_by_component_error_component import (
        ApiV1BlocksPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_criticality_error_component import (
        ApiV1BlocksPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_debug_mode_error_component import (
        ApiV1BlocksPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_description_error_component import (
        ApiV1BlocksPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_discovery_enabled_error_component import (
        ApiV1BlocksPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_display_name_error_component import (
        ApiV1BlocksPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_documentation_url_error_component import (
        ApiV1BlocksPartialUpdateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_examples_poly_raw_error_component import (
        ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_flavor_error_component import (
        ApiV1BlocksPartialUpdateFlavorErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_from_block_error_component import (
        ApiV1BlocksPartialUpdateFromBlockErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_full_spec_error_component import (
        ApiV1BlocksPartialUpdateFullSpecErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_git_repository_url_error_component import (
        ApiV1BlocksPartialUpdateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_icon_url_error_component import (
        ApiV1BlocksPartialUpdateIconUrlErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_is_behind_stable_error_component import (
        ApiV1BlocksPartialUpdateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_kind_error_component import ApiV1BlocksPartialUpdateKindErrorComponent
    from ..models.api_v1_blocks_partial_update_labels_error_component import (
        ApiV1BlocksPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_latest_stable_error_component import (
        ApiV1BlocksPartialUpdateLatestStableErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_license_error_component import (
        ApiV1BlocksPartialUpdateLicenseErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_license_url_error_component import (
        ApiV1BlocksPartialUpdateLicenseUrlErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_name_error_component import ApiV1BlocksPartialUpdateNameErrorComponent
    from ..models.api_v1_blocks_partial_update_non_field_errors_error_component import (
        ApiV1BlocksPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_platform_service_error_component import (
        ApiV1BlocksPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_provider_error_component import (
        ApiV1BlocksPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_provider_id_error_component import (
        ApiV1BlocksPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_provider_reference_error_component import (
        ApiV1BlocksPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_readme_md_raw_error_component import (
        ApiV1BlocksPartialUpdateReadmeMdRawErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_reconciliation_enabled_error_component import (
        ApiV1BlocksPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_registry_url_error_component import (
        ApiV1BlocksPartialUpdateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_releases_url_error_component import (
        ApiV1BlocksPartialUpdateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_scope_error_component import ApiV1BlocksPartialUpdateScopeErrorComponent
    from ..models.api_v1_blocks_partial_update_sla_availability_error_component import (
        ApiV1BlocksPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_sla_target_error_component import (
        ApiV1BlocksPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_slo_availability_error_component import (
        ApiV1BlocksPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_slo_target_error_component import (
        ApiV1BlocksPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_supports_ha_error_component import (
        ApiV1BlocksPartialUpdateSupportsHaErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_target_availability_error_component import (
        ApiV1BlocksPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_template_block_error_component import (
        ApiV1BlocksPartialUpdateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_template_error_component import (
        ApiV1BlocksPartialUpdateTemplateErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_type_error_component import ApiV1BlocksPartialUpdateTypeErrorComponent
    from ..models.api_v1_blocks_partial_update_user_spec_error_component import (
        ApiV1BlocksPartialUpdateUserSpecErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_version_error_component import (
        ApiV1BlocksPartialUpdateVersionErrorComponent,
    )
    from ..models.api_v1_blocks_partial_update_website_url_error_component import (
        ApiV1BlocksPartialUpdateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlocksPartialUpdateValidationError")


@_attrs_define
class ApiV1BlocksPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksPartialUpdateActionsErrorComponent |
            ApiV1BlocksPartialUpdateActualAvailabilityErrorComponent | ApiV1BlocksPartialUpdateAnnotationsErrorComponent |
            ApiV1BlocksPartialUpdateAppVersionErrorComponent | ApiV1BlocksPartialUpdateArchivedAtErrorComponent |
            ApiV1BlocksPartialUpdateArchivedErrorComponent | ApiV1BlocksPartialUpdateArchivedReasonErrorComponent |
            ApiV1BlocksPartialUpdateAutoRolloutErrorComponent | ApiV1BlocksPartialUpdateBlockPolyRawErrorComponent |
            ApiV1BlocksPartialUpdateChangelogPolyRawErrorComponent | ApiV1BlocksPartialUpdateChecksumErrorComponent |
            ApiV1BlocksPartialUpdateConfigErrorComponent | ApiV1BlocksPartialUpdateCreatedByBrcErrorComponent |
            ApiV1BlocksPartialUpdateCreatedByComponentErrorComponent | ApiV1BlocksPartialUpdateCriticalityErrorComponent |
            ApiV1BlocksPartialUpdateDebugModeErrorComponent | ApiV1BlocksPartialUpdateDescriptionErrorComponent |
            ApiV1BlocksPartialUpdateDiscoveryEnabledErrorComponent | ApiV1BlocksPartialUpdateDisplayNameErrorComponent |
            ApiV1BlocksPartialUpdateDocumentationUrlErrorComponent | ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponent |
            ApiV1BlocksPartialUpdateFlavorErrorComponent | ApiV1BlocksPartialUpdateFromBlockErrorComponent |
            ApiV1BlocksPartialUpdateFullSpecErrorComponent | ApiV1BlocksPartialUpdateGitRepositoryUrlErrorComponent |
            ApiV1BlocksPartialUpdateIconUrlErrorComponent | ApiV1BlocksPartialUpdateIsBehindStableErrorComponent |
            ApiV1BlocksPartialUpdateKindErrorComponent | ApiV1BlocksPartialUpdateLabelsErrorComponent |
            ApiV1BlocksPartialUpdateLatestStableErrorComponent | ApiV1BlocksPartialUpdateLicenseErrorComponent |
            ApiV1BlocksPartialUpdateLicenseUrlErrorComponent | ApiV1BlocksPartialUpdateNameErrorComponent |
            ApiV1BlocksPartialUpdateNonFieldErrorsErrorComponent | ApiV1BlocksPartialUpdatePlatformServiceErrorComponent |
            ApiV1BlocksPartialUpdateProviderErrorComponent | ApiV1BlocksPartialUpdateProviderIdErrorComponent |
            ApiV1BlocksPartialUpdateProviderReferenceErrorComponent | ApiV1BlocksPartialUpdateReadmeMdRawErrorComponent |
            ApiV1BlocksPartialUpdateReconciliationEnabledErrorComponent | ApiV1BlocksPartialUpdateRegistryUrlErrorComponent
            | ApiV1BlocksPartialUpdateReleasesUrlErrorComponent | ApiV1BlocksPartialUpdateScopeErrorComponent |
            ApiV1BlocksPartialUpdateSlaAvailabilityErrorComponent | ApiV1BlocksPartialUpdateSlaTargetErrorComponent |
            ApiV1BlocksPartialUpdateSloAvailabilityErrorComponent | ApiV1BlocksPartialUpdateSloTargetErrorComponent |
            ApiV1BlocksPartialUpdateSupportsHaErrorComponent | ApiV1BlocksPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1BlocksPartialUpdateTemplateBlockErrorComponent | ApiV1BlocksPartialUpdateTemplateErrorComponent |
            ApiV1BlocksPartialUpdateTypeErrorComponent | ApiV1BlocksPartialUpdateUserSpecErrorComponent |
            ApiV1BlocksPartialUpdateVersionErrorComponent | ApiV1BlocksPartialUpdateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksPartialUpdateActionsErrorComponent
        | ApiV1BlocksPartialUpdateActualAvailabilityErrorComponent
        | ApiV1BlocksPartialUpdateAnnotationsErrorComponent
        | ApiV1BlocksPartialUpdateAppVersionErrorComponent
        | ApiV1BlocksPartialUpdateArchivedAtErrorComponent
        | ApiV1BlocksPartialUpdateArchivedErrorComponent
        | ApiV1BlocksPartialUpdateArchivedReasonErrorComponent
        | ApiV1BlocksPartialUpdateAutoRolloutErrorComponent
        | ApiV1BlocksPartialUpdateBlockPolyRawErrorComponent
        | ApiV1BlocksPartialUpdateChangelogPolyRawErrorComponent
        | ApiV1BlocksPartialUpdateChecksumErrorComponent
        | ApiV1BlocksPartialUpdateConfigErrorComponent
        | ApiV1BlocksPartialUpdateCreatedByBrcErrorComponent
        | ApiV1BlocksPartialUpdateCreatedByComponentErrorComponent
        | ApiV1BlocksPartialUpdateCriticalityErrorComponent
        | ApiV1BlocksPartialUpdateDebugModeErrorComponent
        | ApiV1BlocksPartialUpdateDescriptionErrorComponent
        | ApiV1BlocksPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1BlocksPartialUpdateDisplayNameErrorComponent
        | ApiV1BlocksPartialUpdateDocumentationUrlErrorComponent
        | ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponent
        | ApiV1BlocksPartialUpdateFlavorErrorComponent
        | ApiV1BlocksPartialUpdateFromBlockErrorComponent
        | ApiV1BlocksPartialUpdateFullSpecErrorComponent
        | ApiV1BlocksPartialUpdateGitRepositoryUrlErrorComponent
        | ApiV1BlocksPartialUpdateIconUrlErrorComponent
        | ApiV1BlocksPartialUpdateIsBehindStableErrorComponent
        | ApiV1BlocksPartialUpdateKindErrorComponent
        | ApiV1BlocksPartialUpdateLabelsErrorComponent
        | ApiV1BlocksPartialUpdateLatestStableErrorComponent
        | ApiV1BlocksPartialUpdateLicenseErrorComponent
        | ApiV1BlocksPartialUpdateLicenseUrlErrorComponent
        | ApiV1BlocksPartialUpdateNameErrorComponent
        | ApiV1BlocksPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1BlocksPartialUpdatePlatformServiceErrorComponent
        | ApiV1BlocksPartialUpdateProviderErrorComponent
        | ApiV1BlocksPartialUpdateProviderIdErrorComponent
        | ApiV1BlocksPartialUpdateProviderReferenceErrorComponent
        | ApiV1BlocksPartialUpdateReadmeMdRawErrorComponent
        | ApiV1BlocksPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1BlocksPartialUpdateRegistryUrlErrorComponent
        | ApiV1BlocksPartialUpdateReleasesUrlErrorComponent
        | ApiV1BlocksPartialUpdateScopeErrorComponent
        | ApiV1BlocksPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1BlocksPartialUpdateSlaTargetErrorComponent
        | ApiV1BlocksPartialUpdateSloAvailabilityErrorComponent
        | ApiV1BlocksPartialUpdateSloTargetErrorComponent
        | ApiV1BlocksPartialUpdateSupportsHaErrorComponent
        | ApiV1BlocksPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1BlocksPartialUpdateTemplateBlockErrorComponent
        | ApiV1BlocksPartialUpdateTemplateErrorComponent
        | ApiV1BlocksPartialUpdateTypeErrorComponent
        | ApiV1BlocksPartialUpdateUserSpecErrorComponent
        | ApiV1BlocksPartialUpdateVersionErrorComponent
        | ApiV1BlocksPartialUpdateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_partial_update_actions_error_component import (
            ApiV1BlocksPartialUpdateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_actual_availability_error_component import (
            ApiV1BlocksPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_annotations_error_component import (
            ApiV1BlocksPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_app_version_error_component import (
            ApiV1BlocksPartialUpdateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_archived_at_error_component import (
            ApiV1BlocksPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_archived_error_component import (
            ApiV1BlocksPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_archived_reason_error_component import (
            ApiV1BlocksPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_auto_rollout_error_component import (
            ApiV1BlocksPartialUpdateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_block_poly_raw_error_component import (
            ApiV1BlocksPartialUpdateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_changelog_poly_raw_error_component import (
            ApiV1BlocksPartialUpdateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_checksum_error_component import (
            ApiV1BlocksPartialUpdateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_config_error_component import (
            ApiV1BlocksPartialUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_created_by_brc_error_component import (
            ApiV1BlocksPartialUpdateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_criticality_error_component import (
            ApiV1BlocksPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_debug_mode_error_component import (
            ApiV1BlocksPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_description_error_component import (
            ApiV1BlocksPartialUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_discovery_enabled_error_component import (
            ApiV1BlocksPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_display_name_error_component import (
            ApiV1BlocksPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_documentation_url_error_component import (
            ApiV1BlocksPartialUpdateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_examples_poly_raw_error_component import (
            ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_flavor_error_component import (
            ApiV1BlocksPartialUpdateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_from_block_error_component import (
            ApiV1BlocksPartialUpdateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_full_spec_error_component import (
            ApiV1BlocksPartialUpdateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_git_repository_url_error_component import (
            ApiV1BlocksPartialUpdateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_icon_url_error_component import (
            ApiV1BlocksPartialUpdateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_is_behind_stable_error_component import (
            ApiV1BlocksPartialUpdateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_kind_error_component import (
            ApiV1BlocksPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_labels_error_component import (
            ApiV1BlocksPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_latest_stable_error_component import (
            ApiV1BlocksPartialUpdateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_license_error_component import (
            ApiV1BlocksPartialUpdateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_license_url_error_component import (
            ApiV1BlocksPartialUpdateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_name_error_component import (
            ApiV1BlocksPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_non_field_errors_error_component import (
            ApiV1BlocksPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_platform_service_error_component import (
            ApiV1BlocksPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_provider_error_component import (
            ApiV1BlocksPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_provider_id_error_component import (
            ApiV1BlocksPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_provider_reference_error_component import (
            ApiV1BlocksPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_readme_md_raw_error_component import (
            ApiV1BlocksPartialUpdateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_reconciliation_enabled_error_component import (
            ApiV1BlocksPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_registry_url_error_component import (
            ApiV1BlocksPartialUpdateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_releases_url_error_component import (
            ApiV1BlocksPartialUpdateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_scope_error_component import (
            ApiV1BlocksPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_sla_availability_error_component import (
            ApiV1BlocksPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_sla_target_error_component import (
            ApiV1BlocksPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_slo_availability_error_component import (
            ApiV1BlocksPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_slo_target_error_component import (
            ApiV1BlocksPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_supports_ha_error_component import (
            ApiV1BlocksPartialUpdateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_target_availability_error_component import (
            ApiV1BlocksPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_template_block_error_component import (
            ApiV1BlocksPartialUpdateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_template_error_component import (
            ApiV1BlocksPartialUpdateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_type_error_component import (
            ApiV1BlocksPartialUpdateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_user_spec_error_component import (
            ApiV1BlocksPartialUpdateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_version_error_component import (
            ApiV1BlocksPartialUpdateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_website_url_error_component import (
            ApiV1BlocksPartialUpdateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksPartialUpdateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_partial_update_actions_error_component import (
            ApiV1BlocksPartialUpdateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_actual_availability_error_component import (
            ApiV1BlocksPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_annotations_error_component import (
            ApiV1BlocksPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_app_version_error_component import (
            ApiV1BlocksPartialUpdateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_archived_at_error_component import (
            ApiV1BlocksPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_archived_error_component import (
            ApiV1BlocksPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_archived_reason_error_component import (
            ApiV1BlocksPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_auto_rollout_error_component import (
            ApiV1BlocksPartialUpdateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_block_poly_raw_error_component import (
            ApiV1BlocksPartialUpdateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_changelog_poly_raw_error_component import (
            ApiV1BlocksPartialUpdateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_checksum_error_component import (
            ApiV1BlocksPartialUpdateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_config_error_component import (
            ApiV1BlocksPartialUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_created_by_brc_error_component import (
            ApiV1BlocksPartialUpdateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_created_by_component_error_component import (
            ApiV1BlocksPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_criticality_error_component import (
            ApiV1BlocksPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_debug_mode_error_component import (
            ApiV1BlocksPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_description_error_component import (
            ApiV1BlocksPartialUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_discovery_enabled_error_component import (
            ApiV1BlocksPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_display_name_error_component import (
            ApiV1BlocksPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_documentation_url_error_component import (
            ApiV1BlocksPartialUpdateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_examples_poly_raw_error_component import (
            ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_flavor_error_component import (
            ApiV1BlocksPartialUpdateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_from_block_error_component import (
            ApiV1BlocksPartialUpdateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_full_spec_error_component import (
            ApiV1BlocksPartialUpdateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_git_repository_url_error_component import (
            ApiV1BlocksPartialUpdateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_icon_url_error_component import (
            ApiV1BlocksPartialUpdateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_is_behind_stable_error_component import (
            ApiV1BlocksPartialUpdateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_kind_error_component import (
            ApiV1BlocksPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_labels_error_component import (
            ApiV1BlocksPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_latest_stable_error_component import (
            ApiV1BlocksPartialUpdateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_license_error_component import (
            ApiV1BlocksPartialUpdateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_license_url_error_component import (
            ApiV1BlocksPartialUpdateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_name_error_component import (
            ApiV1BlocksPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_non_field_errors_error_component import (
            ApiV1BlocksPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_platform_service_error_component import (
            ApiV1BlocksPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_provider_error_component import (
            ApiV1BlocksPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_provider_id_error_component import (
            ApiV1BlocksPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_provider_reference_error_component import (
            ApiV1BlocksPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_readme_md_raw_error_component import (
            ApiV1BlocksPartialUpdateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_reconciliation_enabled_error_component import (
            ApiV1BlocksPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_registry_url_error_component import (
            ApiV1BlocksPartialUpdateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_releases_url_error_component import (
            ApiV1BlocksPartialUpdateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_scope_error_component import (
            ApiV1BlocksPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_sla_availability_error_component import (
            ApiV1BlocksPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_sla_target_error_component import (
            ApiV1BlocksPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_slo_availability_error_component import (
            ApiV1BlocksPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_slo_target_error_component import (
            ApiV1BlocksPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_supports_ha_error_component import (
            ApiV1BlocksPartialUpdateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_target_availability_error_component import (
            ApiV1BlocksPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_template_block_error_component import (
            ApiV1BlocksPartialUpdateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_template_error_component import (
            ApiV1BlocksPartialUpdateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_type_error_component import (
            ApiV1BlocksPartialUpdateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_user_spec_error_component import (
            ApiV1BlocksPartialUpdateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_version_error_component import (
            ApiV1BlocksPartialUpdateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_partial_update_website_url_error_component import (
            ApiV1BlocksPartialUpdateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksPartialUpdateActionsErrorComponent
                | ApiV1BlocksPartialUpdateActualAvailabilityErrorComponent
                | ApiV1BlocksPartialUpdateAnnotationsErrorComponent
                | ApiV1BlocksPartialUpdateAppVersionErrorComponent
                | ApiV1BlocksPartialUpdateArchivedAtErrorComponent
                | ApiV1BlocksPartialUpdateArchivedErrorComponent
                | ApiV1BlocksPartialUpdateArchivedReasonErrorComponent
                | ApiV1BlocksPartialUpdateAutoRolloutErrorComponent
                | ApiV1BlocksPartialUpdateBlockPolyRawErrorComponent
                | ApiV1BlocksPartialUpdateChangelogPolyRawErrorComponent
                | ApiV1BlocksPartialUpdateChecksumErrorComponent
                | ApiV1BlocksPartialUpdateConfigErrorComponent
                | ApiV1BlocksPartialUpdateCreatedByBrcErrorComponent
                | ApiV1BlocksPartialUpdateCreatedByComponentErrorComponent
                | ApiV1BlocksPartialUpdateCriticalityErrorComponent
                | ApiV1BlocksPartialUpdateDebugModeErrorComponent
                | ApiV1BlocksPartialUpdateDescriptionErrorComponent
                | ApiV1BlocksPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1BlocksPartialUpdateDisplayNameErrorComponent
                | ApiV1BlocksPartialUpdateDocumentationUrlErrorComponent
                | ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponent
                | ApiV1BlocksPartialUpdateFlavorErrorComponent
                | ApiV1BlocksPartialUpdateFromBlockErrorComponent
                | ApiV1BlocksPartialUpdateFullSpecErrorComponent
                | ApiV1BlocksPartialUpdateGitRepositoryUrlErrorComponent
                | ApiV1BlocksPartialUpdateIconUrlErrorComponent
                | ApiV1BlocksPartialUpdateIsBehindStableErrorComponent
                | ApiV1BlocksPartialUpdateKindErrorComponent
                | ApiV1BlocksPartialUpdateLabelsErrorComponent
                | ApiV1BlocksPartialUpdateLatestStableErrorComponent
                | ApiV1BlocksPartialUpdateLicenseErrorComponent
                | ApiV1BlocksPartialUpdateLicenseUrlErrorComponent
                | ApiV1BlocksPartialUpdateNameErrorComponent
                | ApiV1BlocksPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1BlocksPartialUpdatePlatformServiceErrorComponent
                | ApiV1BlocksPartialUpdateProviderErrorComponent
                | ApiV1BlocksPartialUpdateProviderIdErrorComponent
                | ApiV1BlocksPartialUpdateProviderReferenceErrorComponent
                | ApiV1BlocksPartialUpdateReadmeMdRawErrorComponent
                | ApiV1BlocksPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1BlocksPartialUpdateRegistryUrlErrorComponent
                | ApiV1BlocksPartialUpdateReleasesUrlErrorComponent
                | ApiV1BlocksPartialUpdateScopeErrorComponent
                | ApiV1BlocksPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1BlocksPartialUpdateSlaTargetErrorComponent
                | ApiV1BlocksPartialUpdateSloAvailabilityErrorComponent
                | ApiV1BlocksPartialUpdateSloTargetErrorComponent
                | ApiV1BlocksPartialUpdateSupportsHaErrorComponent
                | ApiV1BlocksPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1BlocksPartialUpdateTemplateBlockErrorComponent
                | ApiV1BlocksPartialUpdateTemplateErrorComponent
                | ApiV1BlocksPartialUpdateTypeErrorComponent
                | ApiV1BlocksPartialUpdateUserSpecErrorComponent
                | ApiV1BlocksPartialUpdateVersionErrorComponent
                | ApiV1BlocksPartialUpdateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_0 = (
                        ApiV1BlocksPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_1 = (
                        ApiV1BlocksPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_2 = (
                        ApiV1BlocksPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_3 = (
                        ApiV1BlocksPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_4 = (
                        ApiV1BlocksPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_5 = (
                        ApiV1BlocksPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_6 = (
                        ApiV1BlocksPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_7 = (
                        ApiV1BlocksPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_8 = (
                        ApiV1BlocksPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_9 = (
                        ApiV1BlocksPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_10 = (
                        ApiV1BlocksPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_11 = (
                        ApiV1BlocksPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_12 = (
                        ApiV1BlocksPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_13 = (
                        ApiV1BlocksPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_14 = (
                        ApiV1BlocksPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_15 = (
                        ApiV1BlocksPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_16 = (
                        ApiV1BlocksPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_17 = (
                        ApiV1BlocksPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_18 = (
                        ApiV1BlocksPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_19 = (
                        ApiV1BlocksPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_20 = (
                        ApiV1BlocksPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_21 = (
                        ApiV1BlocksPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_22 = (
                        ApiV1BlocksPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_23 = (
                        ApiV1BlocksPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_24 = (
                        ApiV1BlocksPartialUpdateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_25 = (
                        ApiV1BlocksPartialUpdateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_26 = (
                        ApiV1BlocksPartialUpdateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_27 = (
                        ApiV1BlocksPartialUpdateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_28 = (
                        ApiV1BlocksPartialUpdateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_29 = (
                        ApiV1BlocksPartialUpdateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_30 = (
                        ApiV1BlocksPartialUpdateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_31 = (
                        ApiV1BlocksPartialUpdateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_32 = (
                        ApiV1BlocksPartialUpdateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_33 = (
                        ApiV1BlocksPartialUpdateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_34 = (
                        ApiV1BlocksPartialUpdateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_35 = (
                        ApiV1BlocksPartialUpdateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_36 = (
                        ApiV1BlocksPartialUpdateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_37 = (
                        ApiV1BlocksPartialUpdateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_38 = (
                        ApiV1BlocksPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_39 = (
                        ApiV1BlocksPartialUpdateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_40 = (
                        ApiV1BlocksPartialUpdateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_41 = (
                        ApiV1BlocksPartialUpdateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_42 = (
                        ApiV1BlocksPartialUpdateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_43 = (
                        ApiV1BlocksPartialUpdateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_44 = (
                        ApiV1BlocksPartialUpdateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_45 = (
                        ApiV1BlocksPartialUpdateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_46 = (
                        ApiV1BlocksPartialUpdateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_47 = (
                        ApiV1BlocksPartialUpdateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_48 = (
                        ApiV1BlocksPartialUpdateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_49 = (
                        ApiV1BlocksPartialUpdateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_50 = (
                        ApiV1BlocksPartialUpdateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_51 = (
                        ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_52 = (
                        ApiV1BlocksPartialUpdateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_partial_update_error_type_53 = (
                        ApiV1BlocksPartialUpdateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_partial_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_partial_update_error_type_54 = (
                    ApiV1BlocksPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_partial_update_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_partial_update_validation_error.additional_properties = d
        return api_v1_blocks_partial_update_validation_error

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
