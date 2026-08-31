from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_discover_create_actions_error_component import (
        ApiV1BlocksDiscoverCreateActionsErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_actual_availability_error_component import (
        ApiV1BlocksDiscoverCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_annotations_error_component import (
        ApiV1BlocksDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_app_version_error_component import (
        ApiV1BlocksDiscoverCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_archived_at_error_component import (
        ApiV1BlocksDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_archived_error_component import (
        ApiV1BlocksDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_archived_reason_error_component import (
        ApiV1BlocksDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_auto_rollout_error_component import (
        ApiV1BlocksDiscoverCreateAutoRolloutErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_block_poly_raw_error_component import (
        ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_changelog_poly_raw_error_component import (
        ApiV1BlocksDiscoverCreateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_checksum_error_component import (
        ApiV1BlocksDiscoverCreateChecksumErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_config_error_component import (
        ApiV1BlocksDiscoverCreateConfigErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_created_by_brc_error_component import (
        ApiV1BlocksDiscoverCreateCreatedByBrcErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_created_by_component_error_component import (
        ApiV1BlocksDiscoverCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_criticality_error_component import (
        ApiV1BlocksDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_debug_mode_error_component import (
        ApiV1BlocksDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_description_error_component import (
        ApiV1BlocksDiscoverCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_discovery_enabled_error_component import (
        ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_display_name_error_component import (
        ApiV1BlocksDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_documentation_url_error_component import (
        ApiV1BlocksDiscoverCreateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_examples_poly_raw_error_component import (
        ApiV1BlocksDiscoverCreateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_flavor_error_component import (
        ApiV1BlocksDiscoverCreateFlavorErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_from_block_error_component import (
        ApiV1BlocksDiscoverCreateFromBlockErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_full_spec_error_component import (
        ApiV1BlocksDiscoverCreateFullSpecErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_git_repository_url_error_component import (
        ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_icon_url_error_component import (
        ApiV1BlocksDiscoverCreateIconUrlErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_is_behind_stable_error_component import (
        ApiV1BlocksDiscoverCreateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_kind_error_component import ApiV1BlocksDiscoverCreateKindErrorComponent
    from ..models.api_v1_blocks_discover_create_labels_error_component import (
        ApiV1BlocksDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_latest_stable_error_component import (
        ApiV1BlocksDiscoverCreateLatestStableErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_license_error_component import (
        ApiV1BlocksDiscoverCreateLicenseErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_license_url_error_component import (
        ApiV1BlocksDiscoverCreateLicenseUrlErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_name_error_component import ApiV1BlocksDiscoverCreateNameErrorComponent
    from ..models.api_v1_blocks_discover_create_non_field_errors_error_component import (
        ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_platform_service_error_component import (
        ApiV1BlocksDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_provider_error_component import (
        ApiV1BlocksDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_provider_id_error_component import (
        ApiV1BlocksDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_provider_reference_error_component import (
        ApiV1BlocksDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_readme_md_raw_error_component import (
        ApiV1BlocksDiscoverCreateReadmeMdRawErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_reconciliation_enabled_error_component import (
        ApiV1BlocksDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_registry_url_error_component import (
        ApiV1BlocksDiscoverCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_releases_url_error_component import (
        ApiV1BlocksDiscoverCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_scope_error_component import (
        ApiV1BlocksDiscoverCreateScopeErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_sla_availability_error_component import (
        ApiV1BlocksDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_sla_target_error_component import (
        ApiV1BlocksDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_slo_availability_error_component import (
        ApiV1BlocksDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_slo_target_error_component import (
        ApiV1BlocksDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_supports_ha_error_component import (
        ApiV1BlocksDiscoverCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_target_availability_error_component import (
        ApiV1BlocksDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_template_block_error_component import (
        ApiV1BlocksDiscoverCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_template_error_component import (
        ApiV1BlocksDiscoverCreateTemplateErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_type_error_component import ApiV1BlocksDiscoverCreateTypeErrorComponent
    from ..models.api_v1_blocks_discover_create_user_spec_error_component import (
        ApiV1BlocksDiscoverCreateUserSpecErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_version_error_component import (
        ApiV1BlocksDiscoverCreateVersionErrorComponent,
    )
    from ..models.api_v1_blocks_discover_create_website_url_error_component import (
        ApiV1BlocksDiscoverCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlocksDiscoverCreateValidationError")


@_attrs_define
class ApiV1BlocksDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksDiscoverCreateActionsErrorComponent |
            ApiV1BlocksDiscoverCreateActualAvailabilityErrorComponent | ApiV1BlocksDiscoverCreateAnnotationsErrorComponent |
            ApiV1BlocksDiscoverCreateAppVersionErrorComponent | ApiV1BlocksDiscoverCreateArchivedAtErrorComponent |
            ApiV1BlocksDiscoverCreateArchivedErrorComponent | ApiV1BlocksDiscoverCreateArchivedReasonErrorComponent |
            ApiV1BlocksDiscoverCreateAutoRolloutErrorComponent | ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponent |
            ApiV1BlocksDiscoverCreateChangelogPolyRawErrorComponent | ApiV1BlocksDiscoverCreateChecksumErrorComponent |
            ApiV1BlocksDiscoverCreateConfigErrorComponent | ApiV1BlocksDiscoverCreateCreatedByBrcErrorComponent |
            ApiV1BlocksDiscoverCreateCreatedByComponentErrorComponent | ApiV1BlocksDiscoverCreateCriticalityErrorComponent |
            ApiV1BlocksDiscoverCreateDebugModeErrorComponent | ApiV1BlocksDiscoverCreateDescriptionErrorComponent |
            ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponent | ApiV1BlocksDiscoverCreateDisplayNameErrorComponent |
            ApiV1BlocksDiscoverCreateDocumentationUrlErrorComponent | ApiV1BlocksDiscoverCreateExamplesPolyRawErrorComponent
            | ApiV1BlocksDiscoverCreateFlavorErrorComponent | ApiV1BlocksDiscoverCreateFromBlockErrorComponent |
            ApiV1BlocksDiscoverCreateFullSpecErrorComponent | ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponent |
            ApiV1BlocksDiscoverCreateIconUrlErrorComponent | ApiV1BlocksDiscoverCreateIsBehindStableErrorComponent |
            ApiV1BlocksDiscoverCreateKindErrorComponent | ApiV1BlocksDiscoverCreateLabelsErrorComponent |
            ApiV1BlocksDiscoverCreateLatestStableErrorComponent | ApiV1BlocksDiscoverCreateLicenseErrorComponent |
            ApiV1BlocksDiscoverCreateLicenseUrlErrorComponent | ApiV1BlocksDiscoverCreateNameErrorComponent |
            ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponent | ApiV1BlocksDiscoverCreatePlatformServiceErrorComponent |
            ApiV1BlocksDiscoverCreateProviderErrorComponent | ApiV1BlocksDiscoverCreateProviderIdErrorComponent |
            ApiV1BlocksDiscoverCreateProviderReferenceErrorComponent | ApiV1BlocksDiscoverCreateReadmeMdRawErrorComponent |
            ApiV1BlocksDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1BlocksDiscoverCreateRegistryUrlErrorComponent | ApiV1BlocksDiscoverCreateReleasesUrlErrorComponent |
            ApiV1BlocksDiscoverCreateScopeErrorComponent | ApiV1BlocksDiscoverCreateSlaAvailabilityErrorComponent |
            ApiV1BlocksDiscoverCreateSlaTargetErrorComponent | ApiV1BlocksDiscoverCreateSloAvailabilityErrorComponent |
            ApiV1BlocksDiscoverCreateSloTargetErrorComponent | ApiV1BlocksDiscoverCreateSupportsHaErrorComponent |
            ApiV1BlocksDiscoverCreateTargetAvailabilityErrorComponent | ApiV1BlocksDiscoverCreateTemplateBlockErrorComponent
            | ApiV1BlocksDiscoverCreateTemplateErrorComponent | ApiV1BlocksDiscoverCreateTypeErrorComponent |
            ApiV1BlocksDiscoverCreateUserSpecErrorComponent | ApiV1BlocksDiscoverCreateVersionErrorComponent |
            ApiV1BlocksDiscoverCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksDiscoverCreateActionsErrorComponent
        | ApiV1BlocksDiscoverCreateActualAvailabilityErrorComponent
        | ApiV1BlocksDiscoverCreateAnnotationsErrorComponent
        | ApiV1BlocksDiscoverCreateAppVersionErrorComponent
        | ApiV1BlocksDiscoverCreateArchivedAtErrorComponent
        | ApiV1BlocksDiscoverCreateArchivedErrorComponent
        | ApiV1BlocksDiscoverCreateArchivedReasonErrorComponent
        | ApiV1BlocksDiscoverCreateAutoRolloutErrorComponent
        | ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponent
        | ApiV1BlocksDiscoverCreateChangelogPolyRawErrorComponent
        | ApiV1BlocksDiscoverCreateChecksumErrorComponent
        | ApiV1BlocksDiscoverCreateConfigErrorComponent
        | ApiV1BlocksDiscoverCreateCreatedByBrcErrorComponent
        | ApiV1BlocksDiscoverCreateCreatedByComponentErrorComponent
        | ApiV1BlocksDiscoverCreateCriticalityErrorComponent
        | ApiV1BlocksDiscoverCreateDebugModeErrorComponent
        | ApiV1BlocksDiscoverCreateDescriptionErrorComponent
        | ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponent
        | ApiV1BlocksDiscoverCreateDisplayNameErrorComponent
        | ApiV1BlocksDiscoverCreateDocumentationUrlErrorComponent
        | ApiV1BlocksDiscoverCreateExamplesPolyRawErrorComponent
        | ApiV1BlocksDiscoverCreateFlavorErrorComponent
        | ApiV1BlocksDiscoverCreateFromBlockErrorComponent
        | ApiV1BlocksDiscoverCreateFullSpecErrorComponent
        | ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponent
        | ApiV1BlocksDiscoverCreateIconUrlErrorComponent
        | ApiV1BlocksDiscoverCreateIsBehindStableErrorComponent
        | ApiV1BlocksDiscoverCreateKindErrorComponent
        | ApiV1BlocksDiscoverCreateLabelsErrorComponent
        | ApiV1BlocksDiscoverCreateLatestStableErrorComponent
        | ApiV1BlocksDiscoverCreateLicenseErrorComponent
        | ApiV1BlocksDiscoverCreateLicenseUrlErrorComponent
        | ApiV1BlocksDiscoverCreateNameErrorComponent
        | ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1BlocksDiscoverCreatePlatformServiceErrorComponent
        | ApiV1BlocksDiscoverCreateProviderErrorComponent
        | ApiV1BlocksDiscoverCreateProviderIdErrorComponent
        | ApiV1BlocksDiscoverCreateProviderReferenceErrorComponent
        | ApiV1BlocksDiscoverCreateReadmeMdRawErrorComponent
        | ApiV1BlocksDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1BlocksDiscoverCreateRegistryUrlErrorComponent
        | ApiV1BlocksDiscoverCreateReleasesUrlErrorComponent
        | ApiV1BlocksDiscoverCreateScopeErrorComponent
        | ApiV1BlocksDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1BlocksDiscoverCreateSlaTargetErrorComponent
        | ApiV1BlocksDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1BlocksDiscoverCreateSloTargetErrorComponent
        | ApiV1BlocksDiscoverCreateSupportsHaErrorComponent
        | ApiV1BlocksDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1BlocksDiscoverCreateTemplateBlockErrorComponent
        | ApiV1BlocksDiscoverCreateTemplateErrorComponent
        | ApiV1BlocksDiscoverCreateTypeErrorComponent
        | ApiV1BlocksDiscoverCreateUserSpecErrorComponent
        | ApiV1BlocksDiscoverCreateVersionErrorComponent
        | ApiV1BlocksDiscoverCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_discover_create_actions_error_component import (
            ApiV1BlocksDiscoverCreateActionsErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_actual_availability_error_component import (
            ApiV1BlocksDiscoverCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_annotations_error_component import (
            ApiV1BlocksDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_app_version_error_component import (
            ApiV1BlocksDiscoverCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_archived_at_error_component import (
            ApiV1BlocksDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_archived_error_component import (
            ApiV1BlocksDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_archived_reason_error_component import (
            ApiV1BlocksDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_auto_rollout_error_component import (
            ApiV1BlocksDiscoverCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_block_poly_raw_error_component import (
            ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_changelog_poly_raw_error_component import (
            ApiV1BlocksDiscoverCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_checksum_error_component import (
            ApiV1BlocksDiscoverCreateChecksumErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_config_error_component import (
            ApiV1BlocksDiscoverCreateConfigErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_created_by_brc_error_component import (
            ApiV1BlocksDiscoverCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_criticality_error_component import (
            ApiV1BlocksDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_debug_mode_error_component import (
            ApiV1BlocksDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_description_error_component import (
            ApiV1BlocksDiscoverCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_discovery_enabled_error_component import (
            ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_display_name_error_component import (
            ApiV1BlocksDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_documentation_url_error_component import (
            ApiV1BlocksDiscoverCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_examples_poly_raw_error_component import (
            ApiV1BlocksDiscoverCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_flavor_error_component import (
            ApiV1BlocksDiscoverCreateFlavorErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_from_block_error_component import (
            ApiV1BlocksDiscoverCreateFromBlockErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_full_spec_error_component import (
            ApiV1BlocksDiscoverCreateFullSpecErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_git_repository_url_error_component import (
            ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_icon_url_error_component import (
            ApiV1BlocksDiscoverCreateIconUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_is_behind_stable_error_component import (
            ApiV1BlocksDiscoverCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_kind_error_component import (
            ApiV1BlocksDiscoverCreateKindErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_labels_error_component import (
            ApiV1BlocksDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_latest_stable_error_component import (
            ApiV1BlocksDiscoverCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_license_error_component import (
            ApiV1BlocksDiscoverCreateLicenseErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_license_url_error_component import (
            ApiV1BlocksDiscoverCreateLicenseUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_name_error_component import (
            ApiV1BlocksDiscoverCreateNameErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_non_field_errors_error_component import (
            ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_platform_service_error_component import (
            ApiV1BlocksDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_provider_error_component import (
            ApiV1BlocksDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_provider_id_error_component import (
            ApiV1BlocksDiscoverCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_provider_reference_error_component import (
            ApiV1BlocksDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_readme_md_raw_error_component import (
            ApiV1BlocksDiscoverCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_reconciliation_enabled_error_component import (
            ApiV1BlocksDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_registry_url_error_component import (
            ApiV1BlocksDiscoverCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_releases_url_error_component import (
            ApiV1BlocksDiscoverCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_scope_error_component import (
            ApiV1BlocksDiscoverCreateScopeErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_sla_availability_error_component import (
            ApiV1BlocksDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_sla_target_error_component import (
            ApiV1BlocksDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_slo_availability_error_component import (
            ApiV1BlocksDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_slo_target_error_component import (
            ApiV1BlocksDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_supports_ha_error_component import (
            ApiV1BlocksDiscoverCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_target_availability_error_component import (
            ApiV1BlocksDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_template_block_error_component import (
            ApiV1BlocksDiscoverCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_template_error_component import (
            ApiV1BlocksDiscoverCreateTemplateErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_type_error_component import (
            ApiV1BlocksDiscoverCreateTypeErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_user_spec_error_component import (
            ApiV1BlocksDiscoverCreateUserSpecErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_version_error_component import (
            ApiV1BlocksDiscoverCreateVersionErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_website_url_error_component import (
            ApiV1BlocksDiscoverCreateWebsiteUrlErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksDiscoverCreateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_discover_create_actions_error_component import (
            ApiV1BlocksDiscoverCreateActionsErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_actual_availability_error_component import (
            ApiV1BlocksDiscoverCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_annotations_error_component import (
            ApiV1BlocksDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_app_version_error_component import (
            ApiV1BlocksDiscoverCreateAppVersionErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_archived_at_error_component import (
            ApiV1BlocksDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_archived_error_component import (
            ApiV1BlocksDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_archived_reason_error_component import (
            ApiV1BlocksDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_auto_rollout_error_component import (
            ApiV1BlocksDiscoverCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_block_poly_raw_error_component import (
            ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_changelog_poly_raw_error_component import (
            ApiV1BlocksDiscoverCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_checksum_error_component import (
            ApiV1BlocksDiscoverCreateChecksumErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_config_error_component import (
            ApiV1BlocksDiscoverCreateConfigErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_created_by_brc_error_component import (
            ApiV1BlocksDiscoverCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_created_by_component_error_component import (
            ApiV1BlocksDiscoverCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_criticality_error_component import (
            ApiV1BlocksDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_debug_mode_error_component import (
            ApiV1BlocksDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_description_error_component import (
            ApiV1BlocksDiscoverCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_discovery_enabled_error_component import (
            ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_display_name_error_component import (
            ApiV1BlocksDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_documentation_url_error_component import (
            ApiV1BlocksDiscoverCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_examples_poly_raw_error_component import (
            ApiV1BlocksDiscoverCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_flavor_error_component import (
            ApiV1BlocksDiscoverCreateFlavorErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_from_block_error_component import (
            ApiV1BlocksDiscoverCreateFromBlockErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_full_spec_error_component import (
            ApiV1BlocksDiscoverCreateFullSpecErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_git_repository_url_error_component import (
            ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_icon_url_error_component import (
            ApiV1BlocksDiscoverCreateIconUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_is_behind_stable_error_component import (
            ApiV1BlocksDiscoverCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_kind_error_component import (
            ApiV1BlocksDiscoverCreateKindErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_labels_error_component import (
            ApiV1BlocksDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_latest_stable_error_component import (
            ApiV1BlocksDiscoverCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_license_error_component import (
            ApiV1BlocksDiscoverCreateLicenseErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_license_url_error_component import (
            ApiV1BlocksDiscoverCreateLicenseUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_name_error_component import (
            ApiV1BlocksDiscoverCreateNameErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_non_field_errors_error_component import (
            ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_platform_service_error_component import (
            ApiV1BlocksDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_provider_error_component import (
            ApiV1BlocksDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_provider_id_error_component import (
            ApiV1BlocksDiscoverCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_provider_reference_error_component import (
            ApiV1BlocksDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_readme_md_raw_error_component import (
            ApiV1BlocksDiscoverCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_reconciliation_enabled_error_component import (
            ApiV1BlocksDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_registry_url_error_component import (
            ApiV1BlocksDiscoverCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_releases_url_error_component import (
            ApiV1BlocksDiscoverCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_scope_error_component import (
            ApiV1BlocksDiscoverCreateScopeErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_sla_availability_error_component import (
            ApiV1BlocksDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_sla_target_error_component import (
            ApiV1BlocksDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_slo_availability_error_component import (
            ApiV1BlocksDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_slo_target_error_component import (
            ApiV1BlocksDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_supports_ha_error_component import (
            ApiV1BlocksDiscoverCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_target_availability_error_component import (
            ApiV1BlocksDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_template_block_error_component import (
            ApiV1BlocksDiscoverCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_template_error_component import (
            ApiV1BlocksDiscoverCreateTemplateErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_type_error_component import (
            ApiV1BlocksDiscoverCreateTypeErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_user_spec_error_component import (
            ApiV1BlocksDiscoverCreateUserSpecErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_version_error_component import (
            ApiV1BlocksDiscoverCreateVersionErrorComponent,
        )
        from ..models.api_v1_blocks_discover_create_website_url_error_component import (
            ApiV1BlocksDiscoverCreateWebsiteUrlErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksDiscoverCreateActionsErrorComponent
                | ApiV1BlocksDiscoverCreateActualAvailabilityErrorComponent
                | ApiV1BlocksDiscoverCreateAnnotationsErrorComponent
                | ApiV1BlocksDiscoverCreateAppVersionErrorComponent
                | ApiV1BlocksDiscoverCreateArchivedAtErrorComponent
                | ApiV1BlocksDiscoverCreateArchivedErrorComponent
                | ApiV1BlocksDiscoverCreateArchivedReasonErrorComponent
                | ApiV1BlocksDiscoverCreateAutoRolloutErrorComponent
                | ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponent
                | ApiV1BlocksDiscoverCreateChangelogPolyRawErrorComponent
                | ApiV1BlocksDiscoverCreateChecksumErrorComponent
                | ApiV1BlocksDiscoverCreateConfigErrorComponent
                | ApiV1BlocksDiscoverCreateCreatedByBrcErrorComponent
                | ApiV1BlocksDiscoverCreateCreatedByComponentErrorComponent
                | ApiV1BlocksDiscoverCreateCriticalityErrorComponent
                | ApiV1BlocksDiscoverCreateDebugModeErrorComponent
                | ApiV1BlocksDiscoverCreateDescriptionErrorComponent
                | ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponent
                | ApiV1BlocksDiscoverCreateDisplayNameErrorComponent
                | ApiV1BlocksDiscoverCreateDocumentationUrlErrorComponent
                | ApiV1BlocksDiscoverCreateExamplesPolyRawErrorComponent
                | ApiV1BlocksDiscoverCreateFlavorErrorComponent
                | ApiV1BlocksDiscoverCreateFromBlockErrorComponent
                | ApiV1BlocksDiscoverCreateFullSpecErrorComponent
                | ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponent
                | ApiV1BlocksDiscoverCreateIconUrlErrorComponent
                | ApiV1BlocksDiscoverCreateIsBehindStableErrorComponent
                | ApiV1BlocksDiscoverCreateKindErrorComponent
                | ApiV1BlocksDiscoverCreateLabelsErrorComponent
                | ApiV1BlocksDiscoverCreateLatestStableErrorComponent
                | ApiV1BlocksDiscoverCreateLicenseErrorComponent
                | ApiV1BlocksDiscoverCreateLicenseUrlErrorComponent
                | ApiV1BlocksDiscoverCreateNameErrorComponent
                | ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1BlocksDiscoverCreatePlatformServiceErrorComponent
                | ApiV1BlocksDiscoverCreateProviderErrorComponent
                | ApiV1BlocksDiscoverCreateProviderIdErrorComponent
                | ApiV1BlocksDiscoverCreateProviderReferenceErrorComponent
                | ApiV1BlocksDiscoverCreateReadmeMdRawErrorComponent
                | ApiV1BlocksDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1BlocksDiscoverCreateRegistryUrlErrorComponent
                | ApiV1BlocksDiscoverCreateReleasesUrlErrorComponent
                | ApiV1BlocksDiscoverCreateScopeErrorComponent
                | ApiV1BlocksDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1BlocksDiscoverCreateSlaTargetErrorComponent
                | ApiV1BlocksDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1BlocksDiscoverCreateSloTargetErrorComponent
                | ApiV1BlocksDiscoverCreateSupportsHaErrorComponent
                | ApiV1BlocksDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1BlocksDiscoverCreateTemplateBlockErrorComponent
                | ApiV1BlocksDiscoverCreateTemplateErrorComponent
                | ApiV1BlocksDiscoverCreateTypeErrorComponent
                | ApiV1BlocksDiscoverCreateUserSpecErrorComponent
                | ApiV1BlocksDiscoverCreateVersionErrorComponent
                | ApiV1BlocksDiscoverCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_0 = (
                        ApiV1BlocksDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_1 = (
                        ApiV1BlocksDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_2 = (
                        ApiV1BlocksDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_3 = (
                        ApiV1BlocksDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_4 = (
                        ApiV1BlocksDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_5 = (
                        ApiV1BlocksDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_6 = (
                        ApiV1BlocksDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_7 = (
                        ApiV1BlocksDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_8 = (
                        ApiV1BlocksDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_9 = (
                        ApiV1BlocksDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_10 = (
                        ApiV1BlocksDiscoverCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_11 = (
                        ApiV1BlocksDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_12 = (
                        ApiV1BlocksDiscoverCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_13 = (
                        ApiV1BlocksDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_14 = (
                        ApiV1BlocksDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_15 = (
                        ApiV1BlocksDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_16 = (
                        ApiV1BlocksDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_17 = (
                        ApiV1BlocksDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_18 = (
                        ApiV1BlocksDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_19 = (
                        ApiV1BlocksDiscoverCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_20 = (
                        ApiV1BlocksDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_21 = (
                        ApiV1BlocksDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_22 = (
                        ApiV1BlocksDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_23 = (
                        ApiV1BlocksDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_24 = (
                        ApiV1BlocksDiscoverCreateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_25 = (
                        ApiV1BlocksDiscoverCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_26 = (
                        ApiV1BlocksDiscoverCreateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_27 = (
                        ApiV1BlocksDiscoverCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_28 = (
                        ApiV1BlocksDiscoverCreateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_29 = (
                        ApiV1BlocksDiscoverCreateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_30 = (
                        ApiV1BlocksDiscoverCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_31 = (
                        ApiV1BlocksDiscoverCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_32 = (
                        ApiV1BlocksDiscoverCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_33 = (
                        ApiV1BlocksDiscoverCreateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_34 = (
                        ApiV1BlocksDiscoverCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_35 = (
                        ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_36 = (
                        ApiV1BlocksDiscoverCreateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_37 = (
                        ApiV1BlocksDiscoverCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_38 = (
                        ApiV1BlocksDiscoverCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_39 = (
                        ApiV1BlocksDiscoverCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_40 = (
                        ApiV1BlocksDiscoverCreateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_41 = (
                        ApiV1BlocksDiscoverCreateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_42 = (
                        ApiV1BlocksDiscoverCreateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_43 = (
                        ApiV1BlocksDiscoverCreateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_44 = (
                        ApiV1BlocksDiscoverCreateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_45 = (
                        ApiV1BlocksDiscoverCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_46 = (
                        ApiV1BlocksDiscoverCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_47 = (
                        ApiV1BlocksDiscoverCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_48 = (
                        ApiV1BlocksDiscoverCreateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_49 = (
                        ApiV1BlocksDiscoverCreateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_50 = (
                        ApiV1BlocksDiscoverCreateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_51 = (
                        ApiV1BlocksDiscoverCreateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_52 = (
                        ApiV1BlocksDiscoverCreateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_discover_create_error_type_53 = (
                        ApiV1BlocksDiscoverCreateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_discover_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_discover_create_error_type_54 = (
                    ApiV1BlocksDiscoverCreateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_discover_create_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_discover_create_validation_error.additional_properties = d
        return api_v1_blocks_discover_create_validation_error

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
