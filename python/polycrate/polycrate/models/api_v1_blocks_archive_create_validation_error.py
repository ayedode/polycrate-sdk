from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_archive_create_actions_error_component import (
        ApiV1BlocksArchiveCreateActionsErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_actual_availability_error_component import (
        ApiV1BlocksArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_annotations_error_component import (
        ApiV1BlocksArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_app_version_error_component import (
        ApiV1BlocksArchiveCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_archived_at_error_component import (
        ApiV1BlocksArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_archived_error_component import (
        ApiV1BlocksArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_archived_reason_error_component import (
        ApiV1BlocksArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_auto_rollout_error_component import (
        ApiV1BlocksArchiveCreateAutoRolloutErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_block_poly_raw_error_component import (
        ApiV1BlocksArchiveCreateBlockPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_changelog_poly_raw_error_component import (
        ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_checksum_error_component import (
        ApiV1BlocksArchiveCreateChecksumErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_config_error_component import (
        ApiV1BlocksArchiveCreateConfigErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_created_by_brc_error_component import (
        ApiV1BlocksArchiveCreateCreatedByBrcErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_created_by_component_error_component import (
        ApiV1BlocksArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_criticality_error_component import (
        ApiV1BlocksArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_debug_mode_error_component import (
        ApiV1BlocksArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_description_error_component import (
        ApiV1BlocksArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_discovery_enabled_error_component import (
        ApiV1BlocksArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_display_name_error_component import (
        ApiV1BlocksArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_documentation_url_error_component import (
        ApiV1BlocksArchiveCreateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_examples_poly_raw_error_component import (
        ApiV1BlocksArchiveCreateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_flavor_error_component import (
        ApiV1BlocksArchiveCreateFlavorErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_from_block_error_component import (
        ApiV1BlocksArchiveCreateFromBlockErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_full_spec_error_component import (
        ApiV1BlocksArchiveCreateFullSpecErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_git_repository_url_error_component import (
        ApiV1BlocksArchiveCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_icon_url_error_component import (
        ApiV1BlocksArchiveCreateIconUrlErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_is_behind_stable_error_component import (
        ApiV1BlocksArchiveCreateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_kind_error_component import ApiV1BlocksArchiveCreateKindErrorComponent
    from ..models.api_v1_blocks_archive_create_labels_error_component import (
        ApiV1BlocksArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_latest_stable_error_component import (
        ApiV1BlocksArchiveCreateLatestStableErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_license_error_component import (
        ApiV1BlocksArchiveCreateLicenseErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_license_url_error_component import (
        ApiV1BlocksArchiveCreateLicenseUrlErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_name_error_component import ApiV1BlocksArchiveCreateNameErrorComponent
    from ..models.api_v1_blocks_archive_create_non_field_errors_error_component import (
        ApiV1BlocksArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_platform_service_error_component import (
        ApiV1BlocksArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_provider_error_component import (
        ApiV1BlocksArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_provider_id_error_component import (
        ApiV1BlocksArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_provider_reference_error_component import (
        ApiV1BlocksArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_readme_md_raw_error_component import (
        ApiV1BlocksArchiveCreateReadmeMdRawErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_reconciliation_enabled_error_component import (
        ApiV1BlocksArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_registry_url_error_component import (
        ApiV1BlocksArchiveCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_releases_url_error_component import (
        ApiV1BlocksArchiveCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_scope_error_component import ApiV1BlocksArchiveCreateScopeErrorComponent
    from ..models.api_v1_blocks_archive_create_sla_availability_error_component import (
        ApiV1BlocksArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_sla_target_error_component import (
        ApiV1BlocksArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_slo_availability_error_component import (
        ApiV1BlocksArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_slo_target_error_component import (
        ApiV1BlocksArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_supports_ha_error_component import (
        ApiV1BlocksArchiveCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_target_availability_error_component import (
        ApiV1BlocksArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_template_block_error_component import (
        ApiV1BlocksArchiveCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_template_error_component import (
        ApiV1BlocksArchiveCreateTemplateErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_type_error_component import ApiV1BlocksArchiveCreateTypeErrorComponent
    from ..models.api_v1_blocks_archive_create_user_spec_error_component import (
        ApiV1BlocksArchiveCreateUserSpecErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_version_error_component import (
        ApiV1BlocksArchiveCreateVersionErrorComponent,
    )
    from ..models.api_v1_blocks_archive_create_website_url_error_component import (
        ApiV1BlocksArchiveCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlocksArchiveCreateValidationError")


@_attrs_define
class ApiV1BlocksArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksArchiveCreateActionsErrorComponent |
            ApiV1BlocksArchiveCreateActualAvailabilityErrorComponent | ApiV1BlocksArchiveCreateAnnotationsErrorComponent |
            ApiV1BlocksArchiveCreateAppVersionErrorComponent | ApiV1BlocksArchiveCreateArchivedAtErrorComponent |
            ApiV1BlocksArchiveCreateArchivedErrorComponent | ApiV1BlocksArchiveCreateArchivedReasonErrorComponent |
            ApiV1BlocksArchiveCreateAutoRolloutErrorComponent | ApiV1BlocksArchiveCreateBlockPolyRawErrorComponent |
            ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponent | ApiV1BlocksArchiveCreateChecksumErrorComponent |
            ApiV1BlocksArchiveCreateConfigErrorComponent | ApiV1BlocksArchiveCreateCreatedByBrcErrorComponent |
            ApiV1BlocksArchiveCreateCreatedByComponentErrorComponent | ApiV1BlocksArchiveCreateCriticalityErrorComponent |
            ApiV1BlocksArchiveCreateDebugModeErrorComponent | ApiV1BlocksArchiveCreateDescriptionErrorComponent |
            ApiV1BlocksArchiveCreateDiscoveryEnabledErrorComponent | ApiV1BlocksArchiveCreateDisplayNameErrorComponent |
            ApiV1BlocksArchiveCreateDocumentationUrlErrorComponent | ApiV1BlocksArchiveCreateExamplesPolyRawErrorComponent |
            ApiV1BlocksArchiveCreateFlavorErrorComponent | ApiV1BlocksArchiveCreateFromBlockErrorComponent |
            ApiV1BlocksArchiveCreateFullSpecErrorComponent | ApiV1BlocksArchiveCreateGitRepositoryUrlErrorComponent |
            ApiV1BlocksArchiveCreateIconUrlErrorComponent | ApiV1BlocksArchiveCreateIsBehindStableErrorComponent |
            ApiV1BlocksArchiveCreateKindErrorComponent | ApiV1BlocksArchiveCreateLabelsErrorComponent |
            ApiV1BlocksArchiveCreateLatestStableErrorComponent | ApiV1BlocksArchiveCreateLicenseErrorComponent |
            ApiV1BlocksArchiveCreateLicenseUrlErrorComponent | ApiV1BlocksArchiveCreateNameErrorComponent |
            ApiV1BlocksArchiveCreateNonFieldErrorsErrorComponent | ApiV1BlocksArchiveCreatePlatformServiceErrorComponent |
            ApiV1BlocksArchiveCreateProviderErrorComponent | ApiV1BlocksArchiveCreateProviderIdErrorComponent |
            ApiV1BlocksArchiveCreateProviderReferenceErrorComponent | ApiV1BlocksArchiveCreateReadmeMdRawErrorComponent |
            ApiV1BlocksArchiveCreateReconciliationEnabledErrorComponent | ApiV1BlocksArchiveCreateRegistryUrlErrorComponent
            | ApiV1BlocksArchiveCreateReleasesUrlErrorComponent | ApiV1BlocksArchiveCreateScopeErrorComponent |
            ApiV1BlocksArchiveCreateSlaAvailabilityErrorComponent | ApiV1BlocksArchiveCreateSlaTargetErrorComponent |
            ApiV1BlocksArchiveCreateSloAvailabilityErrorComponent | ApiV1BlocksArchiveCreateSloTargetErrorComponent |
            ApiV1BlocksArchiveCreateSupportsHaErrorComponent | ApiV1BlocksArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1BlocksArchiveCreateTemplateBlockErrorComponent | ApiV1BlocksArchiveCreateTemplateErrorComponent |
            ApiV1BlocksArchiveCreateTypeErrorComponent | ApiV1BlocksArchiveCreateUserSpecErrorComponent |
            ApiV1BlocksArchiveCreateVersionErrorComponent | ApiV1BlocksArchiveCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksArchiveCreateActionsErrorComponent
        | ApiV1BlocksArchiveCreateActualAvailabilityErrorComponent
        | ApiV1BlocksArchiveCreateAnnotationsErrorComponent
        | ApiV1BlocksArchiveCreateAppVersionErrorComponent
        | ApiV1BlocksArchiveCreateArchivedAtErrorComponent
        | ApiV1BlocksArchiveCreateArchivedErrorComponent
        | ApiV1BlocksArchiveCreateArchivedReasonErrorComponent
        | ApiV1BlocksArchiveCreateAutoRolloutErrorComponent
        | ApiV1BlocksArchiveCreateBlockPolyRawErrorComponent
        | ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponent
        | ApiV1BlocksArchiveCreateChecksumErrorComponent
        | ApiV1BlocksArchiveCreateConfigErrorComponent
        | ApiV1BlocksArchiveCreateCreatedByBrcErrorComponent
        | ApiV1BlocksArchiveCreateCreatedByComponentErrorComponent
        | ApiV1BlocksArchiveCreateCriticalityErrorComponent
        | ApiV1BlocksArchiveCreateDebugModeErrorComponent
        | ApiV1BlocksArchiveCreateDescriptionErrorComponent
        | ApiV1BlocksArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1BlocksArchiveCreateDisplayNameErrorComponent
        | ApiV1BlocksArchiveCreateDocumentationUrlErrorComponent
        | ApiV1BlocksArchiveCreateExamplesPolyRawErrorComponent
        | ApiV1BlocksArchiveCreateFlavorErrorComponent
        | ApiV1BlocksArchiveCreateFromBlockErrorComponent
        | ApiV1BlocksArchiveCreateFullSpecErrorComponent
        | ApiV1BlocksArchiveCreateGitRepositoryUrlErrorComponent
        | ApiV1BlocksArchiveCreateIconUrlErrorComponent
        | ApiV1BlocksArchiveCreateIsBehindStableErrorComponent
        | ApiV1BlocksArchiveCreateKindErrorComponent
        | ApiV1BlocksArchiveCreateLabelsErrorComponent
        | ApiV1BlocksArchiveCreateLatestStableErrorComponent
        | ApiV1BlocksArchiveCreateLicenseErrorComponent
        | ApiV1BlocksArchiveCreateLicenseUrlErrorComponent
        | ApiV1BlocksArchiveCreateNameErrorComponent
        | ApiV1BlocksArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1BlocksArchiveCreatePlatformServiceErrorComponent
        | ApiV1BlocksArchiveCreateProviderErrorComponent
        | ApiV1BlocksArchiveCreateProviderIdErrorComponent
        | ApiV1BlocksArchiveCreateProviderReferenceErrorComponent
        | ApiV1BlocksArchiveCreateReadmeMdRawErrorComponent
        | ApiV1BlocksArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1BlocksArchiveCreateRegistryUrlErrorComponent
        | ApiV1BlocksArchiveCreateReleasesUrlErrorComponent
        | ApiV1BlocksArchiveCreateScopeErrorComponent
        | ApiV1BlocksArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1BlocksArchiveCreateSlaTargetErrorComponent
        | ApiV1BlocksArchiveCreateSloAvailabilityErrorComponent
        | ApiV1BlocksArchiveCreateSloTargetErrorComponent
        | ApiV1BlocksArchiveCreateSupportsHaErrorComponent
        | ApiV1BlocksArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1BlocksArchiveCreateTemplateBlockErrorComponent
        | ApiV1BlocksArchiveCreateTemplateErrorComponent
        | ApiV1BlocksArchiveCreateTypeErrorComponent
        | ApiV1BlocksArchiveCreateUserSpecErrorComponent
        | ApiV1BlocksArchiveCreateVersionErrorComponent
        | ApiV1BlocksArchiveCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_archive_create_actions_error_component import (
            ApiV1BlocksArchiveCreateActionsErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_actual_availability_error_component import (
            ApiV1BlocksArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_annotations_error_component import (
            ApiV1BlocksArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_app_version_error_component import (
            ApiV1BlocksArchiveCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_archived_at_error_component import (
            ApiV1BlocksArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_archived_error_component import (
            ApiV1BlocksArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_archived_reason_error_component import (
            ApiV1BlocksArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_auto_rollout_error_component import (
            ApiV1BlocksArchiveCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_block_poly_raw_error_component import (
            ApiV1BlocksArchiveCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_changelog_poly_raw_error_component import (
            ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_checksum_error_component import (
            ApiV1BlocksArchiveCreateChecksumErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_config_error_component import (
            ApiV1BlocksArchiveCreateConfigErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_created_by_brc_error_component import (
            ApiV1BlocksArchiveCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_criticality_error_component import (
            ApiV1BlocksArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_debug_mode_error_component import (
            ApiV1BlocksArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_description_error_component import (
            ApiV1BlocksArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_discovery_enabled_error_component import (
            ApiV1BlocksArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_display_name_error_component import (
            ApiV1BlocksArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_documentation_url_error_component import (
            ApiV1BlocksArchiveCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_examples_poly_raw_error_component import (
            ApiV1BlocksArchiveCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_flavor_error_component import (
            ApiV1BlocksArchiveCreateFlavorErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_from_block_error_component import (
            ApiV1BlocksArchiveCreateFromBlockErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_full_spec_error_component import (
            ApiV1BlocksArchiveCreateFullSpecErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_git_repository_url_error_component import (
            ApiV1BlocksArchiveCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_icon_url_error_component import (
            ApiV1BlocksArchiveCreateIconUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_is_behind_stable_error_component import (
            ApiV1BlocksArchiveCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_kind_error_component import (
            ApiV1BlocksArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_labels_error_component import (
            ApiV1BlocksArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_latest_stable_error_component import (
            ApiV1BlocksArchiveCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_license_error_component import (
            ApiV1BlocksArchiveCreateLicenseErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_license_url_error_component import (
            ApiV1BlocksArchiveCreateLicenseUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_name_error_component import (
            ApiV1BlocksArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_non_field_errors_error_component import (
            ApiV1BlocksArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_platform_service_error_component import (
            ApiV1BlocksArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_provider_error_component import (
            ApiV1BlocksArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_provider_id_error_component import (
            ApiV1BlocksArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_provider_reference_error_component import (
            ApiV1BlocksArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_readme_md_raw_error_component import (
            ApiV1BlocksArchiveCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_reconciliation_enabled_error_component import (
            ApiV1BlocksArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_registry_url_error_component import (
            ApiV1BlocksArchiveCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_releases_url_error_component import (
            ApiV1BlocksArchiveCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_scope_error_component import (
            ApiV1BlocksArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_sla_availability_error_component import (
            ApiV1BlocksArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_sla_target_error_component import (
            ApiV1BlocksArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_slo_availability_error_component import (
            ApiV1BlocksArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_slo_target_error_component import (
            ApiV1BlocksArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_supports_ha_error_component import (
            ApiV1BlocksArchiveCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_target_availability_error_component import (
            ApiV1BlocksArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_template_block_error_component import (
            ApiV1BlocksArchiveCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_template_error_component import (
            ApiV1BlocksArchiveCreateTemplateErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_type_error_component import (
            ApiV1BlocksArchiveCreateTypeErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_user_spec_error_component import (
            ApiV1BlocksArchiveCreateUserSpecErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_version_error_component import (
            ApiV1BlocksArchiveCreateVersionErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_website_url_error_component import (
            ApiV1BlocksArchiveCreateWebsiteUrlErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksArchiveCreateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_archive_create_actions_error_component import (
            ApiV1BlocksArchiveCreateActionsErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_actual_availability_error_component import (
            ApiV1BlocksArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_annotations_error_component import (
            ApiV1BlocksArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_app_version_error_component import (
            ApiV1BlocksArchiveCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_archived_at_error_component import (
            ApiV1BlocksArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_archived_error_component import (
            ApiV1BlocksArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_archived_reason_error_component import (
            ApiV1BlocksArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_auto_rollout_error_component import (
            ApiV1BlocksArchiveCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_block_poly_raw_error_component import (
            ApiV1BlocksArchiveCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_changelog_poly_raw_error_component import (
            ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_checksum_error_component import (
            ApiV1BlocksArchiveCreateChecksumErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_config_error_component import (
            ApiV1BlocksArchiveCreateConfigErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_created_by_brc_error_component import (
            ApiV1BlocksArchiveCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_created_by_component_error_component import (
            ApiV1BlocksArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_criticality_error_component import (
            ApiV1BlocksArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_debug_mode_error_component import (
            ApiV1BlocksArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_description_error_component import (
            ApiV1BlocksArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_discovery_enabled_error_component import (
            ApiV1BlocksArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_display_name_error_component import (
            ApiV1BlocksArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_documentation_url_error_component import (
            ApiV1BlocksArchiveCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_examples_poly_raw_error_component import (
            ApiV1BlocksArchiveCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_flavor_error_component import (
            ApiV1BlocksArchiveCreateFlavorErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_from_block_error_component import (
            ApiV1BlocksArchiveCreateFromBlockErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_full_spec_error_component import (
            ApiV1BlocksArchiveCreateFullSpecErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_git_repository_url_error_component import (
            ApiV1BlocksArchiveCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_icon_url_error_component import (
            ApiV1BlocksArchiveCreateIconUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_is_behind_stable_error_component import (
            ApiV1BlocksArchiveCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_kind_error_component import (
            ApiV1BlocksArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_labels_error_component import (
            ApiV1BlocksArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_latest_stable_error_component import (
            ApiV1BlocksArchiveCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_license_error_component import (
            ApiV1BlocksArchiveCreateLicenseErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_license_url_error_component import (
            ApiV1BlocksArchiveCreateLicenseUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_name_error_component import (
            ApiV1BlocksArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_non_field_errors_error_component import (
            ApiV1BlocksArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_platform_service_error_component import (
            ApiV1BlocksArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_provider_error_component import (
            ApiV1BlocksArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_provider_id_error_component import (
            ApiV1BlocksArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_provider_reference_error_component import (
            ApiV1BlocksArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_readme_md_raw_error_component import (
            ApiV1BlocksArchiveCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_reconciliation_enabled_error_component import (
            ApiV1BlocksArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_registry_url_error_component import (
            ApiV1BlocksArchiveCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_releases_url_error_component import (
            ApiV1BlocksArchiveCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_scope_error_component import (
            ApiV1BlocksArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_sla_availability_error_component import (
            ApiV1BlocksArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_sla_target_error_component import (
            ApiV1BlocksArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_slo_availability_error_component import (
            ApiV1BlocksArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_slo_target_error_component import (
            ApiV1BlocksArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_supports_ha_error_component import (
            ApiV1BlocksArchiveCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_target_availability_error_component import (
            ApiV1BlocksArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_template_block_error_component import (
            ApiV1BlocksArchiveCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_template_error_component import (
            ApiV1BlocksArchiveCreateTemplateErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_type_error_component import (
            ApiV1BlocksArchiveCreateTypeErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_user_spec_error_component import (
            ApiV1BlocksArchiveCreateUserSpecErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_version_error_component import (
            ApiV1BlocksArchiveCreateVersionErrorComponent,
        )
        from ..models.api_v1_blocks_archive_create_website_url_error_component import (
            ApiV1BlocksArchiveCreateWebsiteUrlErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksArchiveCreateActionsErrorComponent
                | ApiV1BlocksArchiveCreateActualAvailabilityErrorComponent
                | ApiV1BlocksArchiveCreateAnnotationsErrorComponent
                | ApiV1BlocksArchiveCreateAppVersionErrorComponent
                | ApiV1BlocksArchiveCreateArchivedAtErrorComponent
                | ApiV1BlocksArchiveCreateArchivedErrorComponent
                | ApiV1BlocksArchiveCreateArchivedReasonErrorComponent
                | ApiV1BlocksArchiveCreateAutoRolloutErrorComponent
                | ApiV1BlocksArchiveCreateBlockPolyRawErrorComponent
                | ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponent
                | ApiV1BlocksArchiveCreateChecksumErrorComponent
                | ApiV1BlocksArchiveCreateConfigErrorComponent
                | ApiV1BlocksArchiveCreateCreatedByBrcErrorComponent
                | ApiV1BlocksArchiveCreateCreatedByComponentErrorComponent
                | ApiV1BlocksArchiveCreateCriticalityErrorComponent
                | ApiV1BlocksArchiveCreateDebugModeErrorComponent
                | ApiV1BlocksArchiveCreateDescriptionErrorComponent
                | ApiV1BlocksArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1BlocksArchiveCreateDisplayNameErrorComponent
                | ApiV1BlocksArchiveCreateDocumentationUrlErrorComponent
                | ApiV1BlocksArchiveCreateExamplesPolyRawErrorComponent
                | ApiV1BlocksArchiveCreateFlavorErrorComponent
                | ApiV1BlocksArchiveCreateFromBlockErrorComponent
                | ApiV1BlocksArchiveCreateFullSpecErrorComponent
                | ApiV1BlocksArchiveCreateGitRepositoryUrlErrorComponent
                | ApiV1BlocksArchiveCreateIconUrlErrorComponent
                | ApiV1BlocksArchiveCreateIsBehindStableErrorComponent
                | ApiV1BlocksArchiveCreateKindErrorComponent
                | ApiV1BlocksArchiveCreateLabelsErrorComponent
                | ApiV1BlocksArchiveCreateLatestStableErrorComponent
                | ApiV1BlocksArchiveCreateLicenseErrorComponent
                | ApiV1BlocksArchiveCreateLicenseUrlErrorComponent
                | ApiV1BlocksArchiveCreateNameErrorComponent
                | ApiV1BlocksArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1BlocksArchiveCreatePlatformServiceErrorComponent
                | ApiV1BlocksArchiveCreateProviderErrorComponent
                | ApiV1BlocksArchiveCreateProviderIdErrorComponent
                | ApiV1BlocksArchiveCreateProviderReferenceErrorComponent
                | ApiV1BlocksArchiveCreateReadmeMdRawErrorComponent
                | ApiV1BlocksArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1BlocksArchiveCreateRegistryUrlErrorComponent
                | ApiV1BlocksArchiveCreateReleasesUrlErrorComponent
                | ApiV1BlocksArchiveCreateScopeErrorComponent
                | ApiV1BlocksArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1BlocksArchiveCreateSlaTargetErrorComponent
                | ApiV1BlocksArchiveCreateSloAvailabilityErrorComponent
                | ApiV1BlocksArchiveCreateSloTargetErrorComponent
                | ApiV1BlocksArchiveCreateSupportsHaErrorComponent
                | ApiV1BlocksArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1BlocksArchiveCreateTemplateBlockErrorComponent
                | ApiV1BlocksArchiveCreateTemplateErrorComponent
                | ApiV1BlocksArchiveCreateTypeErrorComponent
                | ApiV1BlocksArchiveCreateUserSpecErrorComponent
                | ApiV1BlocksArchiveCreateVersionErrorComponent
                | ApiV1BlocksArchiveCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_0 = (
                        ApiV1BlocksArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_1 = (
                        ApiV1BlocksArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_2 = (
                        ApiV1BlocksArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_3 = (
                        ApiV1BlocksArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_4 = (
                        ApiV1BlocksArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_5 = (
                        ApiV1BlocksArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_6 = (
                        ApiV1BlocksArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_7 = (
                        ApiV1BlocksArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_8 = (
                        ApiV1BlocksArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_9 = (
                        ApiV1BlocksArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_10 = (
                        ApiV1BlocksArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_11 = (
                        ApiV1BlocksArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_12 = (
                        ApiV1BlocksArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_13 = (
                        ApiV1BlocksArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_14 = (
                        ApiV1BlocksArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_15 = (
                        ApiV1BlocksArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_16 = (
                        ApiV1BlocksArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_17 = (
                        ApiV1BlocksArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_18 = (
                        ApiV1BlocksArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_19 = (
                        ApiV1BlocksArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_20 = (
                        ApiV1BlocksArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_21 = (
                        ApiV1BlocksArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_22 = (
                        ApiV1BlocksArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_23 = (
                        ApiV1BlocksArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_24 = (
                        ApiV1BlocksArchiveCreateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_25 = (
                        ApiV1BlocksArchiveCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_26 = (
                        ApiV1BlocksArchiveCreateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_27 = (
                        ApiV1BlocksArchiveCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_28 = (
                        ApiV1BlocksArchiveCreateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_29 = (
                        ApiV1BlocksArchiveCreateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_30 = (
                        ApiV1BlocksArchiveCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_31 = (
                        ApiV1BlocksArchiveCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_32 = (
                        ApiV1BlocksArchiveCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_33 = (
                        ApiV1BlocksArchiveCreateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_34 = (
                        ApiV1BlocksArchiveCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_35 = (
                        ApiV1BlocksArchiveCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_36 = (
                        ApiV1BlocksArchiveCreateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_37 = (
                        ApiV1BlocksArchiveCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_38 = (
                        ApiV1BlocksArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_39 = (
                        ApiV1BlocksArchiveCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_40 = (
                        ApiV1BlocksArchiveCreateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_41 = (
                        ApiV1BlocksArchiveCreateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_42 = (
                        ApiV1BlocksArchiveCreateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_43 = (
                        ApiV1BlocksArchiveCreateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_44 = (
                        ApiV1BlocksArchiveCreateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_45 = (
                        ApiV1BlocksArchiveCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_46 = (
                        ApiV1BlocksArchiveCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_47 = (
                        ApiV1BlocksArchiveCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_48 = (
                        ApiV1BlocksArchiveCreateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_49 = (
                        ApiV1BlocksArchiveCreateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_50 = (
                        ApiV1BlocksArchiveCreateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_51 = (
                        ApiV1BlocksArchiveCreateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_52 = (
                        ApiV1BlocksArchiveCreateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_archive_create_error_type_53 = (
                        ApiV1BlocksArchiveCreateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_archive_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_archive_create_error_type_54 = (
                    ApiV1BlocksArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_archive_create_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_archive_create_validation_error.additional_properties = d
        return api_v1_blocks_archive_create_validation_error

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
