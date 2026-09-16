from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_logs_reload_create_actions_error_component import (
        ApiV1BlocksLogsReloadCreateActionsErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_actual_availability_error_component import (
        ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_annotations_error_component import (
        ApiV1BlocksLogsReloadCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_app_version_error_component import (
        ApiV1BlocksLogsReloadCreateAppVersionErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_archived_at_error_component import (
        ApiV1BlocksLogsReloadCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_archived_error_component import (
        ApiV1BlocksLogsReloadCreateArchivedErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_archived_reason_error_component import (
        ApiV1BlocksLogsReloadCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_auto_rollout_error_component import (
        ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_block_poly_raw_error_component import (
        ApiV1BlocksLogsReloadCreateBlockPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_changelog_poly_raw_error_component import (
        ApiV1BlocksLogsReloadCreateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_checksum_error_component import (
        ApiV1BlocksLogsReloadCreateChecksumErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_config_error_component import (
        ApiV1BlocksLogsReloadCreateConfigErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_created_by_brc_error_component import (
        ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_created_by_component_error_component import (
        ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_criticality_error_component import (
        ApiV1BlocksLogsReloadCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_debug_mode_error_component import (
        ApiV1BlocksLogsReloadCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_description_error_component import (
        ApiV1BlocksLogsReloadCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_discovery_enabled_error_component import (
        ApiV1BlocksLogsReloadCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_display_name_error_component import (
        ApiV1BlocksLogsReloadCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_documentation_url_error_component import (
        ApiV1BlocksLogsReloadCreateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_examples_poly_raw_error_component import (
        ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_flavor_error_component import (
        ApiV1BlocksLogsReloadCreateFlavorErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_from_block_error_component import (
        ApiV1BlocksLogsReloadCreateFromBlockErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_full_spec_error_component import (
        ApiV1BlocksLogsReloadCreateFullSpecErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_git_repository_url_error_component import (
        ApiV1BlocksLogsReloadCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_icon_url_error_component import (
        ApiV1BlocksLogsReloadCreateIconUrlErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_is_behind_stable_error_component import (
        ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_kind_error_component import (
        ApiV1BlocksLogsReloadCreateKindErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_labels_error_component import (
        ApiV1BlocksLogsReloadCreateLabelsErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_latest_stable_error_component import (
        ApiV1BlocksLogsReloadCreateLatestStableErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_license_error_component import (
        ApiV1BlocksLogsReloadCreateLicenseErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_license_url_error_component import (
        ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_name_error_component import (
        ApiV1BlocksLogsReloadCreateNameErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_non_field_errors_error_component import (
        ApiV1BlocksLogsReloadCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_platform_service_error_component import (
        ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_provider_error_component import (
        ApiV1BlocksLogsReloadCreateProviderErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_provider_id_error_component import (
        ApiV1BlocksLogsReloadCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_provider_reference_error_component import (
        ApiV1BlocksLogsReloadCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_readme_md_raw_error_component import (
        ApiV1BlocksLogsReloadCreateReadmeMdRawErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_reconciliation_enabled_error_component import (
        ApiV1BlocksLogsReloadCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_registry_url_error_component import (
        ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_releases_url_error_component import (
        ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_scope_error_component import (
        ApiV1BlocksLogsReloadCreateScopeErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_sla_availability_error_component import (
        ApiV1BlocksLogsReloadCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_sla_target_error_component import (
        ApiV1BlocksLogsReloadCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_slo_availability_error_component import (
        ApiV1BlocksLogsReloadCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_slo_target_error_component import (
        ApiV1BlocksLogsReloadCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_supports_ha_error_component import (
        ApiV1BlocksLogsReloadCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_target_availability_error_component import (
        ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_template_block_error_component import (
        ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_template_error_component import (
        ApiV1BlocksLogsReloadCreateTemplateErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_type_error_component import (
        ApiV1BlocksLogsReloadCreateTypeErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_user_spec_error_component import (
        ApiV1BlocksLogsReloadCreateUserSpecErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_version_error_component import (
        ApiV1BlocksLogsReloadCreateVersionErrorComponent,
    )
    from ..models.api_v1_blocks_logs_reload_create_website_url_error_component import (
        ApiV1BlocksLogsReloadCreateWebsiteUrlErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlocksLogsReloadCreateValidationError")


@_attrs_define
class ApiV1BlocksLogsReloadCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksLogsReloadCreateActionsErrorComponent |
            ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponent |
            ApiV1BlocksLogsReloadCreateAnnotationsErrorComponent | ApiV1BlocksLogsReloadCreateAppVersionErrorComponent |
            ApiV1BlocksLogsReloadCreateArchivedAtErrorComponent | ApiV1BlocksLogsReloadCreateArchivedErrorComponent |
            ApiV1BlocksLogsReloadCreateArchivedReasonErrorComponent | ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponent |
            ApiV1BlocksLogsReloadCreateBlockPolyRawErrorComponent |
            ApiV1BlocksLogsReloadCreateChangelogPolyRawErrorComponent | ApiV1BlocksLogsReloadCreateChecksumErrorComponent |
            ApiV1BlocksLogsReloadCreateConfigErrorComponent | ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponent |
            ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponent |
            ApiV1BlocksLogsReloadCreateCriticalityErrorComponent | ApiV1BlocksLogsReloadCreateDebugModeErrorComponent |
            ApiV1BlocksLogsReloadCreateDescriptionErrorComponent | ApiV1BlocksLogsReloadCreateDiscoveryEnabledErrorComponent
            | ApiV1BlocksLogsReloadCreateDisplayNameErrorComponent |
            ApiV1BlocksLogsReloadCreateDocumentationUrlErrorComponent |
            ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponent | ApiV1BlocksLogsReloadCreateFlavorErrorComponent |
            ApiV1BlocksLogsReloadCreateFromBlockErrorComponent | ApiV1BlocksLogsReloadCreateFullSpecErrorComponent |
            ApiV1BlocksLogsReloadCreateGitRepositoryUrlErrorComponent | ApiV1BlocksLogsReloadCreateIconUrlErrorComponent |
            ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponent | ApiV1BlocksLogsReloadCreateKindErrorComponent |
            ApiV1BlocksLogsReloadCreateLabelsErrorComponent | ApiV1BlocksLogsReloadCreateLatestStableErrorComponent |
            ApiV1BlocksLogsReloadCreateLicenseErrorComponent | ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponent |
            ApiV1BlocksLogsReloadCreateNameErrorComponent | ApiV1BlocksLogsReloadCreateNonFieldErrorsErrorComponent |
            ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponent | ApiV1BlocksLogsReloadCreateProviderErrorComponent |
            ApiV1BlocksLogsReloadCreateProviderIdErrorComponent | ApiV1BlocksLogsReloadCreateProviderReferenceErrorComponent
            | ApiV1BlocksLogsReloadCreateReadmeMdRawErrorComponent |
            ApiV1BlocksLogsReloadCreateReconciliationEnabledErrorComponent |
            ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponent | ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponent |
            ApiV1BlocksLogsReloadCreateScopeErrorComponent | ApiV1BlocksLogsReloadCreateSlaAvailabilityErrorComponent |
            ApiV1BlocksLogsReloadCreateSlaTargetErrorComponent | ApiV1BlocksLogsReloadCreateSloAvailabilityErrorComponent |
            ApiV1BlocksLogsReloadCreateSloTargetErrorComponent | ApiV1BlocksLogsReloadCreateSupportsHaErrorComponent |
            ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponent |
            ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponent | ApiV1BlocksLogsReloadCreateTemplateErrorComponent |
            ApiV1BlocksLogsReloadCreateTypeErrorComponent | ApiV1BlocksLogsReloadCreateUserSpecErrorComponent |
            ApiV1BlocksLogsReloadCreateVersionErrorComponent | ApiV1BlocksLogsReloadCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksLogsReloadCreateActionsErrorComponent
        | ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponent
        | ApiV1BlocksLogsReloadCreateAnnotationsErrorComponent
        | ApiV1BlocksLogsReloadCreateAppVersionErrorComponent
        | ApiV1BlocksLogsReloadCreateArchivedAtErrorComponent
        | ApiV1BlocksLogsReloadCreateArchivedErrorComponent
        | ApiV1BlocksLogsReloadCreateArchivedReasonErrorComponent
        | ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponent
        | ApiV1BlocksLogsReloadCreateBlockPolyRawErrorComponent
        | ApiV1BlocksLogsReloadCreateChangelogPolyRawErrorComponent
        | ApiV1BlocksLogsReloadCreateChecksumErrorComponent
        | ApiV1BlocksLogsReloadCreateConfigErrorComponent
        | ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponent
        | ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponent
        | ApiV1BlocksLogsReloadCreateCriticalityErrorComponent
        | ApiV1BlocksLogsReloadCreateDebugModeErrorComponent
        | ApiV1BlocksLogsReloadCreateDescriptionErrorComponent
        | ApiV1BlocksLogsReloadCreateDiscoveryEnabledErrorComponent
        | ApiV1BlocksLogsReloadCreateDisplayNameErrorComponent
        | ApiV1BlocksLogsReloadCreateDocumentationUrlErrorComponent
        | ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponent
        | ApiV1BlocksLogsReloadCreateFlavorErrorComponent
        | ApiV1BlocksLogsReloadCreateFromBlockErrorComponent
        | ApiV1BlocksLogsReloadCreateFullSpecErrorComponent
        | ApiV1BlocksLogsReloadCreateGitRepositoryUrlErrorComponent
        | ApiV1BlocksLogsReloadCreateIconUrlErrorComponent
        | ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponent
        | ApiV1BlocksLogsReloadCreateKindErrorComponent
        | ApiV1BlocksLogsReloadCreateLabelsErrorComponent
        | ApiV1BlocksLogsReloadCreateLatestStableErrorComponent
        | ApiV1BlocksLogsReloadCreateLicenseErrorComponent
        | ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponent
        | ApiV1BlocksLogsReloadCreateNameErrorComponent
        | ApiV1BlocksLogsReloadCreateNonFieldErrorsErrorComponent
        | ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponent
        | ApiV1BlocksLogsReloadCreateProviderErrorComponent
        | ApiV1BlocksLogsReloadCreateProviderIdErrorComponent
        | ApiV1BlocksLogsReloadCreateProviderReferenceErrorComponent
        | ApiV1BlocksLogsReloadCreateReadmeMdRawErrorComponent
        | ApiV1BlocksLogsReloadCreateReconciliationEnabledErrorComponent
        | ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponent
        | ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponent
        | ApiV1BlocksLogsReloadCreateScopeErrorComponent
        | ApiV1BlocksLogsReloadCreateSlaAvailabilityErrorComponent
        | ApiV1BlocksLogsReloadCreateSlaTargetErrorComponent
        | ApiV1BlocksLogsReloadCreateSloAvailabilityErrorComponent
        | ApiV1BlocksLogsReloadCreateSloTargetErrorComponent
        | ApiV1BlocksLogsReloadCreateSupportsHaErrorComponent
        | ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponent
        | ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponent
        | ApiV1BlocksLogsReloadCreateTemplateErrorComponent
        | ApiV1BlocksLogsReloadCreateTypeErrorComponent
        | ApiV1BlocksLogsReloadCreateUserSpecErrorComponent
        | ApiV1BlocksLogsReloadCreateVersionErrorComponent
        | ApiV1BlocksLogsReloadCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_logs_reload_create_actions_error_component import (
            ApiV1BlocksLogsReloadCreateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_actual_availability_error_component import (
            ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_annotations_error_component import (
            ApiV1BlocksLogsReloadCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_app_version_error_component import (
            ApiV1BlocksLogsReloadCreateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_archived_at_error_component import (
            ApiV1BlocksLogsReloadCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_archived_error_component import (
            ApiV1BlocksLogsReloadCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_archived_reason_error_component import (
            ApiV1BlocksLogsReloadCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_auto_rollout_error_component import (
            ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_block_poly_raw_error_component import (
            ApiV1BlocksLogsReloadCreateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_changelog_poly_raw_error_component import (
            ApiV1BlocksLogsReloadCreateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_checksum_error_component import (
            ApiV1BlocksLogsReloadCreateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_config_error_component import (
            ApiV1BlocksLogsReloadCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_created_by_brc_error_component import (
            ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_criticality_error_component import (
            ApiV1BlocksLogsReloadCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_debug_mode_error_component import (
            ApiV1BlocksLogsReloadCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_description_error_component import (
            ApiV1BlocksLogsReloadCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_discovery_enabled_error_component import (
            ApiV1BlocksLogsReloadCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_display_name_error_component import (
            ApiV1BlocksLogsReloadCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_documentation_url_error_component import (
            ApiV1BlocksLogsReloadCreateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_examples_poly_raw_error_component import (
            ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_flavor_error_component import (
            ApiV1BlocksLogsReloadCreateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_from_block_error_component import (
            ApiV1BlocksLogsReloadCreateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_full_spec_error_component import (
            ApiV1BlocksLogsReloadCreateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_git_repository_url_error_component import (
            ApiV1BlocksLogsReloadCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_icon_url_error_component import (
            ApiV1BlocksLogsReloadCreateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_is_behind_stable_error_component import (
            ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_kind_error_component import (
            ApiV1BlocksLogsReloadCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_labels_error_component import (
            ApiV1BlocksLogsReloadCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_latest_stable_error_component import (
            ApiV1BlocksLogsReloadCreateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_license_error_component import (
            ApiV1BlocksLogsReloadCreateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_license_url_error_component import (
            ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_name_error_component import (
            ApiV1BlocksLogsReloadCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_non_field_errors_error_component import (
            ApiV1BlocksLogsReloadCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_platform_service_error_component import (
            ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_provider_error_component import (
            ApiV1BlocksLogsReloadCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_provider_id_error_component import (
            ApiV1BlocksLogsReloadCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_provider_reference_error_component import (
            ApiV1BlocksLogsReloadCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_readme_md_raw_error_component import (
            ApiV1BlocksLogsReloadCreateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_reconciliation_enabled_error_component import (
            ApiV1BlocksLogsReloadCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_registry_url_error_component import (
            ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_releases_url_error_component import (
            ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_scope_error_component import (
            ApiV1BlocksLogsReloadCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_sla_availability_error_component import (
            ApiV1BlocksLogsReloadCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_sla_target_error_component import (
            ApiV1BlocksLogsReloadCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_slo_availability_error_component import (
            ApiV1BlocksLogsReloadCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_slo_target_error_component import (
            ApiV1BlocksLogsReloadCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_supports_ha_error_component import (
            ApiV1BlocksLogsReloadCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_target_availability_error_component import (
            ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_template_block_error_component import (
            ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_template_error_component import (
            ApiV1BlocksLogsReloadCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_type_error_component import (
            ApiV1BlocksLogsReloadCreateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_user_spec_error_component import (
            ApiV1BlocksLogsReloadCreateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_version_error_component import (
            ApiV1BlocksLogsReloadCreateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_website_url_error_component import (
            ApiV1BlocksLogsReloadCreateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_logs_reload_create_actions_error_component import (
            ApiV1BlocksLogsReloadCreateActionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_actual_availability_error_component import (
            ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_annotations_error_component import (
            ApiV1BlocksLogsReloadCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_app_version_error_component import (
            ApiV1BlocksLogsReloadCreateAppVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_archived_at_error_component import (
            ApiV1BlocksLogsReloadCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_archived_error_component import (
            ApiV1BlocksLogsReloadCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_archived_reason_error_component import (
            ApiV1BlocksLogsReloadCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_auto_rollout_error_component import (
            ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_block_poly_raw_error_component import (
            ApiV1BlocksLogsReloadCreateBlockPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_changelog_poly_raw_error_component import (
            ApiV1BlocksLogsReloadCreateChangelogPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_checksum_error_component import (
            ApiV1BlocksLogsReloadCreateChecksumErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_config_error_component import (
            ApiV1BlocksLogsReloadCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_created_by_brc_error_component import (
            ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_created_by_component_error_component import (
            ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_criticality_error_component import (
            ApiV1BlocksLogsReloadCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_debug_mode_error_component import (
            ApiV1BlocksLogsReloadCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_description_error_component import (
            ApiV1BlocksLogsReloadCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_discovery_enabled_error_component import (
            ApiV1BlocksLogsReloadCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_display_name_error_component import (
            ApiV1BlocksLogsReloadCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_documentation_url_error_component import (
            ApiV1BlocksLogsReloadCreateDocumentationUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_examples_poly_raw_error_component import (
            ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_flavor_error_component import (
            ApiV1BlocksLogsReloadCreateFlavorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_from_block_error_component import (
            ApiV1BlocksLogsReloadCreateFromBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_full_spec_error_component import (
            ApiV1BlocksLogsReloadCreateFullSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_git_repository_url_error_component import (
            ApiV1BlocksLogsReloadCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_icon_url_error_component import (
            ApiV1BlocksLogsReloadCreateIconUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_is_behind_stable_error_component import (
            ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_kind_error_component import (
            ApiV1BlocksLogsReloadCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_labels_error_component import (
            ApiV1BlocksLogsReloadCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_latest_stable_error_component import (
            ApiV1BlocksLogsReloadCreateLatestStableErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_license_error_component import (
            ApiV1BlocksLogsReloadCreateLicenseErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_license_url_error_component import (
            ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_name_error_component import (
            ApiV1BlocksLogsReloadCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_non_field_errors_error_component import (
            ApiV1BlocksLogsReloadCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_platform_service_error_component import (
            ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_provider_error_component import (
            ApiV1BlocksLogsReloadCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_provider_id_error_component import (
            ApiV1BlocksLogsReloadCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_provider_reference_error_component import (
            ApiV1BlocksLogsReloadCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_readme_md_raw_error_component import (
            ApiV1BlocksLogsReloadCreateReadmeMdRawErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_reconciliation_enabled_error_component import (
            ApiV1BlocksLogsReloadCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_registry_url_error_component import (
            ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_releases_url_error_component import (
            ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_scope_error_component import (
            ApiV1BlocksLogsReloadCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_sla_availability_error_component import (
            ApiV1BlocksLogsReloadCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_sla_target_error_component import (
            ApiV1BlocksLogsReloadCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_slo_availability_error_component import (
            ApiV1BlocksLogsReloadCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_slo_target_error_component import (
            ApiV1BlocksLogsReloadCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_supports_ha_error_component import (
            ApiV1BlocksLogsReloadCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_target_availability_error_component import (
            ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_template_block_error_component import (
            ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_template_error_component import (
            ApiV1BlocksLogsReloadCreateTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_type_error_component import (
            ApiV1BlocksLogsReloadCreateTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_user_spec_error_component import (
            ApiV1BlocksLogsReloadCreateUserSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_version_error_component import (
            ApiV1BlocksLogsReloadCreateVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_blocks_logs_reload_create_website_url_error_component import (
            ApiV1BlocksLogsReloadCreateWebsiteUrlErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksLogsReloadCreateActionsErrorComponent
                | ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponent
                | ApiV1BlocksLogsReloadCreateAnnotationsErrorComponent
                | ApiV1BlocksLogsReloadCreateAppVersionErrorComponent
                | ApiV1BlocksLogsReloadCreateArchivedAtErrorComponent
                | ApiV1BlocksLogsReloadCreateArchivedErrorComponent
                | ApiV1BlocksLogsReloadCreateArchivedReasonErrorComponent
                | ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponent
                | ApiV1BlocksLogsReloadCreateBlockPolyRawErrorComponent
                | ApiV1BlocksLogsReloadCreateChangelogPolyRawErrorComponent
                | ApiV1BlocksLogsReloadCreateChecksumErrorComponent
                | ApiV1BlocksLogsReloadCreateConfigErrorComponent
                | ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponent
                | ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponent
                | ApiV1BlocksLogsReloadCreateCriticalityErrorComponent
                | ApiV1BlocksLogsReloadCreateDebugModeErrorComponent
                | ApiV1BlocksLogsReloadCreateDescriptionErrorComponent
                | ApiV1BlocksLogsReloadCreateDiscoveryEnabledErrorComponent
                | ApiV1BlocksLogsReloadCreateDisplayNameErrorComponent
                | ApiV1BlocksLogsReloadCreateDocumentationUrlErrorComponent
                | ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponent
                | ApiV1BlocksLogsReloadCreateFlavorErrorComponent
                | ApiV1BlocksLogsReloadCreateFromBlockErrorComponent
                | ApiV1BlocksLogsReloadCreateFullSpecErrorComponent
                | ApiV1BlocksLogsReloadCreateGitRepositoryUrlErrorComponent
                | ApiV1BlocksLogsReloadCreateIconUrlErrorComponent
                | ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponent
                | ApiV1BlocksLogsReloadCreateKindErrorComponent
                | ApiV1BlocksLogsReloadCreateLabelsErrorComponent
                | ApiV1BlocksLogsReloadCreateLatestStableErrorComponent
                | ApiV1BlocksLogsReloadCreateLicenseErrorComponent
                | ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponent
                | ApiV1BlocksLogsReloadCreateNameErrorComponent
                | ApiV1BlocksLogsReloadCreateNonFieldErrorsErrorComponent
                | ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponent
                | ApiV1BlocksLogsReloadCreateProviderErrorComponent
                | ApiV1BlocksLogsReloadCreateProviderIdErrorComponent
                | ApiV1BlocksLogsReloadCreateProviderReferenceErrorComponent
                | ApiV1BlocksLogsReloadCreateReadmeMdRawErrorComponent
                | ApiV1BlocksLogsReloadCreateReconciliationEnabledErrorComponent
                | ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponent
                | ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponent
                | ApiV1BlocksLogsReloadCreateScopeErrorComponent
                | ApiV1BlocksLogsReloadCreateSlaAvailabilityErrorComponent
                | ApiV1BlocksLogsReloadCreateSlaTargetErrorComponent
                | ApiV1BlocksLogsReloadCreateSloAvailabilityErrorComponent
                | ApiV1BlocksLogsReloadCreateSloTargetErrorComponent
                | ApiV1BlocksLogsReloadCreateSupportsHaErrorComponent
                | ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponent
                | ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponent
                | ApiV1BlocksLogsReloadCreateTemplateErrorComponent
                | ApiV1BlocksLogsReloadCreateTypeErrorComponent
                | ApiV1BlocksLogsReloadCreateUserSpecErrorComponent
                | ApiV1BlocksLogsReloadCreateVersionErrorComponent
                | ApiV1BlocksLogsReloadCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_0 = (
                        ApiV1BlocksLogsReloadCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_1 = (
                        ApiV1BlocksLogsReloadCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_2 = (
                        ApiV1BlocksLogsReloadCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_3 = (
                        ApiV1BlocksLogsReloadCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_4 = (
                        ApiV1BlocksLogsReloadCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_5 = (
                        ApiV1BlocksLogsReloadCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_6 = (
                        ApiV1BlocksLogsReloadCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_7 = (
                        ApiV1BlocksLogsReloadCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_8 = (
                        ApiV1BlocksLogsReloadCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_9 = (
                        ApiV1BlocksLogsReloadCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_10 = (
                        ApiV1BlocksLogsReloadCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_11 = (
                        ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_12 = (
                        ApiV1BlocksLogsReloadCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_13 = (
                        ApiV1BlocksLogsReloadCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_14 = (
                        ApiV1BlocksLogsReloadCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_15 = (
                        ApiV1BlocksLogsReloadCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_16 = (
                        ApiV1BlocksLogsReloadCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_17 = (
                        ApiV1BlocksLogsReloadCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_18 = (
                        ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_19 = (
                        ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_20 = (
                        ApiV1BlocksLogsReloadCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_21 = (
                        ApiV1BlocksLogsReloadCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_22 = (
                        ApiV1BlocksLogsReloadCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_23 = (
                        ApiV1BlocksLogsReloadCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_24 = (
                        ApiV1BlocksLogsReloadCreateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_25 = (
                        ApiV1BlocksLogsReloadCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_26 = (
                        ApiV1BlocksLogsReloadCreateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_27 = (
                        ApiV1BlocksLogsReloadCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_28 = (
                        ApiV1BlocksLogsReloadCreateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_29 = (
                        ApiV1BlocksLogsReloadCreateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_30 = (
                        ApiV1BlocksLogsReloadCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_31 = (
                        ApiV1BlocksLogsReloadCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_32 = (
                        ApiV1BlocksLogsReloadCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_33 = (
                        ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_34 = (
                        ApiV1BlocksLogsReloadCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_35 = (
                        ApiV1BlocksLogsReloadCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_36 = (
                        ApiV1BlocksLogsReloadCreateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_37 = (
                        ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_38 = (
                        ApiV1BlocksLogsReloadCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_39 = (
                        ApiV1BlocksLogsReloadCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_40 = (
                        ApiV1BlocksLogsReloadCreateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_41 = (
                        ApiV1BlocksLogsReloadCreateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_42 = (
                        ApiV1BlocksLogsReloadCreateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_43 = (
                        ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_44 = (
                        ApiV1BlocksLogsReloadCreateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_45 = (
                        ApiV1BlocksLogsReloadCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_46 = (
                        ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_47 = (
                        ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_48 = (
                        ApiV1BlocksLogsReloadCreateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_49 = (
                        ApiV1BlocksLogsReloadCreateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_50 = (
                        ApiV1BlocksLogsReloadCreateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_51 = (
                        ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_52 = (
                        ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_logs_reload_create_error_type_53 = (
                        ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_logs_reload_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_logs_reload_create_error_type_54 = (
                    ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_logs_reload_create_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_logs_reload_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_logs_reload_create_validation_error.additional_properties = d
        return api_v1_blocks_logs_reload_create_validation_error

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
