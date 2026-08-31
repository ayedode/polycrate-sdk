from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_repair_create_actions_error_component import (
        ApiV1BlocksRepairCreateActionsErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_actual_availability_error_component import (
        ApiV1BlocksRepairCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_annotations_error_component import (
        ApiV1BlocksRepairCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_app_version_error_component import (
        ApiV1BlocksRepairCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_archived_at_error_component import (
        ApiV1BlocksRepairCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_archived_error_component import (
        ApiV1BlocksRepairCreateArchivedErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_archived_reason_error_component import (
        ApiV1BlocksRepairCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_auto_rollout_error_component import (
        ApiV1BlocksRepairCreateAutoRolloutErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_block_poly_raw_error_component import (
        ApiV1BlocksRepairCreateBlockPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_changelog_poly_raw_error_component import (
        ApiV1BlocksRepairCreateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_checksum_error_component import (
        ApiV1BlocksRepairCreateChecksumErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_config_error_component import ApiV1BlocksRepairCreateConfigErrorComponent
    from ..models.api_v1_blocks_repair_create_created_by_brc_error_component import (
        ApiV1BlocksRepairCreateCreatedByBrcErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_created_by_component_error_component import (
        ApiV1BlocksRepairCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_criticality_error_component import (
        ApiV1BlocksRepairCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_debug_mode_error_component import (
        ApiV1BlocksRepairCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_description_error_component import (
        ApiV1BlocksRepairCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_discovery_enabled_error_component import (
        ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_display_name_error_component import (
        ApiV1BlocksRepairCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_documentation_url_error_component import (
        ApiV1BlocksRepairCreateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_examples_poly_raw_error_component import (
        ApiV1BlocksRepairCreateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_flavor_error_component import ApiV1BlocksRepairCreateFlavorErrorComponent
    from ..models.api_v1_blocks_repair_create_from_block_error_component import (
        ApiV1BlocksRepairCreateFromBlockErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_full_spec_error_component import (
        ApiV1BlocksRepairCreateFullSpecErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_git_repository_url_error_component import (
        ApiV1BlocksRepairCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_icon_url_error_component import (
        ApiV1BlocksRepairCreateIconUrlErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_is_behind_stable_error_component import (
        ApiV1BlocksRepairCreateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_kind_error_component import ApiV1BlocksRepairCreateKindErrorComponent
    from ..models.api_v1_blocks_repair_create_labels_error_component import ApiV1BlocksRepairCreateLabelsErrorComponent
    from ..models.api_v1_blocks_repair_create_latest_stable_error_component import (
        ApiV1BlocksRepairCreateLatestStableErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_license_error_component import (
        ApiV1BlocksRepairCreateLicenseErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_license_url_error_component import (
        ApiV1BlocksRepairCreateLicenseUrlErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_name_error_component import ApiV1BlocksRepairCreateNameErrorComponent
    from ..models.api_v1_blocks_repair_create_non_field_errors_error_component import (
        ApiV1BlocksRepairCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_platform_service_error_component import (
        ApiV1BlocksRepairCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_provider_error_component import (
        ApiV1BlocksRepairCreateProviderErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_provider_id_error_component import (
        ApiV1BlocksRepairCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_provider_reference_error_component import (
        ApiV1BlocksRepairCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_readme_md_raw_error_component import (
        ApiV1BlocksRepairCreateReadmeMdRawErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_reconciliation_enabled_error_component import (
        ApiV1BlocksRepairCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_registry_url_error_component import (
        ApiV1BlocksRepairCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_releases_url_error_component import (
        ApiV1BlocksRepairCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_scope_error_component import ApiV1BlocksRepairCreateScopeErrorComponent
    from ..models.api_v1_blocks_repair_create_sla_availability_error_component import (
        ApiV1BlocksRepairCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_sla_target_error_component import (
        ApiV1BlocksRepairCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_slo_availability_error_component import (
        ApiV1BlocksRepairCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_slo_target_error_component import (
        ApiV1BlocksRepairCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_supports_ha_error_component import (
        ApiV1BlocksRepairCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_target_availability_error_component import (
        ApiV1BlocksRepairCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_template_block_error_component import (
        ApiV1BlocksRepairCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_template_error_component import (
        ApiV1BlocksRepairCreateTemplateErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_type_error_component import ApiV1BlocksRepairCreateTypeErrorComponent
    from ..models.api_v1_blocks_repair_create_user_spec_error_component import (
        ApiV1BlocksRepairCreateUserSpecErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_version_error_component import (
        ApiV1BlocksRepairCreateVersionErrorComponent,
    )
    from ..models.api_v1_blocks_repair_create_website_url_error_component import (
        ApiV1BlocksRepairCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlocksRepairCreateValidationError")


@_attrs_define
class ApiV1BlocksRepairCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksRepairCreateActionsErrorComponent |
            ApiV1BlocksRepairCreateActualAvailabilityErrorComponent | ApiV1BlocksRepairCreateAnnotationsErrorComponent |
            ApiV1BlocksRepairCreateAppVersionErrorComponent | ApiV1BlocksRepairCreateArchivedAtErrorComponent |
            ApiV1BlocksRepairCreateArchivedErrorComponent | ApiV1BlocksRepairCreateArchivedReasonErrorComponent |
            ApiV1BlocksRepairCreateAutoRolloutErrorComponent | ApiV1BlocksRepairCreateBlockPolyRawErrorComponent |
            ApiV1BlocksRepairCreateChangelogPolyRawErrorComponent | ApiV1BlocksRepairCreateChecksumErrorComponent |
            ApiV1BlocksRepairCreateConfigErrorComponent | ApiV1BlocksRepairCreateCreatedByBrcErrorComponent |
            ApiV1BlocksRepairCreateCreatedByComponentErrorComponent | ApiV1BlocksRepairCreateCriticalityErrorComponent |
            ApiV1BlocksRepairCreateDebugModeErrorComponent | ApiV1BlocksRepairCreateDescriptionErrorComponent |
            ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponent | ApiV1BlocksRepairCreateDisplayNameErrorComponent |
            ApiV1BlocksRepairCreateDocumentationUrlErrorComponent | ApiV1BlocksRepairCreateExamplesPolyRawErrorComponent |
            ApiV1BlocksRepairCreateFlavorErrorComponent | ApiV1BlocksRepairCreateFromBlockErrorComponent |
            ApiV1BlocksRepairCreateFullSpecErrorComponent | ApiV1BlocksRepairCreateGitRepositoryUrlErrorComponent |
            ApiV1BlocksRepairCreateIconUrlErrorComponent | ApiV1BlocksRepairCreateIsBehindStableErrorComponent |
            ApiV1BlocksRepairCreateKindErrorComponent | ApiV1BlocksRepairCreateLabelsErrorComponent |
            ApiV1BlocksRepairCreateLatestStableErrorComponent | ApiV1BlocksRepairCreateLicenseErrorComponent |
            ApiV1BlocksRepairCreateLicenseUrlErrorComponent | ApiV1BlocksRepairCreateNameErrorComponent |
            ApiV1BlocksRepairCreateNonFieldErrorsErrorComponent | ApiV1BlocksRepairCreatePlatformServiceErrorComponent |
            ApiV1BlocksRepairCreateProviderErrorComponent | ApiV1BlocksRepairCreateProviderIdErrorComponent |
            ApiV1BlocksRepairCreateProviderReferenceErrorComponent | ApiV1BlocksRepairCreateReadmeMdRawErrorComponent |
            ApiV1BlocksRepairCreateReconciliationEnabledErrorComponent | ApiV1BlocksRepairCreateRegistryUrlErrorComponent |
            ApiV1BlocksRepairCreateReleasesUrlErrorComponent | ApiV1BlocksRepairCreateScopeErrorComponent |
            ApiV1BlocksRepairCreateSlaAvailabilityErrorComponent | ApiV1BlocksRepairCreateSlaTargetErrorComponent |
            ApiV1BlocksRepairCreateSloAvailabilityErrorComponent | ApiV1BlocksRepairCreateSloTargetErrorComponent |
            ApiV1BlocksRepairCreateSupportsHaErrorComponent | ApiV1BlocksRepairCreateTargetAvailabilityErrorComponent |
            ApiV1BlocksRepairCreateTemplateBlockErrorComponent | ApiV1BlocksRepairCreateTemplateErrorComponent |
            ApiV1BlocksRepairCreateTypeErrorComponent | ApiV1BlocksRepairCreateUserSpecErrorComponent |
            ApiV1BlocksRepairCreateVersionErrorComponent | ApiV1BlocksRepairCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksRepairCreateActionsErrorComponent
        | ApiV1BlocksRepairCreateActualAvailabilityErrorComponent
        | ApiV1BlocksRepairCreateAnnotationsErrorComponent
        | ApiV1BlocksRepairCreateAppVersionErrorComponent
        | ApiV1BlocksRepairCreateArchivedAtErrorComponent
        | ApiV1BlocksRepairCreateArchivedErrorComponent
        | ApiV1BlocksRepairCreateArchivedReasonErrorComponent
        | ApiV1BlocksRepairCreateAutoRolloutErrorComponent
        | ApiV1BlocksRepairCreateBlockPolyRawErrorComponent
        | ApiV1BlocksRepairCreateChangelogPolyRawErrorComponent
        | ApiV1BlocksRepairCreateChecksumErrorComponent
        | ApiV1BlocksRepairCreateConfigErrorComponent
        | ApiV1BlocksRepairCreateCreatedByBrcErrorComponent
        | ApiV1BlocksRepairCreateCreatedByComponentErrorComponent
        | ApiV1BlocksRepairCreateCriticalityErrorComponent
        | ApiV1BlocksRepairCreateDebugModeErrorComponent
        | ApiV1BlocksRepairCreateDescriptionErrorComponent
        | ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponent
        | ApiV1BlocksRepairCreateDisplayNameErrorComponent
        | ApiV1BlocksRepairCreateDocumentationUrlErrorComponent
        | ApiV1BlocksRepairCreateExamplesPolyRawErrorComponent
        | ApiV1BlocksRepairCreateFlavorErrorComponent
        | ApiV1BlocksRepairCreateFromBlockErrorComponent
        | ApiV1BlocksRepairCreateFullSpecErrorComponent
        | ApiV1BlocksRepairCreateGitRepositoryUrlErrorComponent
        | ApiV1BlocksRepairCreateIconUrlErrorComponent
        | ApiV1BlocksRepairCreateIsBehindStableErrorComponent
        | ApiV1BlocksRepairCreateKindErrorComponent
        | ApiV1BlocksRepairCreateLabelsErrorComponent
        | ApiV1BlocksRepairCreateLatestStableErrorComponent
        | ApiV1BlocksRepairCreateLicenseErrorComponent
        | ApiV1BlocksRepairCreateLicenseUrlErrorComponent
        | ApiV1BlocksRepairCreateNameErrorComponent
        | ApiV1BlocksRepairCreateNonFieldErrorsErrorComponent
        | ApiV1BlocksRepairCreatePlatformServiceErrorComponent
        | ApiV1BlocksRepairCreateProviderErrorComponent
        | ApiV1BlocksRepairCreateProviderIdErrorComponent
        | ApiV1BlocksRepairCreateProviderReferenceErrorComponent
        | ApiV1BlocksRepairCreateReadmeMdRawErrorComponent
        | ApiV1BlocksRepairCreateReconciliationEnabledErrorComponent
        | ApiV1BlocksRepairCreateRegistryUrlErrorComponent
        | ApiV1BlocksRepairCreateReleasesUrlErrorComponent
        | ApiV1BlocksRepairCreateScopeErrorComponent
        | ApiV1BlocksRepairCreateSlaAvailabilityErrorComponent
        | ApiV1BlocksRepairCreateSlaTargetErrorComponent
        | ApiV1BlocksRepairCreateSloAvailabilityErrorComponent
        | ApiV1BlocksRepairCreateSloTargetErrorComponent
        | ApiV1BlocksRepairCreateSupportsHaErrorComponent
        | ApiV1BlocksRepairCreateTargetAvailabilityErrorComponent
        | ApiV1BlocksRepairCreateTemplateBlockErrorComponent
        | ApiV1BlocksRepairCreateTemplateErrorComponent
        | ApiV1BlocksRepairCreateTypeErrorComponent
        | ApiV1BlocksRepairCreateUserSpecErrorComponent
        | ApiV1BlocksRepairCreateVersionErrorComponent
        | ApiV1BlocksRepairCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_repair_create_actions_error_component import (
            ApiV1BlocksRepairCreateActionsErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_actual_availability_error_component import (
            ApiV1BlocksRepairCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_annotations_error_component import (
            ApiV1BlocksRepairCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_app_version_error_component import (
            ApiV1BlocksRepairCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_archived_at_error_component import (
            ApiV1BlocksRepairCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_archived_error_component import (
            ApiV1BlocksRepairCreateArchivedErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_archived_reason_error_component import (
            ApiV1BlocksRepairCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_auto_rollout_error_component import (
            ApiV1BlocksRepairCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_block_poly_raw_error_component import (
            ApiV1BlocksRepairCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_changelog_poly_raw_error_component import (
            ApiV1BlocksRepairCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_checksum_error_component import (
            ApiV1BlocksRepairCreateChecksumErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_config_error_component import (
            ApiV1BlocksRepairCreateConfigErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_created_by_brc_error_component import (
            ApiV1BlocksRepairCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_criticality_error_component import (
            ApiV1BlocksRepairCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_debug_mode_error_component import (
            ApiV1BlocksRepairCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_description_error_component import (
            ApiV1BlocksRepairCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_discovery_enabled_error_component import (
            ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_display_name_error_component import (
            ApiV1BlocksRepairCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_documentation_url_error_component import (
            ApiV1BlocksRepairCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_examples_poly_raw_error_component import (
            ApiV1BlocksRepairCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_flavor_error_component import (
            ApiV1BlocksRepairCreateFlavorErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_from_block_error_component import (
            ApiV1BlocksRepairCreateFromBlockErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_full_spec_error_component import (
            ApiV1BlocksRepairCreateFullSpecErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_git_repository_url_error_component import (
            ApiV1BlocksRepairCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_icon_url_error_component import (
            ApiV1BlocksRepairCreateIconUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_is_behind_stable_error_component import (
            ApiV1BlocksRepairCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_kind_error_component import ApiV1BlocksRepairCreateKindErrorComponent
        from ..models.api_v1_blocks_repair_create_labels_error_component import (
            ApiV1BlocksRepairCreateLabelsErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_latest_stable_error_component import (
            ApiV1BlocksRepairCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_license_error_component import (
            ApiV1BlocksRepairCreateLicenseErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_license_url_error_component import (
            ApiV1BlocksRepairCreateLicenseUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_name_error_component import ApiV1BlocksRepairCreateNameErrorComponent
        from ..models.api_v1_blocks_repair_create_non_field_errors_error_component import (
            ApiV1BlocksRepairCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_platform_service_error_component import (
            ApiV1BlocksRepairCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_provider_error_component import (
            ApiV1BlocksRepairCreateProviderErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_provider_id_error_component import (
            ApiV1BlocksRepairCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_provider_reference_error_component import (
            ApiV1BlocksRepairCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_readme_md_raw_error_component import (
            ApiV1BlocksRepairCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_reconciliation_enabled_error_component import (
            ApiV1BlocksRepairCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_registry_url_error_component import (
            ApiV1BlocksRepairCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_releases_url_error_component import (
            ApiV1BlocksRepairCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_scope_error_component import (
            ApiV1BlocksRepairCreateScopeErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_sla_availability_error_component import (
            ApiV1BlocksRepairCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_sla_target_error_component import (
            ApiV1BlocksRepairCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_slo_availability_error_component import (
            ApiV1BlocksRepairCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_slo_target_error_component import (
            ApiV1BlocksRepairCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_supports_ha_error_component import (
            ApiV1BlocksRepairCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_target_availability_error_component import (
            ApiV1BlocksRepairCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_template_block_error_component import (
            ApiV1BlocksRepairCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_template_error_component import (
            ApiV1BlocksRepairCreateTemplateErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_type_error_component import ApiV1BlocksRepairCreateTypeErrorComponent
        from ..models.api_v1_blocks_repair_create_user_spec_error_component import (
            ApiV1BlocksRepairCreateUserSpecErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_version_error_component import (
            ApiV1BlocksRepairCreateVersionErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_website_url_error_component import (
            ApiV1BlocksRepairCreateWebsiteUrlErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksRepairCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRepairCreateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_repair_create_actions_error_component import (
            ApiV1BlocksRepairCreateActionsErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_actual_availability_error_component import (
            ApiV1BlocksRepairCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_annotations_error_component import (
            ApiV1BlocksRepairCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_app_version_error_component import (
            ApiV1BlocksRepairCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_archived_at_error_component import (
            ApiV1BlocksRepairCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_archived_error_component import (
            ApiV1BlocksRepairCreateArchivedErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_archived_reason_error_component import (
            ApiV1BlocksRepairCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_auto_rollout_error_component import (
            ApiV1BlocksRepairCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_block_poly_raw_error_component import (
            ApiV1BlocksRepairCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_changelog_poly_raw_error_component import (
            ApiV1BlocksRepairCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_checksum_error_component import (
            ApiV1BlocksRepairCreateChecksumErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_config_error_component import (
            ApiV1BlocksRepairCreateConfigErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_created_by_brc_error_component import (
            ApiV1BlocksRepairCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_created_by_component_error_component import (
            ApiV1BlocksRepairCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_criticality_error_component import (
            ApiV1BlocksRepairCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_debug_mode_error_component import (
            ApiV1BlocksRepairCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_description_error_component import (
            ApiV1BlocksRepairCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_discovery_enabled_error_component import (
            ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_display_name_error_component import (
            ApiV1BlocksRepairCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_documentation_url_error_component import (
            ApiV1BlocksRepairCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_examples_poly_raw_error_component import (
            ApiV1BlocksRepairCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_flavor_error_component import (
            ApiV1BlocksRepairCreateFlavorErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_from_block_error_component import (
            ApiV1BlocksRepairCreateFromBlockErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_full_spec_error_component import (
            ApiV1BlocksRepairCreateFullSpecErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_git_repository_url_error_component import (
            ApiV1BlocksRepairCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_icon_url_error_component import (
            ApiV1BlocksRepairCreateIconUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_is_behind_stable_error_component import (
            ApiV1BlocksRepairCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_kind_error_component import ApiV1BlocksRepairCreateKindErrorComponent
        from ..models.api_v1_blocks_repair_create_labels_error_component import (
            ApiV1BlocksRepairCreateLabelsErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_latest_stable_error_component import (
            ApiV1BlocksRepairCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_license_error_component import (
            ApiV1BlocksRepairCreateLicenseErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_license_url_error_component import (
            ApiV1BlocksRepairCreateLicenseUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_name_error_component import ApiV1BlocksRepairCreateNameErrorComponent
        from ..models.api_v1_blocks_repair_create_non_field_errors_error_component import (
            ApiV1BlocksRepairCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_platform_service_error_component import (
            ApiV1BlocksRepairCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_provider_error_component import (
            ApiV1BlocksRepairCreateProviderErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_provider_id_error_component import (
            ApiV1BlocksRepairCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_provider_reference_error_component import (
            ApiV1BlocksRepairCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_readme_md_raw_error_component import (
            ApiV1BlocksRepairCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_reconciliation_enabled_error_component import (
            ApiV1BlocksRepairCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_registry_url_error_component import (
            ApiV1BlocksRepairCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_releases_url_error_component import (
            ApiV1BlocksRepairCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_scope_error_component import (
            ApiV1BlocksRepairCreateScopeErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_sla_availability_error_component import (
            ApiV1BlocksRepairCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_sla_target_error_component import (
            ApiV1BlocksRepairCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_slo_availability_error_component import (
            ApiV1BlocksRepairCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_slo_target_error_component import (
            ApiV1BlocksRepairCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_supports_ha_error_component import (
            ApiV1BlocksRepairCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_target_availability_error_component import (
            ApiV1BlocksRepairCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_template_block_error_component import (
            ApiV1BlocksRepairCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_template_error_component import (
            ApiV1BlocksRepairCreateTemplateErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_type_error_component import ApiV1BlocksRepairCreateTypeErrorComponent
        from ..models.api_v1_blocks_repair_create_user_spec_error_component import (
            ApiV1BlocksRepairCreateUserSpecErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_version_error_component import (
            ApiV1BlocksRepairCreateVersionErrorComponent,
        )
        from ..models.api_v1_blocks_repair_create_website_url_error_component import (
            ApiV1BlocksRepairCreateWebsiteUrlErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksRepairCreateActionsErrorComponent
                | ApiV1BlocksRepairCreateActualAvailabilityErrorComponent
                | ApiV1BlocksRepairCreateAnnotationsErrorComponent
                | ApiV1BlocksRepairCreateAppVersionErrorComponent
                | ApiV1BlocksRepairCreateArchivedAtErrorComponent
                | ApiV1BlocksRepairCreateArchivedErrorComponent
                | ApiV1BlocksRepairCreateArchivedReasonErrorComponent
                | ApiV1BlocksRepairCreateAutoRolloutErrorComponent
                | ApiV1BlocksRepairCreateBlockPolyRawErrorComponent
                | ApiV1BlocksRepairCreateChangelogPolyRawErrorComponent
                | ApiV1BlocksRepairCreateChecksumErrorComponent
                | ApiV1BlocksRepairCreateConfigErrorComponent
                | ApiV1BlocksRepairCreateCreatedByBrcErrorComponent
                | ApiV1BlocksRepairCreateCreatedByComponentErrorComponent
                | ApiV1BlocksRepairCreateCriticalityErrorComponent
                | ApiV1BlocksRepairCreateDebugModeErrorComponent
                | ApiV1BlocksRepairCreateDescriptionErrorComponent
                | ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponent
                | ApiV1BlocksRepairCreateDisplayNameErrorComponent
                | ApiV1BlocksRepairCreateDocumentationUrlErrorComponent
                | ApiV1BlocksRepairCreateExamplesPolyRawErrorComponent
                | ApiV1BlocksRepairCreateFlavorErrorComponent
                | ApiV1BlocksRepairCreateFromBlockErrorComponent
                | ApiV1BlocksRepairCreateFullSpecErrorComponent
                | ApiV1BlocksRepairCreateGitRepositoryUrlErrorComponent
                | ApiV1BlocksRepairCreateIconUrlErrorComponent
                | ApiV1BlocksRepairCreateIsBehindStableErrorComponent
                | ApiV1BlocksRepairCreateKindErrorComponent
                | ApiV1BlocksRepairCreateLabelsErrorComponent
                | ApiV1BlocksRepairCreateLatestStableErrorComponent
                | ApiV1BlocksRepairCreateLicenseErrorComponent
                | ApiV1BlocksRepairCreateLicenseUrlErrorComponent
                | ApiV1BlocksRepairCreateNameErrorComponent
                | ApiV1BlocksRepairCreateNonFieldErrorsErrorComponent
                | ApiV1BlocksRepairCreatePlatformServiceErrorComponent
                | ApiV1BlocksRepairCreateProviderErrorComponent
                | ApiV1BlocksRepairCreateProviderIdErrorComponent
                | ApiV1BlocksRepairCreateProviderReferenceErrorComponent
                | ApiV1BlocksRepairCreateReadmeMdRawErrorComponent
                | ApiV1BlocksRepairCreateReconciliationEnabledErrorComponent
                | ApiV1BlocksRepairCreateRegistryUrlErrorComponent
                | ApiV1BlocksRepairCreateReleasesUrlErrorComponent
                | ApiV1BlocksRepairCreateScopeErrorComponent
                | ApiV1BlocksRepairCreateSlaAvailabilityErrorComponent
                | ApiV1BlocksRepairCreateSlaTargetErrorComponent
                | ApiV1BlocksRepairCreateSloAvailabilityErrorComponent
                | ApiV1BlocksRepairCreateSloTargetErrorComponent
                | ApiV1BlocksRepairCreateSupportsHaErrorComponent
                | ApiV1BlocksRepairCreateTargetAvailabilityErrorComponent
                | ApiV1BlocksRepairCreateTemplateBlockErrorComponent
                | ApiV1BlocksRepairCreateTemplateErrorComponent
                | ApiV1BlocksRepairCreateTypeErrorComponent
                | ApiV1BlocksRepairCreateUserSpecErrorComponent
                | ApiV1BlocksRepairCreateVersionErrorComponent
                | ApiV1BlocksRepairCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_0 = (
                        ApiV1BlocksRepairCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_1 = (
                        ApiV1BlocksRepairCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_2 = (
                        ApiV1BlocksRepairCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_3 = (
                        ApiV1BlocksRepairCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_4 = (
                        ApiV1BlocksRepairCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_5 = (
                        ApiV1BlocksRepairCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_6 = (
                        ApiV1BlocksRepairCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_7 = (
                        ApiV1BlocksRepairCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_8 = (
                        ApiV1BlocksRepairCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_9 = (
                        ApiV1BlocksRepairCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_10 = (
                        ApiV1BlocksRepairCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_11 = (
                        ApiV1BlocksRepairCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_12 = (
                        ApiV1BlocksRepairCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_13 = (
                        ApiV1BlocksRepairCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_14 = (
                        ApiV1BlocksRepairCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_15 = (
                        ApiV1BlocksRepairCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_16 = (
                        ApiV1BlocksRepairCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_17 = (
                        ApiV1BlocksRepairCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_18 = (
                        ApiV1BlocksRepairCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_19 = (
                        ApiV1BlocksRepairCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_20 = (
                        ApiV1BlocksRepairCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_21 = (
                        ApiV1BlocksRepairCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_22 = (
                        ApiV1BlocksRepairCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_23 = (
                        ApiV1BlocksRepairCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_24 = (
                        ApiV1BlocksRepairCreateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_25 = (
                        ApiV1BlocksRepairCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_26 = (
                        ApiV1BlocksRepairCreateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_27 = (
                        ApiV1BlocksRepairCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_28 = (
                        ApiV1BlocksRepairCreateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_29 = (
                        ApiV1BlocksRepairCreateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_30 = (
                        ApiV1BlocksRepairCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_31 = (
                        ApiV1BlocksRepairCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_32 = (
                        ApiV1BlocksRepairCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_33 = (
                        ApiV1BlocksRepairCreateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_34 = (
                        ApiV1BlocksRepairCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_35 = (
                        ApiV1BlocksRepairCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_36 = (
                        ApiV1BlocksRepairCreateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_37 = (
                        ApiV1BlocksRepairCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_38 = (
                        ApiV1BlocksRepairCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_39 = (
                        ApiV1BlocksRepairCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_40 = (
                        ApiV1BlocksRepairCreateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_41 = (
                        ApiV1BlocksRepairCreateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_42 = (
                        ApiV1BlocksRepairCreateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_43 = (
                        ApiV1BlocksRepairCreateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_44 = (
                        ApiV1BlocksRepairCreateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_45 = (
                        ApiV1BlocksRepairCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_46 = (
                        ApiV1BlocksRepairCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_47 = (
                        ApiV1BlocksRepairCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_48 = (
                        ApiV1BlocksRepairCreateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_49 = (
                        ApiV1BlocksRepairCreateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_50 = (
                        ApiV1BlocksRepairCreateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_51 = (
                        ApiV1BlocksRepairCreateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_52 = (
                        ApiV1BlocksRepairCreateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_repair_create_error_type_53 = (
                        ApiV1BlocksRepairCreateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_repair_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_repair_create_error_type_54 = (
                    ApiV1BlocksRepairCreateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_repair_create_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_repair_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_repair_create_validation_error.additional_properties = d
        return api_v1_blocks_repair_create_validation_error

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
