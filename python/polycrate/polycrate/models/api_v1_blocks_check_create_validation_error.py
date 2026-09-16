from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_check_create_actions_error_component import ApiV1BlocksCheckCreateActionsErrorComponent
    from ..models.api_v1_blocks_check_create_actual_availability_error_component import (
        ApiV1BlocksCheckCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_annotations_error_component import (
        ApiV1BlocksCheckCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_app_version_error_component import (
        ApiV1BlocksCheckCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_archived_at_error_component import (
        ApiV1BlocksCheckCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_archived_error_component import (
        ApiV1BlocksCheckCreateArchivedErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_archived_reason_error_component import (
        ApiV1BlocksCheckCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_auto_rollout_error_component import (
        ApiV1BlocksCheckCreateAutoRolloutErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_block_poly_raw_error_component import (
        ApiV1BlocksCheckCreateBlockPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_changelog_poly_raw_error_component import (
        ApiV1BlocksCheckCreateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_checksum_error_component import (
        ApiV1BlocksCheckCreateChecksumErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_config_error_component import ApiV1BlocksCheckCreateConfigErrorComponent
    from ..models.api_v1_blocks_check_create_created_by_brc_error_component import (
        ApiV1BlocksCheckCreateCreatedByBrcErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_created_by_component_error_component import (
        ApiV1BlocksCheckCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_criticality_error_component import (
        ApiV1BlocksCheckCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_debug_mode_error_component import (
        ApiV1BlocksCheckCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_description_error_component import (
        ApiV1BlocksCheckCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_discovery_enabled_error_component import (
        ApiV1BlocksCheckCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_display_name_error_component import (
        ApiV1BlocksCheckCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_documentation_url_error_component import (
        ApiV1BlocksCheckCreateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_examples_poly_raw_error_component import (
        ApiV1BlocksCheckCreateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_flavor_error_component import ApiV1BlocksCheckCreateFlavorErrorComponent
    from ..models.api_v1_blocks_check_create_from_block_error_component import (
        ApiV1BlocksCheckCreateFromBlockErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_full_spec_error_component import (
        ApiV1BlocksCheckCreateFullSpecErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_git_repository_url_error_component import (
        ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_icon_url_error_component import ApiV1BlocksCheckCreateIconUrlErrorComponent
    from ..models.api_v1_blocks_check_create_is_behind_stable_error_component import (
        ApiV1BlocksCheckCreateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_kind_error_component import ApiV1BlocksCheckCreateKindErrorComponent
    from ..models.api_v1_blocks_check_create_labels_error_component import ApiV1BlocksCheckCreateLabelsErrorComponent
    from ..models.api_v1_blocks_check_create_latest_stable_error_component import (
        ApiV1BlocksCheckCreateLatestStableErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_license_error_component import ApiV1BlocksCheckCreateLicenseErrorComponent
    from ..models.api_v1_blocks_check_create_license_url_error_component import (
        ApiV1BlocksCheckCreateLicenseUrlErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_name_error_component import ApiV1BlocksCheckCreateNameErrorComponent
    from ..models.api_v1_blocks_check_create_non_field_errors_error_component import (
        ApiV1BlocksCheckCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_platform_service_error_component import (
        ApiV1BlocksCheckCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_provider_error_component import (
        ApiV1BlocksCheckCreateProviderErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_provider_id_error_component import (
        ApiV1BlocksCheckCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_provider_reference_error_component import (
        ApiV1BlocksCheckCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_readme_md_raw_error_component import (
        ApiV1BlocksCheckCreateReadmeMdRawErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_reconciliation_enabled_error_component import (
        ApiV1BlocksCheckCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_registry_url_error_component import (
        ApiV1BlocksCheckCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_releases_url_error_component import (
        ApiV1BlocksCheckCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_scope_error_component import ApiV1BlocksCheckCreateScopeErrorComponent
    from ..models.api_v1_blocks_check_create_sla_availability_error_component import (
        ApiV1BlocksCheckCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_sla_target_error_component import (
        ApiV1BlocksCheckCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_slo_availability_error_component import (
        ApiV1BlocksCheckCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_slo_target_error_component import (
        ApiV1BlocksCheckCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_supports_ha_error_component import (
        ApiV1BlocksCheckCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_target_availability_error_component import (
        ApiV1BlocksCheckCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_template_block_error_component import (
        ApiV1BlocksCheckCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_template_error_component import (
        ApiV1BlocksCheckCreateTemplateErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_type_error_component import ApiV1BlocksCheckCreateTypeErrorComponent
    from ..models.api_v1_blocks_check_create_user_spec_error_component import (
        ApiV1BlocksCheckCreateUserSpecErrorComponent,
    )
    from ..models.api_v1_blocks_check_create_version_error_component import ApiV1BlocksCheckCreateVersionErrorComponent
    from ..models.api_v1_blocks_check_create_website_url_error_component import (
        ApiV1BlocksCheckCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlocksCheckCreateValidationError")


@_attrs_define
class ApiV1BlocksCheckCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksCheckCreateActionsErrorComponent |
            ApiV1BlocksCheckCreateActualAvailabilityErrorComponent | ApiV1BlocksCheckCreateAnnotationsErrorComponent |
            ApiV1BlocksCheckCreateAppVersionErrorComponent | ApiV1BlocksCheckCreateArchivedAtErrorComponent |
            ApiV1BlocksCheckCreateArchivedErrorComponent | ApiV1BlocksCheckCreateArchivedReasonErrorComponent |
            ApiV1BlocksCheckCreateAutoRolloutErrorComponent | ApiV1BlocksCheckCreateBlockPolyRawErrorComponent |
            ApiV1BlocksCheckCreateChangelogPolyRawErrorComponent | ApiV1BlocksCheckCreateChecksumErrorComponent |
            ApiV1BlocksCheckCreateConfigErrorComponent | ApiV1BlocksCheckCreateCreatedByBrcErrorComponent |
            ApiV1BlocksCheckCreateCreatedByComponentErrorComponent | ApiV1BlocksCheckCreateCriticalityErrorComponent |
            ApiV1BlocksCheckCreateDebugModeErrorComponent | ApiV1BlocksCheckCreateDescriptionErrorComponent |
            ApiV1BlocksCheckCreateDiscoveryEnabledErrorComponent | ApiV1BlocksCheckCreateDisplayNameErrorComponent |
            ApiV1BlocksCheckCreateDocumentationUrlErrorComponent | ApiV1BlocksCheckCreateExamplesPolyRawErrorComponent |
            ApiV1BlocksCheckCreateFlavorErrorComponent | ApiV1BlocksCheckCreateFromBlockErrorComponent |
            ApiV1BlocksCheckCreateFullSpecErrorComponent | ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponent |
            ApiV1BlocksCheckCreateIconUrlErrorComponent | ApiV1BlocksCheckCreateIsBehindStableErrorComponent |
            ApiV1BlocksCheckCreateKindErrorComponent | ApiV1BlocksCheckCreateLabelsErrorComponent |
            ApiV1BlocksCheckCreateLatestStableErrorComponent | ApiV1BlocksCheckCreateLicenseErrorComponent |
            ApiV1BlocksCheckCreateLicenseUrlErrorComponent | ApiV1BlocksCheckCreateNameErrorComponent |
            ApiV1BlocksCheckCreateNonFieldErrorsErrorComponent | ApiV1BlocksCheckCreatePlatformServiceErrorComponent |
            ApiV1BlocksCheckCreateProviderErrorComponent | ApiV1BlocksCheckCreateProviderIdErrorComponent |
            ApiV1BlocksCheckCreateProviderReferenceErrorComponent | ApiV1BlocksCheckCreateReadmeMdRawErrorComponent |
            ApiV1BlocksCheckCreateReconciliationEnabledErrorComponent | ApiV1BlocksCheckCreateRegistryUrlErrorComponent |
            ApiV1BlocksCheckCreateReleasesUrlErrorComponent | ApiV1BlocksCheckCreateScopeErrorComponent |
            ApiV1BlocksCheckCreateSlaAvailabilityErrorComponent | ApiV1BlocksCheckCreateSlaTargetErrorComponent |
            ApiV1BlocksCheckCreateSloAvailabilityErrorComponent | ApiV1BlocksCheckCreateSloTargetErrorComponent |
            ApiV1BlocksCheckCreateSupportsHaErrorComponent | ApiV1BlocksCheckCreateTargetAvailabilityErrorComponent |
            ApiV1BlocksCheckCreateTemplateBlockErrorComponent | ApiV1BlocksCheckCreateTemplateErrorComponent |
            ApiV1BlocksCheckCreateTypeErrorComponent | ApiV1BlocksCheckCreateUserSpecErrorComponent |
            ApiV1BlocksCheckCreateVersionErrorComponent | ApiV1BlocksCheckCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksCheckCreateActionsErrorComponent
        | ApiV1BlocksCheckCreateActualAvailabilityErrorComponent
        | ApiV1BlocksCheckCreateAnnotationsErrorComponent
        | ApiV1BlocksCheckCreateAppVersionErrorComponent
        | ApiV1BlocksCheckCreateArchivedAtErrorComponent
        | ApiV1BlocksCheckCreateArchivedErrorComponent
        | ApiV1BlocksCheckCreateArchivedReasonErrorComponent
        | ApiV1BlocksCheckCreateAutoRolloutErrorComponent
        | ApiV1BlocksCheckCreateBlockPolyRawErrorComponent
        | ApiV1BlocksCheckCreateChangelogPolyRawErrorComponent
        | ApiV1BlocksCheckCreateChecksumErrorComponent
        | ApiV1BlocksCheckCreateConfigErrorComponent
        | ApiV1BlocksCheckCreateCreatedByBrcErrorComponent
        | ApiV1BlocksCheckCreateCreatedByComponentErrorComponent
        | ApiV1BlocksCheckCreateCriticalityErrorComponent
        | ApiV1BlocksCheckCreateDebugModeErrorComponent
        | ApiV1BlocksCheckCreateDescriptionErrorComponent
        | ApiV1BlocksCheckCreateDiscoveryEnabledErrorComponent
        | ApiV1BlocksCheckCreateDisplayNameErrorComponent
        | ApiV1BlocksCheckCreateDocumentationUrlErrorComponent
        | ApiV1BlocksCheckCreateExamplesPolyRawErrorComponent
        | ApiV1BlocksCheckCreateFlavorErrorComponent
        | ApiV1BlocksCheckCreateFromBlockErrorComponent
        | ApiV1BlocksCheckCreateFullSpecErrorComponent
        | ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponent
        | ApiV1BlocksCheckCreateIconUrlErrorComponent
        | ApiV1BlocksCheckCreateIsBehindStableErrorComponent
        | ApiV1BlocksCheckCreateKindErrorComponent
        | ApiV1BlocksCheckCreateLabelsErrorComponent
        | ApiV1BlocksCheckCreateLatestStableErrorComponent
        | ApiV1BlocksCheckCreateLicenseErrorComponent
        | ApiV1BlocksCheckCreateLicenseUrlErrorComponent
        | ApiV1BlocksCheckCreateNameErrorComponent
        | ApiV1BlocksCheckCreateNonFieldErrorsErrorComponent
        | ApiV1BlocksCheckCreatePlatformServiceErrorComponent
        | ApiV1BlocksCheckCreateProviderErrorComponent
        | ApiV1BlocksCheckCreateProviderIdErrorComponent
        | ApiV1BlocksCheckCreateProviderReferenceErrorComponent
        | ApiV1BlocksCheckCreateReadmeMdRawErrorComponent
        | ApiV1BlocksCheckCreateReconciliationEnabledErrorComponent
        | ApiV1BlocksCheckCreateRegistryUrlErrorComponent
        | ApiV1BlocksCheckCreateReleasesUrlErrorComponent
        | ApiV1BlocksCheckCreateScopeErrorComponent
        | ApiV1BlocksCheckCreateSlaAvailabilityErrorComponent
        | ApiV1BlocksCheckCreateSlaTargetErrorComponent
        | ApiV1BlocksCheckCreateSloAvailabilityErrorComponent
        | ApiV1BlocksCheckCreateSloTargetErrorComponent
        | ApiV1BlocksCheckCreateSupportsHaErrorComponent
        | ApiV1BlocksCheckCreateTargetAvailabilityErrorComponent
        | ApiV1BlocksCheckCreateTemplateBlockErrorComponent
        | ApiV1BlocksCheckCreateTemplateErrorComponent
        | ApiV1BlocksCheckCreateTypeErrorComponent
        | ApiV1BlocksCheckCreateUserSpecErrorComponent
        | ApiV1BlocksCheckCreateVersionErrorComponent
        | ApiV1BlocksCheckCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_check_create_actions_error_component import (
            ApiV1BlocksCheckCreateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_actual_availability_error_component import (
            ApiV1BlocksCheckCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_annotations_error_component import (
            ApiV1BlocksCheckCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_app_version_error_component import (
            ApiV1BlocksCheckCreateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_archived_at_error_component import (
            ApiV1BlocksCheckCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_archived_error_component import (
            ApiV1BlocksCheckCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_archived_reason_error_component import (
            ApiV1BlocksCheckCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_auto_rollout_error_component import (
            ApiV1BlocksCheckCreateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_block_poly_raw_error_component import (
            ApiV1BlocksCheckCreateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_changelog_poly_raw_error_component import (
            ApiV1BlocksCheckCreateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_checksum_error_component import (
            ApiV1BlocksCheckCreateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_config_error_component import (
            ApiV1BlocksCheckCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_created_by_brc_error_component import (
            ApiV1BlocksCheckCreateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_criticality_error_component import (
            ApiV1BlocksCheckCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_debug_mode_error_component import (
            ApiV1BlocksCheckCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_description_error_component import (
            ApiV1BlocksCheckCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_discovery_enabled_error_component import (
            ApiV1BlocksCheckCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_display_name_error_component import (
            ApiV1BlocksCheckCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_documentation_url_error_component import (
            ApiV1BlocksCheckCreateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_examples_poly_raw_error_component import (
            ApiV1BlocksCheckCreateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_flavor_error_component import (
            ApiV1BlocksCheckCreateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_from_block_error_component import (
            ApiV1BlocksCheckCreateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_full_spec_error_component import (
            ApiV1BlocksCheckCreateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_git_repository_url_error_component import (
            ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_icon_url_error_component import (
            ApiV1BlocksCheckCreateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_is_behind_stable_error_component import (
            ApiV1BlocksCheckCreateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_kind_error_component import (
            ApiV1BlocksCheckCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_labels_error_component import (
            ApiV1BlocksCheckCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_latest_stable_error_component import (
            ApiV1BlocksCheckCreateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_license_error_component import (
            ApiV1BlocksCheckCreateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_license_url_error_component import (
            ApiV1BlocksCheckCreateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_name_error_component import (
            ApiV1BlocksCheckCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_non_field_errors_error_component import (
            ApiV1BlocksCheckCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_platform_service_error_component import (
            ApiV1BlocksCheckCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_provider_error_component import (
            ApiV1BlocksCheckCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_provider_id_error_component import (
            ApiV1BlocksCheckCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_provider_reference_error_component import (
            ApiV1BlocksCheckCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_readme_md_raw_error_component import (
            ApiV1BlocksCheckCreateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_reconciliation_enabled_error_component import (
            ApiV1BlocksCheckCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_registry_url_error_component import (
            ApiV1BlocksCheckCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_releases_url_error_component import (
            ApiV1BlocksCheckCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_scope_error_component import (
            ApiV1BlocksCheckCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_sla_availability_error_component import (
            ApiV1BlocksCheckCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_sla_target_error_component import (
            ApiV1BlocksCheckCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_slo_availability_error_component import (
            ApiV1BlocksCheckCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_slo_target_error_component import (
            ApiV1BlocksCheckCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_supports_ha_error_component import (
            ApiV1BlocksCheckCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_target_availability_error_component import (
            ApiV1BlocksCheckCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_template_block_error_component import (
            ApiV1BlocksCheckCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_template_error_component import (
            ApiV1BlocksCheckCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_type_error_component import (
            ApiV1BlocksCheckCreateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_user_spec_error_component import (
            ApiV1BlocksCheckCreateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_version_error_component import (
            ApiV1BlocksCheckCreateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_website_url_error_component import (
            ApiV1BlocksCheckCreateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksCheckCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCheckCreateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_check_create_actions_error_component import (
            ApiV1BlocksCheckCreateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_actual_availability_error_component import (
            ApiV1BlocksCheckCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_annotations_error_component import (
            ApiV1BlocksCheckCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_app_version_error_component import (
            ApiV1BlocksCheckCreateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_archived_at_error_component import (
            ApiV1BlocksCheckCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_archived_error_component import (
            ApiV1BlocksCheckCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_archived_reason_error_component import (
            ApiV1BlocksCheckCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_auto_rollout_error_component import (
            ApiV1BlocksCheckCreateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_block_poly_raw_error_component import (
            ApiV1BlocksCheckCreateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_changelog_poly_raw_error_component import (
            ApiV1BlocksCheckCreateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_checksum_error_component import (
            ApiV1BlocksCheckCreateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_config_error_component import (
            ApiV1BlocksCheckCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_created_by_brc_error_component import (
            ApiV1BlocksCheckCreateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_created_by_component_error_component import (
            ApiV1BlocksCheckCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_criticality_error_component import (
            ApiV1BlocksCheckCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_debug_mode_error_component import (
            ApiV1BlocksCheckCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_description_error_component import (
            ApiV1BlocksCheckCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_discovery_enabled_error_component import (
            ApiV1BlocksCheckCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_display_name_error_component import (
            ApiV1BlocksCheckCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_documentation_url_error_component import (
            ApiV1BlocksCheckCreateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_examples_poly_raw_error_component import (
            ApiV1BlocksCheckCreateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_flavor_error_component import (
            ApiV1BlocksCheckCreateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_from_block_error_component import (
            ApiV1BlocksCheckCreateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_full_spec_error_component import (
            ApiV1BlocksCheckCreateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_git_repository_url_error_component import (
            ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_icon_url_error_component import (
            ApiV1BlocksCheckCreateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_is_behind_stable_error_component import (
            ApiV1BlocksCheckCreateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_kind_error_component import (
            ApiV1BlocksCheckCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_labels_error_component import (
            ApiV1BlocksCheckCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_latest_stable_error_component import (
            ApiV1BlocksCheckCreateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_license_error_component import (
            ApiV1BlocksCheckCreateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_license_url_error_component import (
            ApiV1BlocksCheckCreateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_name_error_component import (
            ApiV1BlocksCheckCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_non_field_errors_error_component import (
            ApiV1BlocksCheckCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_platform_service_error_component import (
            ApiV1BlocksCheckCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_provider_error_component import (
            ApiV1BlocksCheckCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_provider_id_error_component import (
            ApiV1BlocksCheckCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_provider_reference_error_component import (
            ApiV1BlocksCheckCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_readme_md_raw_error_component import (
            ApiV1BlocksCheckCreateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_reconciliation_enabled_error_component import (
            ApiV1BlocksCheckCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_registry_url_error_component import (
            ApiV1BlocksCheckCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_releases_url_error_component import (
            ApiV1BlocksCheckCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_scope_error_component import (
            ApiV1BlocksCheckCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_sla_availability_error_component import (
            ApiV1BlocksCheckCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_sla_target_error_component import (
            ApiV1BlocksCheckCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_slo_availability_error_component import (
            ApiV1BlocksCheckCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_slo_target_error_component import (
            ApiV1BlocksCheckCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_supports_ha_error_component import (
            ApiV1BlocksCheckCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_target_availability_error_component import (
            ApiV1BlocksCheckCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_template_block_error_component import (
            ApiV1BlocksCheckCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_template_error_component import (
            ApiV1BlocksCheckCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_type_error_component import (
            ApiV1BlocksCheckCreateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_user_spec_error_component import (
            ApiV1BlocksCheckCreateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_version_error_component import (
            ApiV1BlocksCheckCreateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_check_create_website_url_error_component import (
            ApiV1BlocksCheckCreateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksCheckCreateActionsErrorComponent
                | ApiV1BlocksCheckCreateActualAvailabilityErrorComponent
                | ApiV1BlocksCheckCreateAnnotationsErrorComponent
                | ApiV1BlocksCheckCreateAppVersionErrorComponent
                | ApiV1BlocksCheckCreateArchivedAtErrorComponent
                | ApiV1BlocksCheckCreateArchivedErrorComponent
                | ApiV1BlocksCheckCreateArchivedReasonErrorComponent
                | ApiV1BlocksCheckCreateAutoRolloutErrorComponent
                | ApiV1BlocksCheckCreateBlockPolyRawErrorComponent
                | ApiV1BlocksCheckCreateChangelogPolyRawErrorComponent
                | ApiV1BlocksCheckCreateChecksumErrorComponent
                | ApiV1BlocksCheckCreateConfigErrorComponent
                | ApiV1BlocksCheckCreateCreatedByBrcErrorComponent
                | ApiV1BlocksCheckCreateCreatedByComponentErrorComponent
                | ApiV1BlocksCheckCreateCriticalityErrorComponent
                | ApiV1BlocksCheckCreateDebugModeErrorComponent
                | ApiV1BlocksCheckCreateDescriptionErrorComponent
                | ApiV1BlocksCheckCreateDiscoveryEnabledErrorComponent
                | ApiV1BlocksCheckCreateDisplayNameErrorComponent
                | ApiV1BlocksCheckCreateDocumentationUrlErrorComponent
                | ApiV1BlocksCheckCreateExamplesPolyRawErrorComponent
                | ApiV1BlocksCheckCreateFlavorErrorComponent
                | ApiV1BlocksCheckCreateFromBlockErrorComponent
                | ApiV1BlocksCheckCreateFullSpecErrorComponent
                | ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponent
                | ApiV1BlocksCheckCreateIconUrlErrorComponent
                | ApiV1BlocksCheckCreateIsBehindStableErrorComponent
                | ApiV1BlocksCheckCreateKindErrorComponent
                | ApiV1BlocksCheckCreateLabelsErrorComponent
                | ApiV1BlocksCheckCreateLatestStableErrorComponent
                | ApiV1BlocksCheckCreateLicenseErrorComponent
                | ApiV1BlocksCheckCreateLicenseUrlErrorComponent
                | ApiV1BlocksCheckCreateNameErrorComponent
                | ApiV1BlocksCheckCreateNonFieldErrorsErrorComponent
                | ApiV1BlocksCheckCreatePlatformServiceErrorComponent
                | ApiV1BlocksCheckCreateProviderErrorComponent
                | ApiV1BlocksCheckCreateProviderIdErrorComponent
                | ApiV1BlocksCheckCreateProviderReferenceErrorComponent
                | ApiV1BlocksCheckCreateReadmeMdRawErrorComponent
                | ApiV1BlocksCheckCreateReconciliationEnabledErrorComponent
                | ApiV1BlocksCheckCreateRegistryUrlErrorComponent
                | ApiV1BlocksCheckCreateReleasesUrlErrorComponent
                | ApiV1BlocksCheckCreateScopeErrorComponent
                | ApiV1BlocksCheckCreateSlaAvailabilityErrorComponent
                | ApiV1BlocksCheckCreateSlaTargetErrorComponent
                | ApiV1BlocksCheckCreateSloAvailabilityErrorComponent
                | ApiV1BlocksCheckCreateSloTargetErrorComponent
                | ApiV1BlocksCheckCreateSupportsHaErrorComponent
                | ApiV1BlocksCheckCreateTargetAvailabilityErrorComponent
                | ApiV1BlocksCheckCreateTemplateBlockErrorComponent
                | ApiV1BlocksCheckCreateTemplateErrorComponent
                | ApiV1BlocksCheckCreateTypeErrorComponent
                | ApiV1BlocksCheckCreateUserSpecErrorComponent
                | ApiV1BlocksCheckCreateVersionErrorComponent
                | ApiV1BlocksCheckCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_0 = (
                        ApiV1BlocksCheckCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_1 = (
                        ApiV1BlocksCheckCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_2 = (
                        ApiV1BlocksCheckCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_3 = (
                        ApiV1BlocksCheckCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_4 = (
                        ApiV1BlocksCheckCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_5 = (
                        ApiV1BlocksCheckCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_6 = (
                        ApiV1BlocksCheckCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_7 = (
                        ApiV1BlocksCheckCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_8 = (
                        ApiV1BlocksCheckCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_9 = (
                        ApiV1BlocksCheckCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_10 = (
                        ApiV1BlocksCheckCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_11 = (
                        ApiV1BlocksCheckCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_12 = (
                        ApiV1BlocksCheckCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_13 = (
                        ApiV1BlocksCheckCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_14 = (
                        ApiV1BlocksCheckCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_15 = (
                        ApiV1BlocksCheckCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_16 = (
                        ApiV1BlocksCheckCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_17 = (
                        ApiV1BlocksCheckCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_18 = (
                        ApiV1BlocksCheckCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_19 = (
                        ApiV1BlocksCheckCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_20 = (
                        ApiV1BlocksCheckCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_21 = (
                        ApiV1BlocksCheckCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_22 = (
                        ApiV1BlocksCheckCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_23 = (
                        ApiV1BlocksCheckCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_24 = (
                        ApiV1BlocksCheckCreateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_25 = (
                        ApiV1BlocksCheckCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_26 = (
                        ApiV1BlocksCheckCreateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_27 = (
                        ApiV1BlocksCheckCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_28 = (
                        ApiV1BlocksCheckCreateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_29 = (
                        ApiV1BlocksCheckCreateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_30 = (
                        ApiV1BlocksCheckCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_31 = (
                        ApiV1BlocksCheckCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_32 = (
                        ApiV1BlocksCheckCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_33 = (
                        ApiV1BlocksCheckCreateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_34 = (
                        ApiV1BlocksCheckCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_35 = (
                        ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_36 = (
                        ApiV1BlocksCheckCreateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_37 = (
                        ApiV1BlocksCheckCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_38 = (
                        ApiV1BlocksCheckCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_39 = (
                        ApiV1BlocksCheckCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_40 = (
                        ApiV1BlocksCheckCreateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_41 = (
                        ApiV1BlocksCheckCreateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_42 = (
                        ApiV1BlocksCheckCreateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_43 = (
                        ApiV1BlocksCheckCreateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_44 = (
                        ApiV1BlocksCheckCreateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_45 = (
                        ApiV1BlocksCheckCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_46 = (
                        ApiV1BlocksCheckCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_47 = (
                        ApiV1BlocksCheckCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_48 = (
                        ApiV1BlocksCheckCreateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_49 = (
                        ApiV1BlocksCheckCreateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_50 = (
                        ApiV1BlocksCheckCreateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_51 = (
                        ApiV1BlocksCheckCreateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_52 = (
                        ApiV1BlocksCheckCreateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_check_create_error_type_53 = (
                        ApiV1BlocksCheckCreateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_check_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_check_create_error_type_54 = (
                    ApiV1BlocksCheckCreateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_check_create_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_check_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_check_create_validation_error.additional_properties = d
        return api_v1_blocks_check_create_validation_error

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
