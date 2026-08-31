from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_blocks_create_actions_error_component import ApiV1BlocksCreateActionsErrorComponent
    from ..models.api_v1_blocks_create_actual_availability_error_component import (
        ApiV1BlocksCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_create_annotations_error_component import ApiV1BlocksCreateAnnotationsErrorComponent
    from ..models.api_v1_blocks_create_app_version_error_component import ApiV1BlocksCreateAppVersionErrorComponent
    from ..models.api_v1_blocks_create_archived_at_error_component import ApiV1BlocksCreateArchivedAtErrorComponent
    from ..models.api_v1_blocks_create_archived_error_component import ApiV1BlocksCreateArchivedErrorComponent
    from ..models.api_v1_blocks_create_archived_reason_error_component import (
        ApiV1BlocksCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_blocks_create_auto_rollout_error_component import ApiV1BlocksCreateAutoRolloutErrorComponent
    from ..models.api_v1_blocks_create_block_poly_raw_error_component import ApiV1BlocksCreateBlockPolyRawErrorComponent
    from ..models.api_v1_blocks_create_changelog_poly_raw_error_component import (
        ApiV1BlocksCreateChangelogPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_create_checksum_error_component import ApiV1BlocksCreateChecksumErrorComponent
    from ..models.api_v1_blocks_create_config_error_component import ApiV1BlocksCreateConfigErrorComponent
    from ..models.api_v1_blocks_create_created_by_brc_error_component import ApiV1BlocksCreateCreatedByBrcErrorComponent
    from ..models.api_v1_blocks_create_created_by_component_error_component import (
        ApiV1BlocksCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_blocks_create_criticality_error_component import ApiV1BlocksCreateCriticalityErrorComponent
    from ..models.api_v1_blocks_create_debug_mode_error_component import ApiV1BlocksCreateDebugModeErrorComponent
    from ..models.api_v1_blocks_create_description_error_component import ApiV1BlocksCreateDescriptionErrorComponent
    from ..models.api_v1_blocks_create_discovery_enabled_error_component import (
        ApiV1BlocksCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_create_display_name_error_component import ApiV1BlocksCreateDisplayNameErrorComponent
    from ..models.api_v1_blocks_create_documentation_url_error_component import (
        ApiV1BlocksCreateDocumentationUrlErrorComponent,
    )
    from ..models.api_v1_blocks_create_examples_poly_raw_error_component import (
        ApiV1BlocksCreateExamplesPolyRawErrorComponent,
    )
    from ..models.api_v1_blocks_create_flavor_error_component import ApiV1BlocksCreateFlavorErrorComponent
    from ..models.api_v1_blocks_create_from_block_error_component import ApiV1BlocksCreateFromBlockErrorComponent
    from ..models.api_v1_blocks_create_full_spec_error_component import ApiV1BlocksCreateFullSpecErrorComponent
    from ..models.api_v1_blocks_create_git_repository_url_error_component import (
        ApiV1BlocksCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_blocks_create_icon_url_error_component import ApiV1BlocksCreateIconUrlErrorComponent
    from ..models.api_v1_blocks_create_is_behind_stable_error_component import (
        ApiV1BlocksCreateIsBehindStableErrorComponent,
    )
    from ..models.api_v1_blocks_create_kind_error_component import ApiV1BlocksCreateKindErrorComponent
    from ..models.api_v1_blocks_create_labels_error_component import ApiV1BlocksCreateLabelsErrorComponent
    from ..models.api_v1_blocks_create_latest_stable_error_component import ApiV1BlocksCreateLatestStableErrorComponent
    from ..models.api_v1_blocks_create_license_error_component import ApiV1BlocksCreateLicenseErrorComponent
    from ..models.api_v1_blocks_create_license_url_error_component import ApiV1BlocksCreateLicenseUrlErrorComponent
    from ..models.api_v1_blocks_create_name_error_component import ApiV1BlocksCreateNameErrorComponent
    from ..models.api_v1_blocks_create_non_field_errors_error_component import (
        ApiV1BlocksCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_blocks_create_platform_service_error_component import (
        ApiV1BlocksCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_blocks_create_provider_error_component import ApiV1BlocksCreateProviderErrorComponent
    from ..models.api_v1_blocks_create_provider_id_error_component import ApiV1BlocksCreateProviderIdErrorComponent
    from ..models.api_v1_blocks_create_provider_reference_error_component import (
        ApiV1BlocksCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_blocks_create_readme_md_raw_error_component import ApiV1BlocksCreateReadmeMdRawErrorComponent
    from ..models.api_v1_blocks_create_reconciliation_enabled_error_component import (
        ApiV1BlocksCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_blocks_create_registry_url_error_component import ApiV1BlocksCreateRegistryUrlErrorComponent
    from ..models.api_v1_blocks_create_releases_url_error_component import ApiV1BlocksCreateReleasesUrlErrorComponent
    from ..models.api_v1_blocks_create_scope_error_component import ApiV1BlocksCreateScopeErrorComponent
    from ..models.api_v1_blocks_create_sla_availability_error_component import (
        ApiV1BlocksCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_create_sla_target_error_component import ApiV1BlocksCreateSlaTargetErrorComponent
    from ..models.api_v1_blocks_create_slo_availability_error_component import (
        ApiV1BlocksCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_create_slo_target_error_component import ApiV1BlocksCreateSloTargetErrorComponent
    from ..models.api_v1_blocks_create_supports_ha_error_component import ApiV1BlocksCreateSupportsHaErrorComponent
    from ..models.api_v1_blocks_create_target_availability_error_component import (
        ApiV1BlocksCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_blocks_create_template_block_error_component import (
        ApiV1BlocksCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_blocks_create_template_error_component import ApiV1BlocksCreateTemplateErrorComponent
    from ..models.api_v1_blocks_create_type_error_component import ApiV1BlocksCreateTypeErrorComponent
    from ..models.api_v1_blocks_create_user_spec_error_component import ApiV1BlocksCreateUserSpecErrorComponent
    from ..models.api_v1_blocks_create_version_error_component import ApiV1BlocksCreateVersionErrorComponent
    from ..models.api_v1_blocks_create_website_url_error_component import ApiV1BlocksCreateWebsiteUrlErrorComponent


T = TypeVar("T", bound="ApiV1BlocksCreateValidationError")


@_attrs_define
class ApiV1BlocksCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlocksCreateActionsErrorComponent | ApiV1BlocksCreateActualAvailabilityErrorComponent |
            ApiV1BlocksCreateAnnotationsErrorComponent | ApiV1BlocksCreateAppVersionErrorComponent |
            ApiV1BlocksCreateArchivedAtErrorComponent | ApiV1BlocksCreateArchivedErrorComponent |
            ApiV1BlocksCreateArchivedReasonErrorComponent | ApiV1BlocksCreateAutoRolloutErrorComponent |
            ApiV1BlocksCreateBlockPolyRawErrorComponent | ApiV1BlocksCreateChangelogPolyRawErrorComponent |
            ApiV1BlocksCreateChecksumErrorComponent | ApiV1BlocksCreateConfigErrorComponent |
            ApiV1BlocksCreateCreatedByBrcErrorComponent | ApiV1BlocksCreateCreatedByComponentErrorComponent |
            ApiV1BlocksCreateCriticalityErrorComponent | ApiV1BlocksCreateDebugModeErrorComponent |
            ApiV1BlocksCreateDescriptionErrorComponent | ApiV1BlocksCreateDiscoveryEnabledErrorComponent |
            ApiV1BlocksCreateDisplayNameErrorComponent | ApiV1BlocksCreateDocumentationUrlErrorComponent |
            ApiV1BlocksCreateExamplesPolyRawErrorComponent | ApiV1BlocksCreateFlavorErrorComponent |
            ApiV1BlocksCreateFromBlockErrorComponent | ApiV1BlocksCreateFullSpecErrorComponent |
            ApiV1BlocksCreateGitRepositoryUrlErrorComponent | ApiV1BlocksCreateIconUrlErrorComponent |
            ApiV1BlocksCreateIsBehindStableErrorComponent | ApiV1BlocksCreateKindErrorComponent |
            ApiV1BlocksCreateLabelsErrorComponent | ApiV1BlocksCreateLatestStableErrorComponent |
            ApiV1BlocksCreateLicenseErrorComponent | ApiV1BlocksCreateLicenseUrlErrorComponent |
            ApiV1BlocksCreateNameErrorComponent | ApiV1BlocksCreateNonFieldErrorsErrorComponent |
            ApiV1BlocksCreatePlatformServiceErrorComponent | ApiV1BlocksCreateProviderErrorComponent |
            ApiV1BlocksCreateProviderIdErrorComponent | ApiV1BlocksCreateProviderReferenceErrorComponent |
            ApiV1BlocksCreateReadmeMdRawErrorComponent | ApiV1BlocksCreateReconciliationEnabledErrorComponent |
            ApiV1BlocksCreateRegistryUrlErrorComponent | ApiV1BlocksCreateReleasesUrlErrorComponent |
            ApiV1BlocksCreateScopeErrorComponent | ApiV1BlocksCreateSlaAvailabilityErrorComponent |
            ApiV1BlocksCreateSlaTargetErrorComponent | ApiV1BlocksCreateSloAvailabilityErrorComponent |
            ApiV1BlocksCreateSloTargetErrorComponent | ApiV1BlocksCreateSupportsHaErrorComponent |
            ApiV1BlocksCreateTargetAvailabilityErrorComponent | ApiV1BlocksCreateTemplateBlockErrorComponent |
            ApiV1BlocksCreateTemplateErrorComponent | ApiV1BlocksCreateTypeErrorComponent |
            ApiV1BlocksCreateUserSpecErrorComponent | ApiV1BlocksCreateVersionErrorComponent |
            ApiV1BlocksCreateWebsiteUrlErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlocksCreateActionsErrorComponent
        | ApiV1BlocksCreateActualAvailabilityErrorComponent
        | ApiV1BlocksCreateAnnotationsErrorComponent
        | ApiV1BlocksCreateAppVersionErrorComponent
        | ApiV1BlocksCreateArchivedAtErrorComponent
        | ApiV1BlocksCreateArchivedErrorComponent
        | ApiV1BlocksCreateArchivedReasonErrorComponent
        | ApiV1BlocksCreateAutoRolloutErrorComponent
        | ApiV1BlocksCreateBlockPolyRawErrorComponent
        | ApiV1BlocksCreateChangelogPolyRawErrorComponent
        | ApiV1BlocksCreateChecksumErrorComponent
        | ApiV1BlocksCreateConfigErrorComponent
        | ApiV1BlocksCreateCreatedByBrcErrorComponent
        | ApiV1BlocksCreateCreatedByComponentErrorComponent
        | ApiV1BlocksCreateCriticalityErrorComponent
        | ApiV1BlocksCreateDebugModeErrorComponent
        | ApiV1BlocksCreateDescriptionErrorComponent
        | ApiV1BlocksCreateDiscoveryEnabledErrorComponent
        | ApiV1BlocksCreateDisplayNameErrorComponent
        | ApiV1BlocksCreateDocumentationUrlErrorComponent
        | ApiV1BlocksCreateExamplesPolyRawErrorComponent
        | ApiV1BlocksCreateFlavorErrorComponent
        | ApiV1BlocksCreateFromBlockErrorComponent
        | ApiV1BlocksCreateFullSpecErrorComponent
        | ApiV1BlocksCreateGitRepositoryUrlErrorComponent
        | ApiV1BlocksCreateIconUrlErrorComponent
        | ApiV1BlocksCreateIsBehindStableErrorComponent
        | ApiV1BlocksCreateKindErrorComponent
        | ApiV1BlocksCreateLabelsErrorComponent
        | ApiV1BlocksCreateLatestStableErrorComponent
        | ApiV1BlocksCreateLicenseErrorComponent
        | ApiV1BlocksCreateLicenseUrlErrorComponent
        | ApiV1BlocksCreateNameErrorComponent
        | ApiV1BlocksCreateNonFieldErrorsErrorComponent
        | ApiV1BlocksCreatePlatformServiceErrorComponent
        | ApiV1BlocksCreateProviderErrorComponent
        | ApiV1BlocksCreateProviderIdErrorComponent
        | ApiV1BlocksCreateProviderReferenceErrorComponent
        | ApiV1BlocksCreateReadmeMdRawErrorComponent
        | ApiV1BlocksCreateReconciliationEnabledErrorComponent
        | ApiV1BlocksCreateRegistryUrlErrorComponent
        | ApiV1BlocksCreateReleasesUrlErrorComponent
        | ApiV1BlocksCreateScopeErrorComponent
        | ApiV1BlocksCreateSlaAvailabilityErrorComponent
        | ApiV1BlocksCreateSlaTargetErrorComponent
        | ApiV1BlocksCreateSloAvailabilityErrorComponent
        | ApiV1BlocksCreateSloTargetErrorComponent
        | ApiV1BlocksCreateSupportsHaErrorComponent
        | ApiV1BlocksCreateTargetAvailabilityErrorComponent
        | ApiV1BlocksCreateTemplateBlockErrorComponent
        | ApiV1BlocksCreateTemplateErrorComponent
        | ApiV1BlocksCreateTypeErrorComponent
        | ApiV1BlocksCreateUserSpecErrorComponent
        | ApiV1BlocksCreateVersionErrorComponent
        | ApiV1BlocksCreateWebsiteUrlErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_blocks_create_actions_error_component import ApiV1BlocksCreateActionsErrorComponent
        from ..models.api_v1_blocks_create_actual_availability_error_component import (
            ApiV1BlocksCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_create_annotations_error_component import ApiV1BlocksCreateAnnotationsErrorComponent
        from ..models.api_v1_blocks_create_app_version_error_component import ApiV1BlocksCreateAppVersionErrorComponent
        from ..models.api_v1_blocks_create_archived_at_error_component import ApiV1BlocksCreateArchivedAtErrorComponent
        from ..models.api_v1_blocks_create_archived_error_component import ApiV1BlocksCreateArchivedErrorComponent
        from ..models.api_v1_blocks_create_archived_reason_error_component import (
            ApiV1BlocksCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_create_auto_rollout_error_component import (
            ApiV1BlocksCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_create_block_poly_raw_error_component import (
            ApiV1BlocksCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_create_changelog_poly_raw_error_component import (
            ApiV1BlocksCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_create_checksum_error_component import ApiV1BlocksCreateChecksumErrorComponent
        from ..models.api_v1_blocks_create_config_error_component import ApiV1BlocksCreateConfigErrorComponent
        from ..models.api_v1_blocks_create_created_by_brc_error_component import (
            ApiV1BlocksCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_create_criticality_error_component import ApiV1BlocksCreateCriticalityErrorComponent
        from ..models.api_v1_blocks_create_debug_mode_error_component import ApiV1BlocksCreateDebugModeErrorComponent
        from ..models.api_v1_blocks_create_description_error_component import ApiV1BlocksCreateDescriptionErrorComponent
        from ..models.api_v1_blocks_create_discovery_enabled_error_component import (
            ApiV1BlocksCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_create_display_name_error_component import (
            ApiV1BlocksCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_create_documentation_url_error_component import (
            ApiV1BlocksCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_create_examples_poly_raw_error_component import (
            ApiV1BlocksCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_create_flavor_error_component import ApiV1BlocksCreateFlavorErrorComponent
        from ..models.api_v1_blocks_create_from_block_error_component import ApiV1BlocksCreateFromBlockErrorComponent
        from ..models.api_v1_blocks_create_full_spec_error_component import ApiV1BlocksCreateFullSpecErrorComponent
        from ..models.api_v1_blocks_create_git_repository_url_error_component import (
            ApiV1BlocksCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_create_icon_url_error_component import ApiV1BlocksCreateIconUrlErrorComponent
        from ..models.api_v1_blocks_create_is_behind_stable_error_component import (
            ApiV1BlocksCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_create_kind_error_component import ApiV1BlocksCreateKindErrorComponent
        from ..models.api_v1_blocks_create_labels_error_component import ApiV1BlocksCreateLabelsErrorComponent
        from ..models.api_v1_blocks_create_latest_stable_error_component import (
            ApiV1BlocksCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_create_license_error_component import ApiV1BlocksCreateLicenseErrorComponent
        from ..models.api_v1_blocks_create_license_url_error_component import ApiV1BlocksCreateLicenseUrlErrorComponent
        from ..models.api_v1_blocks_create_name_error_component import ApiV1BlocksCreateNameErrorComponent
        from ..models.api_v1_blocks_create_non_field_errors_error_component import (
            ApiV1BlocksCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_create_platform_service_error_component import (
            ApiV1BlocksCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_create_provider_error_component import ApiV1BlocksCreateProviderErrorComponent
        from ..models.api_v1_blocks_create_provider_id_error_component import ApiV1BlocksCreateProviderIdErrorComponent
        from ..models.api_v1_blocks_create_provider_reference_error_component import (
            ApiV1BlocksCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_create_readme_md_raw_error_component import (
            ApiV1BlocksCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_create_reconciliation_enabled_error_component import (
            ApiV1BlocksCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_create_registry_url_error_component import (
            ApiV1BlocksCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_create_releases_url_error_component import (
            ApiV1BlocksCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_create_scope_error_component import ApiV1BlocksCreateScopeErrorComponent
        from ..models.api_v1_blocks_create_sla_availability_error_component import (
            ApiV1BlocksCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_create_sla_target_error_component import ApiV1BlocksCreateSlaTargetErrorComponent
        from ..models.api_v1_blocks_create_slo_availability_error_component import (
            ApiV1BlocksCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_create_slo_target_error_component import ApiV1BlocksCreateSloTargetErrorComponent
        from ..models.api_v1_blocks_create_supports_ha_error_component import ApiV1BlocksCreateSupportsHaErrorComponent
        from ..models.api_v1_blocks_create_target_availability_error_component import (
            ApiV1BlocksCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_create_template_block_error_component import (
            ApiV1BlocksCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_create_template_error_component import ApiV1BlocksCreateTemplateErrorComponent
        from ..models.api_v1_blocks_create_type_error_component import ApiV1BlocksCreateTypeErrorComponent
        from ..models.api_v1_blocks_create_user_spec_error_component import ApiV1BlocksCreateUserSpecErrorComponent
        from ..models.api_v1_blocks_create_version_error_component import ApiV1BlocksCreateVersionErrorComponent
        from ..models.api_v1_blocks_create_website_url_error_component import ApiV1BlocksCreateWebsiteUrlErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlocksCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateIconUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateFlavorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateChecksumErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateFromBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateLicenseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateLicenseUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateWebsiteUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateDocumentationUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateFullSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateUserSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateActionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateIsBehindStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateLatestStableErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateBlockPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateChangelogPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateReadmeMdRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateExamplesPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateAutoRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlocksCreateCreatedByBrcErrorComponent):
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
        from ..models.api_v1_blocks_create_actions_error_component import ApiV1BlocksCreateActionsErrorComponent
        from ..models.api_v1_blocks_create_actual_availability_error_component import (
            ApiV1BlocksCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_create_annotations_error_component import ApiV1BlocksCreateAnnotationsErrorComponent
        from ..models.api_v1_blocks_create_app_version_error_component import ApiV1BlocksCreateAppVersionErrorComponent
        from ..models.api_v1_blocks_create_archived_at_error_component import ApiV1BlocksCreateArchivedAtErrorComponent
        from ..models.api_v1_blocks_create_archived_error_component import ApiV1BlocksCreateArchivedErrorComponent
        from ..models.api_v1_blocks_create_archived_reason_error_component import (
            ApiV1BlocksCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_blocks_create_auto_rollout_error_component import (
            ApiV1BlocksCreateAutoRolloutErrorComponent,
        )
        from ..models.api_v1_blocks_create_block_poly_raw_error_component import (
            ApiV1BlocksCreateBlockPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_create_changelog_poly_raw_error_component import (
            ApiV1BlocksCreateChangelogPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_create_checksum_error_component import ApiV1BlocksCreateChecksumErrorComponent
        from ..models.api_v1_blocks_create_config_error_component import ApiV1BlocksCreateConfigErrorComponent
        from ..models.api_v1_blocks_create_created_by_brc_error_component import (
            ApiV1BlocksCreateCreatedByBrcErrorComponent,
        )
        from ..models.api_v1_blocks_create_created_by_component_error_component import (
            ApiV1BlocksCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_blocks_create_criticality_error_component import ApiV1BlocksCreateCriticalityErrorComponent
        from ..models.api_v1_blocks_create_debug_mode_error_component import ApiV1BlocksCreateDebugModeErrorComponent
        from ..models.api_v1_blocks_create_description_error_component import ApiV1BlocksCreateDescriptionErrorComponent
        from ..models.api_v1_blocks_create_discovery_enabled_error_component import (
            ApiV1BlocksCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_create_display_name_error_component import (
            ApiV1BlocksCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_blocks_create_documentation_url_error_component import (
            ApiV1BlocksCreateDocumentationUrlErrorComponent,
        )
        from ..models.api_v1_blocks_create_examples_poly_raw_error_component import (
            ApiV1BlocksCreateExamplesPolyRawErrorComponent,
        )
        from ..models.api_v1_blocks_create_flavor_error_component import ApiV1BlocksCreateFlavorErrorComponent
        from ..models.api_v1_blocks_create_from_block_error_component import ApiV1BlocksCreateFromBlockErrorComponent
        from ..models.api_v1_blocks_create_full_spec_error_component import ApiV1BlocksCreateFullSpecErrorComponent
        from ..models.api_v1_blocks_create_git_repository_url_error_component import (
            ApiV1BlocksCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_create_icon_url_error_component import ApiV1BlocksCreateIconUrlErrorComponent
        from ..models.api_v1_blocks_create_is_behind_stable_error_component import (
            ApiV1BlocksCreateIsBehindStableErrorComponent,
        )
        from ..models.api_v1_blocks_create_kind_error_component import ApiV1BlocksCreateKindErrorComponent
        from ..models.api_v1_blocks_create_labels_error_component import ApiV1BlocksCreateLabelsErrorComponent
        from ..models.api_v1_blocks_create_latest_stable_error_component import (
            ApiV1BlocksCreateLatestStableErrorComponent,
        )
        from ..models.api_v1_blocks_create_license_error_component import ApiV1BlocksCreateLicenseErrorComponent
        from ..models.api_v1_blocks_create_license_url_error_component import ApiV1BlocksCreateLicenseUrlErrorComponent
        from ..models.api_v1_blocks_create_name_error_component import ApiV1BlocksCreateNameErrorComponent
        from ..models.api_v1_blocks_create_non_field_errors_error_component import (
            ApiV1BlocksCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_blocks_create_platform_service_error_component import (
            ApiV1BlocksCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_blocks_create_provider_error_component import ApiV1BlocksCreateProviderErrorComponent
        from ..models.api_v1_blocks_create_provider_id_error_component import ApiV1BlocksCreateProviderIdErrorComponent
        from ..models.api_v1_blocks_create_provider_reference_error_component import (
            ApiV1BlocksCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_blocks_create_readme_md_raw_error_component import (
            ApiV1BlocksCreateReadmeMdRawErrorComponent,
        )
        from ..models.api_v1_blocks_create_reconciliation_enabled_error_component import (
            ApiV1BlocksCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_blocks_create_registry_url_error_component import (
            ApiV1BlocksCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_blocks_create_releases_url_error_component import (
            ApiV1BlocksCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_blocks_create_scope_error_component import ApiV1BlocksCreateScopeErrorComponent
        from ..models.api_v1_blocks_create_sla_availability_error_component import (
            ApiV1BlocksCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_create_sla_target_error_component import ApiV1BlocksCreateSlaTargetErrorComponent
        from ..models.api_v1_blocks_create_slo_availability_error_component import (
            ApiV1BlocksCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_create_slo_target_error_component import ApiV1BlocksCreateSloTargetErrorComponent
        from ..models.api_v1_blocks_create_supports_ha_error_component import ApiV1BlocksCreateSupportsHaErrorComponent
        from ..models.api_v1_blocks_create_target_availability_error_component import (
            ApiV1BlocksCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_blocks_create_template_block_error_component import (
            ApiV1BlocksCreateTemplateBlockErrorComponent,
        )
        from ..models.api_v1_blocks_create_template_error_component import ApiV1BlocksCreateTemplateErrorComponent
        from ..models.api_v1_blocks_create_type_error_component import ApiV1BlocksCreateTypeErrorComponent
        from ..models.api_v1_blocks_create_user_spec_error_component import ApiV1BlocksCreateUserSpecErrorComponent
        from ..models.api_v1_blocks_create_version_error_component import ApiV1BlocksCreateVersionErrorComponent
        from ..models.api_v1_blocks_create_website_url_error_component import ApiV1BlocksCreateWebsiteUrlErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlocksCreateActionsErrorComponent
                | ApiV1BlocksCreateActualAvailabilityErrorComponent
                | ApiV1BlocksCreateAnnotationsErrorComponent
                | ApiV1BlocksCreateAppVersionErrorComponent
                | ApiV1BlocksCreateArchivedAtErrorComponent
                | ApiV1BlocksCreateArchivedErrorComponent
                | ApiV1BlocksCreateArchivedReasonErrorComponent
                | ApiV1BlocksCreateAutoRolloutErrorComponent
                | ApiV1BlocksCreateBlockPolyRawErrorComponent
                | ApiV1BlocksCreateChangelogPolyRawErrorComponent
                | ApiV1BlocksCreateChecksumErrorComponent
                | ApiV1BlocksCreateConfigErrorComponent
                | ApiV1BlocksCreateCreatedByBrcErrorComponent
                | ApiV1BlocksCreateCreatedByComponentErrorComponent
                | ApiV1BlocksCreateCriticalityErrorComponent
                | ApiV1BlocksCreateDebugModeErrorComponent
                | ApiV1BlocksCreateDescriptionErrorComponent
                | ApiV1BlocksCreateDiscoveryEnabledErrorComponent
                | ApiV1BlocksCreateDisplayNameErrorComponent
                | ApiV1BlocksCreateDocumentationUrlErrorComponent
                | ApiV1BlocksCreateExamplesPolyRawErrorComponent
                | ApiV1BlocksCreateFlavorErrorComponent
                | ApiV1BlocksCreateFromBlockErrorComponent
                | ApiV1BlocksCreateFullSpecErrorComponent
                | ApiV1BlocksCreateGitRepositoryUrlErrorComponent
                | ApiV1BlocksCreateIconUrlErrorComponent
                | ApiV1BlocksCreateIsBehindStableErrorComponent
                | ApiV1BlocksCreateKindErrorComponent
                | ApiV1BlocksCreateLabelsErrorComponent
                | ApiV1BlocksCreateLatestStableErrorComponent
                | ApiV1BlocksCreateLicenseErrorComponent
                | ApiV1BlocksCreateLicenseUrlErrorComponent
                | ApiV1BlocksCreateNameErrorComponent
                | ApiV1BlocksCreateNonFieldErrorsErrorComponent
                | ApiV1BlocksCreatePlatformServiceErrorComponent
                | ApiV1BlocksCreateProviderErrorComponent
                | ApiV1BlocksCreateProviderIdErrorComponent
                | ApiV1BlocksCreateProviderReferenceErrorComponent
                | ApiV1BlocksCreateReadmeMdRawErrorComponent
                | ApiV1BlocksCreateReconciliationEnabledErrorComponent
                | ApiV1BlocksCreateRegistryUrlErrorComponent
                | ApiV1BlocksCreateReleasesUrlErrorComponent
                | ApiV1BlocksCreateScopeErrorComponent
                | ApiV1BlocksCreateSlaAvailabilityErrorComponent
                | ApiV1BlocksCreateSlaTargetErrorComponent
                | ApiV1BlocksCreateSloAvailabilityErrorComponent
                | ApiV1BlocksCreateSloTargetErrorComponent
                | ApiV1BlocksCreateSupportsHaErrorComponent
                | ApiV1BlocksCreateTargetAvailabilityErrorComponent
                | ApiV1BlocksCreateTemplateBlockErrorComponent
                | ApiV1BlocksCreateTemplateErrorComponent
                | ApiV1BlocksCreateTypeErrorComponent
                | ApiV1BlocksCreateUserSpecErrorComponent
                | ApiV1BlocksCreateVersionErrorComponent
                | ApiV1BlocksCreateWebsiteUrlErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_0 = (
                        ApiV1BlocksCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_1 = ApiV1BlocksCreateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_2 = (
                        ApiV1BlocksCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_3 = (
                        ApiV1BlocksCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_4 = (
                        ApiV1BlocksCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_5 = (
                        ApiV1BlocksCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_6 = (
                        ApiV1BlocksCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_7 = (
                        ApiV1BlocksCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_8 = (
                        ApiV1BlocksCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_9 = (
                        ApiV1BlocksCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_10 = (
                        ApiV1BlocksCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_11 = (
                        ApiV1BlocksCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_12 = (
                        ApiV1BlocksCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_13 = (
                        ApiV1BlocksCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_14 = (
                        ApiV1BlocksCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_15 = (
                        ApiV1BlocksCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_16 = (
                        ApiV1BlocksCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_17 = (
                        ApiV1BlocksCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_18 = (
                        ApiV1BlocksCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_19 = (
                        ApiV1BlocksCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_20 = (
                        ApiV1BlocksCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_21 = (
                        ApiV1BlocksCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_22 = (
                        ApiV1BlocksCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_23 = (
                        ApiV1BlocksCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_24 = (
                        ApiV1BlocksCreateIconUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_25 = (
                        ApiV1BlocksCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_26 = (
                        ApiV1BlocksCreateFlavorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_27 = (
                        ApiV1BlocksCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_28 = (
                        ApiV1BlocksCreateChecksumErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_29 = (
                        ApiV1BlocksCreateFromBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_30 = (
                        ApiV1BlocksCreateAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_31 = (
                        ApiV1BlocksCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_32 = (
                        ApiV1BlocksCreateLicenseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_33 = (
                        ApiV1BlocksCreateLicenseUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_34 = (
                        ApiV1BlocksCreateWebsiteUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_35 = (
                        ApiV1BlocksCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_36 = (
                        ApiV1BlocksCreateDocumentationUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_37 = (
                        ApiV1BlocksCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_38 = (
                        ApiV1BlocksCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_39 = (
                        ApiV1BlocksCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_40 = (
                        ApiV1BlocksCreateFullSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_41 = (
                        ApiV1BlocksCreateUserSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_42 = (
                        ApiV1BlocksCreateActionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_43 = (
                        ApiV1BlocksCreateIsBehindStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_44 = (
                        ApiV1BlocksCreateLatestStableErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_45 = (
                        ApiV1BlocksCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_46 = (
                        ApiV1BlocksCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_47 = (
                        ApiV1BlocksCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_48 = (
                        ApiV1BlocksCreateBlockPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_49 = (
                        ApiV1BlocksCreateChangelogPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_50 = (
                        ApiV1BlocksCreateReadmeMdRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_51 = (
                        ApiV1BlocksCreateExamplesPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_52 = (
                        ApiV1BlocksCreateAutoRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_blocks_create_error_type_53 = (
                        ApiV1BlocksCreateCreatedByBrcErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_blocks_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_blocks_create_error_type_54 = (
                    ApiV1BlocksCreateCreatedByComponentErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_blocks_create_error_type_54

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_blocks_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_blocks_create_validation_error.additional_properties = d
        return api_v1_blocks_create_validation_error

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
