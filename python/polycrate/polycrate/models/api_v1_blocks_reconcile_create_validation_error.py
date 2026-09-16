from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_reconcile_create_actions_error_component import (
        ApiV1BlocksReconcileCreateActionsErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_actual_availability_error_component import (
        ApiV1BlocksReconcileCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_annotations_error_component import (
        ApiV1BlocksReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_app_version_error_component import (
        ApiV1BlocksReconcileCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_archived_at_error_component import (
        ApiV1BlocksReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_archived_error_component import (
        ApiV1BlocksReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_archived_reason_error_component import (
        ApiV1BlocksReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_auto_rollout_error_component import (
        ApiV1BlocksReconcileCreateAutoRolloutErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_block_poly_raw_error_component import (
        ApiV1BlocksReconcileCreateBlockPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_changelog_poly_raw_error_component import (
        ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_checksum_error_component import (
        ApiV1BlocksReconcileCreateChecksumErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_config_error_component import (
        ApiV1BlocksReconcileCreateConfigErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_created_by_brc_error_component import (
        ApiV1BlocksReconcileCreateCreatedByBrcErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_created_by_component_error_component import (
        ApiV1BlocksReconcileCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_criticality_error_component import (
        ApiV1BlocksReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_debug_mode_error_component import (
        ApiV1BlocksReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_description_error_component import (
        ApiV1BlocksReconcileCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_discovery_enabled_error_component import (
        ApiV1BlocksReconcileCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_display_name_error_component import (
        ApiV1BlocksReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_documentation_url_error_component import (
        ApiV1BlocksReconcileCreateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_examples_poly_raw_error_component import (
        ApiV1BlocksReconcileCreateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_flavor_error_component import (
        ApiV1BlocksReconcileCreateFlavorErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_from_block_error_component import (
        ApiV1BlocksReconcileCreateFromBlockErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_full_spec_error_component import (
        ApiV1BlocksReconcileCreateFullSpecErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_git_repository_url_error_component import (
        ApiV1BlocksReconcileCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_icon_url_error_component import (
        ApiV1BlocksReconcileCreateIconUrlErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_is_behind_stable_error_component import (
        ApiV1BlocksReconcileCreateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_kind_error_component import (
        ApiV1BlocksReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_labels_error_component import (
        ApiV1BlocksReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_latest_stable_error_component import (
        ApiV1BlocksReconcileCreateLatestStableErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_license_error_component import (
        ApiV1BlocksReconcileCreateLicenseErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_license_url_error_component import (
        ApiV1BlocksReconcileCreateLicenseUrlErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_name_error_component import (
        ApiV1BlocksReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_non_field_errors_error_component import (
        ApiV1BlocksReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_platform_service_error_component import (
        ApiV1BlocksReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_provider_error_component import (
        ApiV1BlocksReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_provider_id_error_component import (
        ApiV1BlocksReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_provider_reference_error_component import (
        ApiV1BlocksReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_readme_md_raw_error_component import (
        ApiV1BlocksReconcileCreateReadmeMdRawErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1BlocksReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_registry_url_error_component import (
        ApiV1BlocksReconcileCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_releases_url_error_component import (
        ApiV1BlocksReconcileCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_scope_error_component import (
        ApiV1BlocksReconcileCreateScopeErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_sla_availability_error_component import (
        ApiV1BlocksReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_sla_target_error_component import (
        ApiV1BlocksReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_slo_availability_error_component import (
        ApiV1BlocksReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_slo_target_error_component import (
        ApiV1BlocksReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_supports_ha_error_component import (
        ApiV1BlocksReconcileCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_target_availability_error_component import (
        ApiV1BlocksReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_template_block_error_component import (
        ApiV1BlocksReconcileCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_template_error_component import (
        ApiV1BlocksReconcileCreateTemplateErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_type_error_component import (
        ApiV1BlocksReconcileCreateTypeErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_user_spec_error_component import (
        ApiV1BlocksReconcileCreateUserSpecErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_version_error_component import (
        ApiV1BlocksReconcileCreateVersionErrorComponent,
    )
    from ..models.api_v1_blocks_reconcile_create_website_url_error_component import (
        ApiV1BlocksReconcileCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlocksReconcileCreateValidationError")


@_attrs_define
class ApiV1BlocksReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksReconcileCreateActionsErrorComponent |
            ApiV1BlocksReconcileCreateActualAvailabilityErrorComponent | ApiV1BlocksReconcileCreateAnnotationsErrorComponent
            | ApiV1BlocksReconcileCreateAppVersionErrorComponent | ApiV1BlocksReconcileCreateArchivedAtErrorComponent |
            ApiV1BlocksReconcileCreateArchivedErrorComponent | ApiV1BlocksReconcileCreateArchivedReasonErrorComponent |
            ApiV1BlocksReconcileCreateAutoRolloutErrorComponent | ApiV1BlocksReconcileCreateBlockPolyRawErrorComponent |
            ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponent | ApiV1BlocksReconcileCreateChecksumErrorComponent |
            ApiV1BlocksReconcileCreateConfigErrorComponent | ApiV1BlocksReconcileCreateCreatedByBrcErrorComponent |
            ApiV1BlocksReconcileCreateCreatedByComponentErrorComponent | ApiV1BlocksReconcileCreateCriticalityErrorComponent
            | ApiV1BlocksReconcileCreateDebugModeErrorComponent | ApiV1BlocksReconcileCreateDescriptionErrorComponent |
            ApiV1BlocksReconcileCreateDiscoveryEnabledErrorComponent | ApiV1BlocksReconcileCreateDisplayNameErrorComponent |
            ApiV1BlocksReconcileCreateDocumentationUrlErrorComponent |
            ApiV1BlocksReconcileCreateExamplesPolyRawErrorComponent | ApiV1BlocksReconcileCreateFlavorErrorComponent |
            ApiV1BlocksReconcileCreateFromBlockErrorComponent | ApiV1BlocksReconcileCreateFullSpecErrorComponent |
            ApiV1BlocksReconcileCreateGitRepositoryUrlErrorComponent | ApiV1BlocksReconcileCreateIconUrlErrorComponent |
            ApiV1BlocksReconcileCreateIsBehindStableErrorComponent | ApiV1BlocksReconcileCreateKindErrorComponent |
            ApiV1BlocksReconcileCreateLabelsErrorComponent | ApiV1BlocksReconcileCreateLatestStableErrorComponent |
            ApiV1BlocksReconcileCreateLicenseErrorComponent | ApiV1BlocksReconcileCreateLicenseUrlErrorComponent |
            ApiV1BlocksReconcileCreateNameErrorComponent | ApiV1BlocksReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1BlocksReconcileCreatePlatformServiceErrorComponent | ApiV1BlocksReconcileCreateProviderErrorComponent |
            ApiV1BlocksReconcileCreateProviderIdErrorComponent | ApiV1BlocksReconcileCreateProviderReferenceErrorComponent |
            ApiV1BlocksReconcileCreateReadmeMdRawErrorComponent |
            ApiV1BlocksReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1BlocksReconcileCreateRegistryUrlErrorComponent | ApiV1BlocksReconcileCreateReleasesUrlErrorComponent |
            ApiV1BlocksReconcileCreateScopeErrorComponent | ApiV1BlocksReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1BlocksReconcileCreateSlaTargetErrorComponent | ApiV1BlocksReconcileCreateSloAvailabilityErrorComponent |
            ApiV1BlocksReconcileCreateSloTargetErrorComponent | ApiV1BlocksReconcileCreateSupportsHaErrorComponent |
            ApiV1BlocksReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1BlocksReconcileCreateTemplateBlockErrorComponent | ApiV1BlocksReconcileCreateTemplateErrorComponent |
            ApiV1BlocksReconcileCreateTypeErrorComponent | ApiV1BlocksReconcileCreateUserSpecErrorComponent |
            ApiV1BlocksReconcileCreateVersionErrorComponent | ApiV1BlocksReconcileCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksReconcileCreateActionsErrorComponent
        | ApiV1BlocksReconcileCreateActualAvailabilityErrorComponent
        | ApiV1BlocksReconcileCreateAnnotationsErrorComponent
        | ApiV1BlocksReconcileCreateAppVersionErrorComponent
        | ApiV1BlocksReconcileCreateArchivedAtErrorComponent
        | ApiV1BlocksReconcileCreateArchivedErrorComponent
        | ApiV1BlocksReconcileCreateArchivedReasonErrorComponent
        | ApiV1BlocksReconcileCreateAutoRolloutErrorComponent
        | ApiV1BlocksReconcileCreateBlockPolyRawErrorComponent
        | ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponent
        | ApiV1BlocksReconcileCreateChecksumErrorComponent
        | ApiV1BlocksReconcileCreateConfigErrorComponent
        | ApiV1BlocksReconcileCreateCreatedByBrcErrorComponent
        | ApiV1BlocksReconcileCreateCreatedByComponentErrorComponent
        | ApiV1BlocksReconcileCreateCriticalityErrorComponent
        | ApiV1BlocksReconcileCreateDebugModeErrorComponent
        | ApiV1BlocksReconcileCreateDescriptionErrorComponent
        | ApiV1BlocksReconcileCreateDiscoveryEnabledErrorComponent
        | ApiV1BlocksReconcileCreateDisplayNameErrorComponent
        | ApiV1BlocksReconcileCreateDocumentationUrlErrorComponent
        | ApiV1BlocksReconcileCreateExamplesPolyRawErrorComponent
        | ApiV1BlocksReconcileCreateFlavorErrorComponent
        | ApiV1BlocksReconcileCreateFromBlockErrorComponent
        | ApiV1BlocksReconcileCreateFullSpecErrorComponent
        | ApiV1BlocksReconcileCreateGitRepositoryUrlErrorComponent
        | ApiV1BlocksReconcileCreateIconUrlErrorComponent
        | ApiV1BlocksReconcileCreateIsBehindStableErrorComponent
        | ApiV1BlocksReconcileCreateKindErrorComponent
        | ApiV1BlocksReconcileCreateLabelsErrorComponent
        | ApiV1BlocksReconcileCreateLatestStableErrorComponent
        | ApiV1BlocksReconcileCreateLicenseErrorComponent
        | ApiV1BlocksReconcileCreateLicenseUrlErrorComponent
        | ApiV1BlocksReconcileCreateNameErrorComponent
        | ApiV1BlocksReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1BlocksReconcileCreatePlatformServiceErrorComponent
        | ApiV1BlocksReconcileCreateProviderErrorComponent
        | ApiV1BlocksReconcileCreateProviderIdErrorComponent
        | ApiV1BlocksReconcileCreateProviderReferenceErrorComponent
        | ApiV1BlocksReconcileCreateReadmeMdRawErrorComponent
        | ApiV1BlocksReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1BlocksReconcileCreateRegistryUrlErrorComponent
        | ApiV1BlocksReconcileCreateReleasesUrlErrorComponent
        | ApiV1BlocksReconcileCreateScopeErrorComponent
        | ApiV1BlocksReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1BlocksReconcileCreateSlaTargetErrorComponent
        | ApiV1BlocksReconcileCreateSloAvailabilityErrorComponent
        | ApiV1BlocksReconcileCreateSloTargetErrorComponent
        | ApiV1BlocksReconcileCreateSupportsHaErrorComponent
        | ApiV1BlocksReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1BlocksReconcileCreateTemplateBlockErrorComponent
        | ApiV1BlocksReconcileCreateTemplateErrorComponent
        | ApiV1BlocksReconcileCreateTypeErrorComponent
        | ApiV1BlocksReconcileCreateUserSpecErrorComponent
        | ApiV1BlocksReconcileCreateVersionErrorComponent
        | ApiV1BlocksReconcileCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_reconcile_create_actions_error_component import (
            ApiV1BlocksReconcileCreateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_actual_availability_error_component import (
            ApiV1BlocksReconcileCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_annotations_error_component import (
            ApiV1BlocksReconcileCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_app_version_error_component import (
            ApiV1BlocksReconcileCreateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_archived_at_error_component import (
            ApiV1BlocksReconcileCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_archived_error_component import (
            ApiV1BlocksReconcileCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_archived_reason_error_component import (
            ApiV1BlocksReconcileCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_auto_rollout_error_component import (
            ApiV1BlocksReconcileCreateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_block_poly_raw_error_component import (
            ApiV1BlocksReconcileCreateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_changelog_poly_raw_error_component import (
            ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_checksum_error_component import (
            ApiV1BlocksReconcileCreateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_config_error_component import (
            ApiV1BlocksReconcileCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_created_by_brc_error_component import (
            ApiV1BlocksReconcileCreateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_criticality_error_component import (
            ApiV1BlocksReconcileCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_debug_mode_error_component import (
            ApiV1BlocksReconcileCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_description_error_component import (
            ApiV1BlocksReconcileCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_discovery_enabled_error_component import (
            ApiV1BlocksReconcileCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_display_name_error_component import (
            ApiV1BlocksReconcileCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_documentation_url_error_component import (
            ApiV1BlocksReconcileCreateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_examples_poly_raw_error_component import (
            ApiV1BlocksReconcileCreateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_flavor_error_component import (
            ApiV1BlocksReconcileCreateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_from_block_error_component import (
            ApiV1BlocksReconcileCreateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_full_spec_error_component import (
            ApiV1BlocksReconcileCreateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_git_repository_url_error_component import (
            ApiV1BlocksReconcileCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_icon_url_error_component import (
            ApiV1BlocksReconcileCreateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_is_behind_stable_error_component import (
            ApiV1BlocksReconcileCreateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_kind_error_component import (
            ApiV1BlocksReconcileCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_labels_error_component import (
            ApiV1BlocksReconcileCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_latest_stable_error_component import (
            ApiV1BlocksReconcileCreateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_license_error_component import (
            ApiV1BlocksReconcileCreateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_license_url_error_component import (
            ApiV1BlocksReconcileCreateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_name_error_component import (
            ApiV1BlocksReconcileCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_non_field_errors_error_component import (
            ApiV1BlocksReconcileCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_platform_service_error_component import (
            ApiV1BlocksReconcileCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_provider_error_component import (
            ApiV1BlocksReconcileCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_provider_id_error_component import (
            ApiV1BlocksReconcileCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_provider_reference_error_component import (
            ApiV1BlocksReconcileCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_readme_md_raw_error_component import (
            ApiV1BlocksReconcileCreateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1BlocksReconcileCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_registry_url_error_component import (
            ApiV1BlocksReconcileCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_releases_url_error_component import (
            ApiV1BlocksReconcileCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_scope_error_component import (
            ApiV1BlocksReconcileCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_sla_availability_error_component import (
            ApiV1BlocksReconcileCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_sla_target_error_component import (
            ApiV1BlocksReconcileCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_slo_availability_error_component import (
            ApiV1BlocksReconcileCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_slo_target_error_component import (
            ApiV1BlocksReconcileCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_supports_ha_error_component import (
            ApiV1BlocksReconcileCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_target_availability_error_component import (
            ApiV1BlocksReconcileCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_template_block_error_component import (
            ApiV1BlocksReconcileCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_template_error_component import (
            ApiV1BlocksReconcileCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_type_error_component import (
            ApiV1BlocksReconcileCreateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_user_spec_error_component import (
            ApiV1BlocksReconcileCreateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_version_error_component import (
            ApiV1BlocksReconcileCreateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_website_url_error_component import (
            ApiV1BlocksReconcileCreateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksReconcileCreateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_reconcile_create_actions_error_component import (
            ApiV1BlocksReconcileCreateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_actual_availability_error_component import (
            ApiV1BlocksReconcileCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_annotations_error_component import (
            ApiV1BlocksReconcileCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_app_version_error_component import (
            ApiV1BlocksReconcileCreateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_archived_at_error_component import (
            ApiV1BlocksReconcileCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_archived_error_component import (
            ApiV1BlocksReconcileCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_archived_reason_error_component import (
            ApiV1BlocksReconcileCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_auto_rollout_error_component import (
            ApiV1BlocksReconcileCreateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_block_poly_raw_error_component import (
            ApiV1BlocksReconcileCreateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_changelog_poly_raw_error_component import (
            ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_checksum_error_component import (
            ApiV1BlocksReconcileCreateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_config_error_component import (
            ApiV1BlocksReconcileCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_created_by_brc_error_component import (
            ApiV1BlocksReconcileCreateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_created_by_component_error_component import (
            ApiV1BlocksReconcileCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_criticality_error_component import (
            ApiV1BlocksReconcileCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_debug_mode_error_component import (
            ApiV1BlocksReconcileCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_description_error_component import (
            ApiV1BlocksReconcileCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_discovery_enabled_error_component import (
            ApiV1BlocksReconcileCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_display_name_error_component import (
            ApiV1BlocksReconcileCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_documentation_url_error_component import (
            ApiV1BlocksReconcileCreateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_examples_poly_raw_error_component import (
            ApiV1BlocksReconcileCreateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_flavor_error_component import (
            ApiV1BlocksReconcileCreateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_from_block_error_component import (
            ApiV1BlocksReconcileCreateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_full_spec_error_component import (
            ApiV1BlocksReconcileCreateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_git_repository_url_error_component import (
            ApiV1BlocksReconcileCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_icon_url_error_component import (
            ApiV1BlocksReconcileCreateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_is_behind_stable_error_component import (
            ApiV1BlocksReconcileCreateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_kind_error_component import (
            ApiV1BlocksReconcileCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_labels_error_component import (
            ApiV1BlocksReconcileCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_latest_stable_error_component import (
            ApiV1BlocksReconcileCreateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_license_error_component import (
            ApiV1BlocksReconcileCreateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_license_url_error_component import (
            ApiV1BlocksReconcileCreateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_name_error_component import (
            ApiV1BlocksReconcileCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_non_field_errors_error_component import (
            ApiV1BlocksReconcileCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_platform_service_error_component import (
            ApiV1BlocksReconcileCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_provider_error_component import (
            ApiV1BlocksReconcileCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_provider_id_error_component import (
            ApiV1BlocksReconcileCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_provider_reference_error_component import (
            ApiV1BlocksReconcileCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_readme_md_raw_error_component import (
            ApiV1BlocksReconcileCreateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1BlocksReconcileCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_registry_url_error_component import (
            ApiV1BlocksReconcileCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_releases_url_error_component import (
            ApiV1BlocksReconcileCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_scope_error_component import (
            ApiV1BlocksReconcileCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_sla_availability_error_component import (
            ApiV1BlocksReconcileCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_sla_target_error_component import (
            ApiV1BlocksReconcileCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_slo_availability_error_component import (
            ApiV1BlocksReconcileCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_slo_target_error_component import (
            ApiV1BlocksReconcileCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_supports_ha_error_component import (
            ApiV1BlocksReconcileCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_target_availability_error_component import (
            ApiV1BlocksReconcileCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_template_block_error_component import (
            ApiV1BlocksReconcileCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_template_error_component import (
            ApiV1BlocksReconcileCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_type_error_component import (
            ApiV1BlocksReconcileCreateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_user_spec_error_component import (
            ApiV1BlocksReconcileCreateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_version_error_component import (
            ApiV1BlocksReconcileCreateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_reconcile_create_website_url_error_component import (
            ApiV1BlocksReconcileCreateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksReconcileCreateActionsErrorComponent
                | ApiV1BlocksReconcileCreateActualAvailabilityErrorComponent
                | ApiV1BlocksReconcileCreateAnnotationsErrorComponent
                | ApiV1BlocksReconcileCreateAppVersionErrorComponent
                | ApiV1BlocksReconcileCreateArchivedAtErrorComponent
                | ApiV1BlocksReconcileCreateArchivedErrorComponent
                | ApiV1BlocksReconcileCreateArchivedReasonErrorComponent
                | ApiV1BlocksReconcileCreateAutoRolloutErrorComponent
                | ApiV1BlocksReconcileCreateBlockPolyRawErrorComponent
                | ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponent
                | ApiV1BlocksReconcileCreateChecksumErrorComponent
                | ApiV1BlocksReconcileCreateConfigErrorComponent
                | ApiV1BlocksReconcileCreateCreatedByBrcErrorComponent
                | ApiV1BlocksReconcileCreateCreatedByComponentErrorComponent
                | ApiV1BlocksReconcileCreateCriticalityErrorComponent
                | ApiV1BlocksReconcileCreateDebugModeErrorComponent
                | ApiV1BlocksReconcileCreateDescriptionErrorComponent
                | ApiV1BlocksReconcileCreateDiscoveryEnabledErrorComponent
                | ApiV1BlocksReconcileCreateDisplayNameErrorComponent
                | ApiV1BlocksReconcileCreateDocumentationUrlErrorComponent
                | ApiV1BlocksReconcileCreateExamplesPolyRawErrorComponent
                | ApiV1BlocksReconcileCreateFlavorErrorComponent
                | ApiV1BlocksReconcileCreateFromBlockErrorComponent
                | ApiV1BlocksReconcileCreateFullSpecErrorComponent
                | ApiV1BlocksReconcileCreateGitRepositoryUrlErrorComponent
                | ApiV1BlocksReconcileCreateIconUrlErrorComponent
                | ApiV1BlocksReconcileCreateIsBehindStableErrorComponent
                | ApiV1BlocksReconcileCreateKindErrorComponent
                | ApiV1BlocksReconcileCreateLabelsErrorComponent
                | ApiV1BlocksReconcileCreateLatestStableErrorComponent
                | ApiV1BlocksReconcileCreateLicenseErrorComponent
                | ApiV1BlocksReconcileCreateLicenseUrlErrorComponent
                | ApiV1BlocksReconcileCreateNameErrorComponent
                | ApiV1BlocksReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1BlocksReconcileCreatePlatformServiceErrorComponent
                | ApiV1BlocksReconcileCreateProviderErrorComponent
                | ApiV1BlocksReconcileCreateProviderIdErrorComponent
                | ApiV1BlocksReconcileCreateProviderReferenceErrorComponent
                | ApiV1BlocksReconcileCreateReadmeMdRawErrorComponent
                | ApiV1BlocksReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1BlocksReconcileCreateRegistryUrlErrorComponent
                | ApiV1BlocksReconcileCreateReleasesUrlErrorComponent
                | ApiV1BlocksReconcileCreateScopeErrorComponent
                | ApiV1BlocksReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1BlocksReconcileCreateSlaTargetErrorComponent
                | ApiV1BlocksReconcileCreateSloAvailabilityErrorComponent
                | ApiV1BlocksReconcileCreateSloTargetErrorComponent
                | ApiV1BlocksReconcileCreateSupportsHaErrorComponent
                | ApiV1BlocksReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1BlocksReconcileCreateTemplateBlockErrorComponent
                | ApiV1BlocksReconcileCreateTemplateErrorComponent
                | ApiV1BlocksReconcileCreateTypeErrorComponent
                | ApiV1BlocksReconcileCreateUserSpecErrorComponent
                | ApiV1BlocksReconcileCreateVersionErrorComponent
                | ApiV1BlocksReconcileCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_0 = (
                        ApiV1BlocksReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_1 = (
                        ApiV1BlocksReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_2 = (
                        ApiV1BlocksReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_3 = (
                        ApiV1BlocksReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_4 = (
                        ApiV1BlocksReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_5 = (
                        ApiV1BlocksReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_6 = (
                        ApiV1BlocksReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_7 = (
                        ApiV1BlocksReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_8 = (
                        ApiV1BlocksReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_9 = (
                        ApiV1BlocksReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_10 = (
                        ApiV1BlocksReconcileCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_11 = (
                        ApiV1BlocksReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_12 = (
                        ApiV1BlocksReconcileCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_13 = (
                        ApiV1BlocksReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_14 = (
                        ApiV1BlocksReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_15 = (
                        ApiV1BlocksReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_16 = (
                        ApiV1BlocksReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_17 = (
                        ApiV1BlocksReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_18 = (
                        ApiV1BlocksReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_19 = (
                        ApiV1BlocksReconcileCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_20 = (
                        ApiV1BlocksReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_21 = (
                        ApiV1BlocksReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_22 = (
                        ApiV1BlocksReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_23 = (
                        ApiV1BlocksReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_24 = (
                        ApiV1BlocksReconcileCreateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_25 = (
                        ApiV1BlocksReconcileCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_26 = (
                        ApiV1BlocksReconcileCreateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_27 = (
                        ApiV1BlocksReconcileCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_28 = (
                        ApiV1BlocksReconcileCreateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_29 = (
                        ApiV1BlocksReconcileCreateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_30 = (
                        ApiV1BlocksReconcileCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_31 = (
                        ApiV1BlocksReconcileCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_32 = (
                        ApiV1BlocksReconcileCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_33 = (
                        ApiV1BlocksReconcileCreateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_34 = (
                        ApiV1BlocksReconcileCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_35 = (
                        ApiV1BlocksReconcileCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_36 = (
                        ApiV1BlocksReconcileCreateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_37 = (
                        ApiV1BlocksReconcileCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_38 = (
                        ApiV1BlocksReconcileCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_39 = (
                        ApiV1BlocksReconcileCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_40 = (
                        ApiV1BlocksReconcileCreateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_41 = (
                        ApiV1BlocksReconcileCreateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_42 = (
                        ApiV1BlocksReconcileCreateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_43 = (
                        ApiV1BlocksReconcileCreateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_44 = (
                        ApiV1BlocksReconcileCreateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_45 = (
                        ApiV1BlocksReconcileCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_46 = (
                        ApiV1BlocksReconcileCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_47 = (
                        ApiV1BlocksReconcileCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_48 = (
                        ApiV1BlocksReconcileCreateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_49 = (
                        ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_50 = (
                        ApiV1BlocksReconcileCreateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_51 = (
                        ApiV1BlocksReconcileCreateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_52 = (
                        ApiV1BlocksReconcileCreateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_reconcile_create_error_type_53 = (
                        ApiV1BlocksReconcileCreateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_reconcile_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_reconcile_create_error_type_54 = (
                    ApiV1BlocksReconcileCreateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_reconcile_create_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_reconcile_create_validation_error.additional_properties = d
        return api_v1_blocks_reconcile_create_validation_error

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
