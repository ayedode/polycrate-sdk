from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_run_discovery_create_actions_error_component import (
        ApiV1BlocksRunDiscoveryCreateActionsErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_actual_availability_error_component import (
        ApiV1BlocksRunDiscoveryCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_annotations_error_component import (
        ApiV1BlocksRunDiscoveryCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_app_version_error_component import (
        ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_archived_at_error_component import (
        ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_archived_error_component import (
        ApiV1BlocksRunDiscoveryCreateArchivedErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_archived_reason_error_component import (
        ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_auto_rollout_error_component import (
        ApiV1BlocksRunDiscoveryCreateAutoRolloutErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_block_poly_raw_error_component import (
        ApiV1BlocksRunDiscoveryCreateBlockPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_changelog_poly_raw_error_component import (
        ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_checksum_error_component import (
        ApiV1BlocksRunDiscoveryCreateChecksumErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_config_error_component import (
        ApiV1BlocksRunDiscoveryCreateConfigErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_created_by_brc_error_component import (
        ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_created_by_component_error_component import (
        ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_criticality_error_component import (
        ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_debug_mode_error_component import (
        ApiV1BlocksRunDiscoveryCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_description_error_component import (
        ApiV1BlocksRunDiscoveryCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_discovery_enabled_error_component import (
        ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_display_name_error_component import (
        ApiV1BlocksRunDiscoveryCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_documentation_url_error_component import (
        ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_examples_poly_raw_error_component import (
        ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_flavor_error_component import (
        ApiV1BlocksRunDiscoveryCreateFlavorErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_from_block_error_component import (
        ApiV1BlocksRunDiscoveryCreateFromBlockErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_full_spec_error_component import (
        ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_git_repository_url_error_component import (
        ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_icon_url_error_component import (
        ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_is_behind_stable_error_component import (
        ApiV1BlocksRunDiscoveryCreateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_kind_error_component import (
        ApiV1BlocksRunDiscoveryCreateKindErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_labels_error_component import (
        ApiV1BlocksRunDiscoveryCreateLabelsErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_latest_stable_error_component import (
        ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_license_error_component import (
        ApiV1BlocksRunDiscoveryCreateLicenseErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_license_url_error_component import (
        ApiV1BlocksRunDiscoveryCreateLicenseUrlErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_name_error_component import (
        ApiV1BlocksRunDiscoveryCreateNameErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_non_field_errors_error_component import (
        ApiV1BlocksRunDiscoveryCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_platform_service_error_component import (
        ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_provider_error_component import (
        ApiV1BlocksRunDiscoveryCreateProviderErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_provider_id_error_component import (
        ApiV1BlocksRunDiscoveryCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_provider_reference_error_component import (
        ApiV1BlocksRunDiscoveryCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_readme_md_raw_error_component import (
        ApiV1BlocksRunDiscoveryCreateReadmeMdRawErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_reconciliation_enabled_error_component import (
        ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_registry_url_error_component import (
        ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_releases_url_error_component import (
        ApiV1BlocksRunDiscoveryCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_scope_error_component import (
        ApiV1BlocksRunDiscoveryCreateScopeErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_sla_availability_error_component import (
        ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_sla_target_error_component import (
        ApiV1BlocksRunDiscoveryCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_slo_availability_error_component import (
        ApiV1BlocksRunDiscoveryCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_slo_target_error_component import (
        ApiV1BlocksRunDiscoveryCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_supports_ha_error_component import (
        ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_target_availability_error_component import (
        ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_template_block_error_component import (
        ApiV1BlocksRunDiscoveryCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_template_error_component import (
        ApiV1BlocksRunDiscoveryCreateTemplateErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_type_error_component import (
        ApiV1BlocksRunDiscoveryCreateTypeErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_user_spec_error_component import (
        ApiV1BlocksRunDiscoveryCreateUserSpecErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_version_error_component import (
        ApiV1BlocksRunDiscoveryCreateVersionErrorComponent,
    )
    from ..models.api_v1_blocks_run_discovery_create_website_url_error_component import (
        ApiV1BlocksRunDiscoveryCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlocksRunDiscoveryCreateValidationError")


@_attrs_define
class ApiV1BlocksRunDiscoveryCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksRunDiscoveryCreateActionsErrorComponent |
            ApiV1BlocksRunDiscoveryCreateActualAvailabilityErrorComponent |
            ApiV1BlocksRunDiscoveryCreateAnnotationsErrorComponent | ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponent |
            ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponent | ApiV1BlocksRunDiscoveryCreateArchivedErrorComponent |
            ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponent |
            ApiV1BlocksRunDiscoveryCreateAutoRolloutErrorComponent | ApiV1BlocksRunDiscoveryCreateBlockPolyRawErrorComponent
            | ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponent |
            ApiV1BlocksRunDiscoveryCreateChecksumErrorComponent | ApiV1BlocksRunDiscoveryCreateConfigErrorComponent |
            ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponent |
            ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponent |
            ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponent | ApiV1BlocksRunDiscoveryCreateDebugModeErrorComponent |
            ApiV1BlocksRunDiscoveryCreateDescriptionErrorComponent |
            ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponent |
            ApiV1BlocksRunDiscoveryCreateDisplayNameErrorComponent |
            ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponent |
            ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponent | ApiV1BlocksRunDiscoveryCreateFlavorErrorComponent |
            ApiV1BlocksRunDiscoveryCreateFromBlockErrorComponent | ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponent |
            ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponent | ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponent
            | ApiV1BlocksRunDiscoveryCreateIsBehindStableErrorComponent | ApiV1BlocksRunDiscoveryCreateKindErrorComponent |
            ApiV1BlocksRunDiscoveryCreateLabelsErrorComponent | ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponent |
            ApiV1BlocksRunDiscoveryCreateLicenseErrorComponent | ApiV1BlocksRunDiscoveryCreateLicenseUrlErrorComponent |
            ApiV1BlocksRunDiscoveryCreateNameErrorComponent | ApiV1BlocksRunDiscoveryCreateNonFieldErrorsErrorComponent |
            ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponent | ApiV1BlocksRunDiscoveryCreateProviderErrorComponent
            | ApiV1BlocksRunDiscoveryCreateProviderIdErrorComponent |
            ApiV1BlocksRunDiscoveryCreateProviderReferenceErrorComponent |
            ApiV1BlocksRunDiscoveryCreateReadmeMdRawErrorComponent |
            ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponent |
            ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponent | ApiV1BlocksRunDiscoveryCreateReleasesUrlErrorComponent
            | ApiV1BlocksRunDiscoveryCreateScopeErrorComponent | ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponent
            | ApiV1BlocksRunDiscoveryCreateSlaTargetErrorComponent |
            ApiV1BlocksRunDiscoveryCreateSloAvailabilityErrorComponent |
            ApiV1BlocksRunDiscoveryCreateSloTargetErrorComponent | ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponent |
            ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponent |
            ApiV1BlocksRunDiscoveryCreateTemplateBlockErrorComponent | ApiV1BlocksRunDiscoveryCreateTemplateErrorComponent |
            ApiV1BlocksRunDiscoveryCreateTypeErrorComponent | ApiV1BlocksRunDiscoveryCreateUserSpecErrorComponent |
            ApiV1BlocksRunDiscoveryCreateVersionErrorComponent | ApiV1BlocksRunDiscoveryCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksRunDiscoveryCreateActionsErrorComponent
        | ApiV1BlocksRunDiscoveryCreateActualAvailabilityErrorComponent
        | ApiV1BlocksRunDiscoveryCreateAnnotationsErrorComponent
        | ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponent
        | ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponent
        | ApiV1BlocksRunDiscoveryCreateArchivedErrorComponent
        | ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponent
        | ApiV1BlocksRunDiscoveryCreateAutoRolloutErrorComponent
        | ApiV1BlocksRunDiscoveryCreateBlockPolyRawErrorComponent
        | ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponent
        | ApiV1BlocksRunDiscoveryCreateChecksumErrorComponent
        | ApiV1BlocksRunDiscoveryCreateConfigErrorComponent
        | ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponent
        | ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponent
        | ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponent
        | ApiV1BlocksRunDiscoveryCreateDebugModeErrorComponent
        | ApiV1BlocksRunDiscoveryCreateDescriptionErrorComponent
        | ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponent
        | ApiV1BlocksRunDiscoveryCreateDisplayNameErrorComponent
        | ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponent
        | ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponent
        | ApiV1BlocksRunDiscoveryCreateFlavorErrorComponent
        | ApiV1BlocksRunDiscoveryCreateFromBlockErrorComponent
        | ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponent
        | ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponent
        | ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponent
        | ApiV1BlocksRunDiscoveryCreateIsBehindStableErrorComponent
        | ApiV1BlocksRunDiscoveryCreateKindErrorComponent
        | ApiV1BlocksRunDiscoveryCreateLabelsErrorComponent
        | ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponent
        | ApiV1BlocksRunDiscoveryCreateLicenseErrorComponent
        | ApiV1BlocksRunDiscoveryCreateLicenseUrlErrorComponent
        | ApiV1BlocksRunDiscoveryCreateNameErrorComponent
        | ApiV1BlocksRunDiscoveryCreateNonFieldErrorsErrorComponent
        | ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponent
        | ApiV1BlocksRunDiscoveryCreateProviderErrorComponent
        | ApiV1BlocksRunDiscoveryCreateProviderIdErrorComponent
        | ApiV1BlocksRunDiscoveryCreateProviderReferenceErrorComponent
        | ApiV1BlocksRunDiscoveryCreateReadmeMdRawErrorComponent
        | ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponent
        | ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponent
        | ApiV1BlocksRunDiscoveryCreateReleasesUrlErrorComponent
        | ApiV1BlocksRunDiscoveryCreateScopeErrorComponent
        | ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponent
        | ApiV1BlocksRunDiscoveryCreateSlaTargetErrorComponent
        | ApiV1BlocksRunDiscoveryCreateSloAvailabilityErrorComponent
        | ApiV1BlocksRunDiscoveryCreateSloTargetErrorComponent
        | ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponent
        | ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponent
        | ApiV1BlocksRunDiscoveryCreateTemplateBlockErrorComponent
        | ApiV1BlocksRunDiscoveryCreateTemplateErrorComponent
        | ApiV1BlocksRunDiscoveryCreateTypeErrorComponent
        | ApiV1BlocksRunDiscoveryCreateUserSpecErrorComponent
        | ApiV1BlocksRunDiscoveryCreateVersionErrorComponent
        | ApiV1BlocksRunDiscoveryCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_run_discovery_create_actions_error_component import (
            ApiV1BlocksRunDiscoveryCreateActionsErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_actual_availability_error_component import (
            ApiV1BlocksRunDiscoveryCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_annotations_error_component import (
            ApiV1BlocksRunDiscoveryCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_app_version_error_component import (
            ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_archived_at_error_component import (
            ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_archived_error_component import (
            ApiV1BlocksRunDiscoveryCreateArchivedErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_archived_reason_error_component import (
            ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_auto_rollout_error_component import (
            ApiV1BlocksRunDiscoveryCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_block_poly_raw_error_component import (
            ApiV1BlocksRunDiscoveryCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_changelog_poly_raw_error_component import (
            ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_checksum_error_component import (
            ApiV1BlocksRunDiscoveryCreateChecksumErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_config_error_component import (
            ApiV1BlocksRunDiscoveryCreateConfigErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_created_by_brc_error_component import (
            ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_criticality_error_component import (
            ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_debug_mode_error_component import (
            ApiV1BlocksRunDiscoveryCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_description_error_component import (
            ApiV1BlocksRunDiscoveryCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_discovery_enabled_error_component import (
            ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_display_name_error_component import (
            ApiV1BlocksRunDiscoveryCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_documentation_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_examples_poly_raw_error_component import (
            ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_flavor_error_component import (
            ApiV1BlocksRunDiscoveryCreateFlavorErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_from_block_error_component import (
            ApiV1BlocksRunDiscoveryCreateFromBlockErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_full_spec_error_component import (
            ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_git_repository_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_icon_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_is_behind_stable_error_component import (
            ApiV1BlocksRunDiscoveryCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_kind_error_component import (
            ApiV1BlocksRunDiscoveryCreateKindErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_labels_error_component import (
            ApiV1BlocksRunDiscoveryCreateLabelsErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_latest_stable_error_component import (
            ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_license_error_component import (
            ApiV1BlocksRunDiscoveryCreateLicenseErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_license_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateLicenseUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_name_error_component import (
            ApiV1BlocksRunDiscoveryCreateNameErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_non_field_errors_error_component import (
            ApiV1BlocksRunDiscoveryCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_platform_service_error_component import (
            ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_provider_error_component import (
            ApiV1BlocksRunDiscoveryCreateProviderErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_provider_id_error_component import (
            ApiV1BlocksRunDiscoveryCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_provider_reference_error_component import (
            ApiV1BlocksRunDiscoveryCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_readme_md_raw_error_component import (
            ApiV1BlocksRunDiscoveryCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_reconciliation_enabled_error_component import (
            ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_registry_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_releases_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_scope_error_component import (
            ApiV1BlocksRunDiscoveryCreateScopeErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_sla_availability_error_component import (
            ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_sla_target_error_component import (
            ApiV1BlocksRunDiscoveryCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_slo_availability_error_component import (
            ApiV1BlocksRunDiscoveryCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_slo_target_error_component import (
            ApiV1BlocksRunDiscoveryCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_supports_ha_error_component import (
            ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_target_availability_error_component import (
            ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_template_block_error_component import (
            ApiV1BlocksRunDiscoveryCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_template_error_component import (
            ApiV1BlocksRunDiscoveryCreateTemplateErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_type_error_component import (
            ApiV1BlocksRunDiscoveryCreateTypeErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_user_spec_error_component import (
            ApiV1BlocksRunDiscoveryCreateUserSpecErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_version_error_component import (
            ApiV1BlocksRunDiscoveryCreateVersionErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_website_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateWebsiteUrlErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_run_discovery_create_actions_error_component import (
            ApiV1BlocksRunDiscoveryCreateActionsErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_actual_availability_error_component import (
            ApiV1BlocksRunDiscoveryCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_annotations_error_component import (
            ApiV1BlocksRunDiscoveryCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_app_version_error_component import (
            ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_archived_at_error_component import (
            ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_archived_error_component import (
            ApiV1BlocksRunDiscoveryCreateArchivedErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_archived_reason_error_component import (
            ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_auto_rollout_error_component import (
            ApiV1BlocksRunDiscoveryCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_block_poly_raw_error_component import (
            ApiV1BlocksRunDiscoveryCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_changelog_poly_raw_error_component import (
            ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_checksum_error_component import (
            ApiV1BlocksRunDiscoveryCreateChecksumErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_config_error_component import (
            ApiV1BlocksRunDiscoveryCreateConfigErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_created_by_brc_error_component import (
            ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_created_by_component_error_component import (
            ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_criticality_error_component import (
            ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_debug_mode_error_component import (
            ApiV1BlocksRunDiscoveryCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_description_error_component import (
            ApiV1BlocksRunDiscoveryCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_discovery_enabled_error_component import (
            ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_display_name_error_component import (
            ApiV1BlocksRunDiscoveryCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_documentation_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_examples_poly_raw_error_component import (
            ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_flavor_error_component import (
            ApiV1BlocksRunDiscoveryCreateFlavorErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_from_block_error_component import (
            ApiV1BlocksRunDiscoveryCreateFromBlockErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_full_spec_error_component import (
            ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_git_repository_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_icon_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_is_behind_stable_error_component import (
            ApiV1BlocksRunDiscoveryCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_kind_error_component import (
            ApiV1BlocksRunDiscoveryCreateKindErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_labels_error_component import (
            ApiV1BlocksRunDiscoveryCreateLabelsErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_latest_stable_error_component import (
            ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_license_error_component import (
            ApiV1BlocksRunDiscoveryCreateLicenseErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_license_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateLicenseUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_name_error_component import (
            ApiV1BlocksRunDiscoveryCreateNameErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_non_field_errors_error_component import (
            ApiV1BlocksRunDiscoveryCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_platform_service_error_component import (
            ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_provider_error_component import (
            ApiV1BlocksRunDiscoveryCreateProviderErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_provider_id_error_component import (
            ApiV1BlocksRunDiscoveryCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_provider_reference_error_component import (
            ApiV1BlocksRunDiscoveryCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_readme_md_raw_error_component import (
            ApiV1BlocksRunDiscoveryCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_reconciliation_enabled_error_component import (
            ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_registry_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_releases_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_scope_error_component import (
            ApiV1BlocksRunDiscoveryCreateScopeErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_sla_availability_error_component import (
            ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_sla_target_error_component import (
            ApiV1BlocksRunDiscoveryCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_slo_availability_error_component import (
            ApiV1BlocksRunDiscoveryCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_slo_target_error_component import (
            ApiV1BlocksRunDiscoveryCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_supports_ha_error_component import (
            ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_target_availability_error_component import (
            ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_template_block_error_component import (
            ApiV1BlocksRunDiscoveryCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_template_error_component import (
            ApiV1BlocksRunDiscoveryCreateTemplateErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_type_error_component import (
            ApiV1BlocksRunDiscoveryCreateTypeErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_user_spec_error_component import (
            ApiV1BlocksRunDiscoveryCreateUserSpecErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_version_error_component import (
            ApiV1BlocksRunDiscoveryCreateVersionErrorComponent,
        )
        from ..models.api_v1_blocks_run_discovery_create_website_url_error_component import (
            ApiV1BlocksRunDiscoveryCreateWebsiteUrlErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksRunDiscoveryCreateActionsErrorComponent
                | ApiV1BlocksRunDiscoveryCreateActualAvailabilityErrorComponent
                | ApiV1BlocksRunDiscoveryCreateAnnotationsErrorComponent
                | ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponent
                | ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponent
                | ApiV1BlocksRunDiscoveryCreateArchivedErrorComponent
                | ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponent
                | ApiV1BlocksRunDiscoveryCreateAutoRolloutErrorComponent
                | ApiV1BlocksRunDiscoveryCreateBlockPolyRawErrorComponent
                | ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponent
                | ApiV1BlocksRunDiscoveryCreateChecksumErrorComponent
                | ApiV1BlocksRunDiscoveryCreateConfigErrorComponent
                | ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponent
                | ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponent
                | ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponent
                | ApiV1BlocksRunDiscoveryCreateDebugModeErrorComponent
                | ApiV1BlocksRunDiscoveryCreateDescriptionErrorComponent
                | ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponent
                | ApiV1BlocksRunDiscoveryCreateDisplayNameErrorComponent
                | ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponent
                | ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponent
                | ApiV1BlocksRunDiscoveryCreateFlavorErrorComponent
                | ApiV1BlocksRunDiscoveryCreateFromBlockErrorComponent
                | ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponent
                | ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponent
                | ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponent
                | ApiV1BlocksRunDiscoveryCreateIsBehindStableErrorComponent
                | ApiV1BlocksRunDiscoveryCreateKindErrorComponent
                | ApiV1BlocksRunDiscoveryCreateLabelsErrorComponent
                | ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponent
                | ApiV1BlocksRunDiscoveryCreateLicenseErrorComponent
                | ApiV1BlocksRunDiscoveryCreateLicenseUrlErrorComponent
                | ApiV1BlocksRunDiscoveryCreateNameErrorComponent
                | ApiV1BlocksRunDiscoveryCreateNonFieldErrorsErrorComponent
                | ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponent
                | ApiV1BlocksRunDiscoveryCreateProviderErrorComponent
                | ApiV1BlocksRunDiscoveryCreateProviderIdErrorComponent
                | ApiV1BlocksRunDiscoveryCreateProviderReferenceErrorComponent
                | ApiV1BlocksRunDiscoveryCreateReadmeMdRawErrorComponent
                | ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponent
                | ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponent
                | ApiV1BlocksRunDiscoveryCreateReleasesUrlErrorComponent
                | ApiV1BlocksRunDiscoveryCreateScopeErrorComponent
                | ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponent
                | ApiV1BlocksRunDiscoveryCreateSlaTargetErrorComponent
                | ApiV1BlocksRunDiscoveryCreateSloAvailabilityErrorComponent
                | ApiV1BlocksRunDiscoveryCreateSloTargetErrorComponent
                | ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponent
                | ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponent
                | ApiV1BlocksRunDiscoveryCreateTemplateBlockErrorComponent
                | ApiV1BlocksRunDiscoveryCreateTemplateErrorComponent
                | ApiV1BlocksRunDiscoveryCreateTypeErrorComponent
                | ApiV1BlocksRunDiscoveryCreateUserSpecErrorComponent
                | ApiV1BlocksRunDiscoveryCreateVersionErrorComponent
                | ApiV1BlocksRunDiscoveryCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_0 = (
                        ApiV1BlocksRunDiscoveryCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_1 = (
                        ApiV1BlocksRunDiscoveryCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_2 = (
                        ApiV1BlocksRunDiscoveryCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_3 = (
                        ApiV1BlocksRunDiscoveryCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_4 = (
                        ApiV1BlocksRunDiscoveryCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_5 = (
                        ApiV1BlocksRunDiscoveryCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_6 = (
                        ApiV1BlocksRunDiscoveryCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_7 = (
                        ApiV1BlocksRunDiscoveryCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_8 = (
                        ApiV1BlocksRunDiscoveryCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_9 = (
                        ApiV1BlocksRunDiscoveryCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_10 = (
                        ApiV1BlocksRunDiscoveryCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_11 = (
                        ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_12 = (
                        ApiV1BlocksRunDiscoveryCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_13 = (
                        ApiV1BlocksRunDiscoveryCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_14 = (
                        ApiV1BlocksRunDiscoveryCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_15 = (
                        ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_16 = (
                        ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_17 = (
                        ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_18 = (
                        ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_19 = (
                        ApiV1BlocksRunDiscoveryCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_20 = (
                        ApiV1BlocksRunDiscoveryCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_21 = (
                        ApiV1BlocksRunDiscoveryCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_22 = (
                        ApiV1BlocksRunDiscoveryCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_23 = (
                        ApiV1BlocksRunDiscoveryCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_24 = (
                        ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_25 = (
                        ApiV1BlocksRunDiscoveryCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_26 = (
                        ApiV1BlocksRunDiscoveryCreateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_27 = (
                        ApiV1BlocksRunDiscoveryCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_28 = (
                        ApiV1BlocksRunDiscoveryCreateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_29 = (
                        ApiV1BlocksRunDiscoveryCreateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_30 = (
                        ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_31 = (
                        ApiV1BlocksRunDiscoveryCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_32 = (
                        ApiV1BlocksRunDiscoveryCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_33 = (
                        ApiV1BlocksRunDiscoveryCreateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_34 = (
                        ApiV1BlocksRunDiscoveryCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_35 = (
                        ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_36 = (
                        ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_37 = (
                        ApiV1BlocksRunDiscoveryCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_38 = (
                        ApiV1BlocksRunDiscoveryCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_39 = (
                        ApiV1BlocksRunDiscoveryCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_40 = (
                        ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_41 = (
                        ApiV1BlocksRunDiscoveryCreateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_42 = (
                        ApiV1BlocksRunDiscoveryCreateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_43 = (
                        ApiV1BlocksRunDiscoveryCreateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_44 = (
                        ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_45 = (
                        ApiV1BlocksRunDiscoveryCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_46 = (
                        ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_47 = (
                        ApiV1BlocksRunDiscoveryCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_48 = (
                        ApiV1BlocksRunDiscoveryCreateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_49 = (
                        ApiV1BlocksRunDiscoveryCreateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_50 = (
                        ApiV1BlocksRunDiscoveryCreateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_51 = (
                        ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_52 = (
                        ApiV1BlocksRunDiscoveryCreateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_run_discovery_create_error_type_53 = (
                        ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_run_discovery_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_run_discovery_create_error_type_54 = (
                    ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_run_discovery_create_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_run_discovery_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_run_discovery_create_validation_error.additional_properties = d
        return api_v1_blocks_run_discovery_create_validation_error

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
